import pytest

from src.models import Category, Product


class TestProduct:
    def test_product_initialization(self):
        product = Product("Test Phone", "Description", 1000.0, 5)
        assert product.name == "Test Phone"
        assert product.description == "Description"
        assert product.price == 1000.0
        assert product.stock == 5

    def test_product_price_setter_positive(self):
        p = Product("Test", "Desc", 100.0, 5)
        p.price = 200.0
        assert p.price == 200.0

    def test_product_price_setter_negative(self):
        p = Product("Test", "Desc", 100.0, 5)
        p.price = -10.0
        assert p.price == 100.0

    def test_product_price_lower_with_confirmation(self, monkeypatch):
        p = Product("Test", "Desc", 500.0, 5)
        monkeypatch.setattr("builtins.input", lambda _: "y")
        p.price = 300.0
        assert p.price == 300.0

    def test_product_price_lower_declined(self, monkeypatch):
        p = Product("Test", "Desc", 500.0, 5)
        monkeypatch.setattr("builtins.input", lambda _: "n")
        p.price = 300.0
        assert p.price == 500.0

    def test_product_price_lower_any_other_input_declined(self, monkeypatch):
        p = Product("Test", "Desc", 500.0, 5)
        monkeypatch.setattr("builtins.input", lambda _: "что-то непонятное")
        p.price = 300.0
        assert p.price == 500.0


class TestCategory:
    @pytest.fixture(autouse=True)
    def reset_counters(self):
        Category.product_count = 0

    def test_category_creation(self):
        cat = Category("Phones", "All phones")
        assert Category.product_count == 0
        assert len(cat._Category__products) == 0

    def test_add_product_updates_count_and_list(self):
        cat = Category("TVs", "All TVs")
        p1 = Product("TV 1", "Desc", 5000.0, 1)
        cat.add_product(p1)
        assert Category.product_count == 1
        assert len(cat._Category__products) == 1

    def test_multiple_products_update_count_correctly(self):
        cat = Category("Laptops", "All laptops")
        p1 = Product("Laptop 1", "Desc", 1000.0, 1)
        p2 = Product("Laptop 2", "Desc", 1200.0, 1)
        cat.add_product(p1)
        cat.add_product(p2)
        assert Category.product_count == 2
        assert len(cat._Category__products) == 2

    def test_category_products_getter_format(self):
        cat = Category("Phones", "All phones")
        p = Product("Phone", "Good phone", 1000.0, 10)
        cat.add_product(p)
        result = cat.products
        assert result == "Phone, 1000.0 руб. Остаток: 10 шт.\n"

    def test_category_new_product_classmethod(self):
        data = {
            "name": "Phone",
            "description": "Good phone",
            "price": 1000.0,
            "stock": 10,
        }
        p = Category.new_product(data)
        assert isinstance(p, Product)
        assert p.name == "Phone"
        assert p.price == 1000.0
        assert p.stock == 10
