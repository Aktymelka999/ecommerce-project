import pytest

from src.models import Category, Product, ProductIterator


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

    def test_product_str(self):
        p = Product("Samsung Galaxy S23 Ultra", "256GB", 180000.0, 5)
        assert str(p) == "Samsung Galaxy S23 Ultra, 180000.00 руб. Остаток: 5 шт."

    def test_product_str_zero_stock(self):
        p = Product("Пустой товар", "Нет в наличии", 500.0, 0)
        assert str(p) == "Пустой товар, 500.00 руб. Остаток: 0 шт."

    def test_product_str_large_values(self):
        p = Product("Дорогой товар", "Описание", 99999999.0, 1000000)
        result = str(p)
        assert "99999999.00 руб." in result
        assert "1000000 шт." in result

    def test_product_add_basic(self):
        a = Product("Товар A", "Описание", 100.0, 10)
        b = Product("Товар B", "Описание", 200.0, 2)
        assert a + b == 1400.0

    def test_product_add_zero_stock(self):
        a = Product("Товар A", "Описание", 100.0, 0)
        b = Product("Товар B", "Описание", 200.0, 5)
        assert a + b == 1000.0

    def test_product_add_both_zero_stock(self):
        a = Product("Товар A", "Описание", 100.0, 0)
        b = Product("Товар B", "Описание", 200.0, 0)
        assert a + b == 0.0

    def test_product_add_type_error(self):
        a = Product("Товар A", "Описание", 100.0, 10)
        with pytest.raises(TypeError):
            _ = a + "не товар"

    def test_product_add_type_error_int(self):
        a = Product("Товар A", "Описание", 100.0, 10)
        with pytest.raises(TypeError):
            _ = a + 42


class TestCategory:
    @pytest.fixture(autouse=True)
    def reset_counters(self):
        Category.product_count = 0
        Category.category_count = 0

    def test_category_creation(self):
        cat = Category("Phones", "All phones")
        assert Category.product_count == 0
        assert Category.category_count == 1
        assert len(cat._Category__products) == 0

    def test_add_product_updates_count_and_list(self):
        cat = Category("TVs", "All TVs")
        p1 = Product("TV 1", "Desc", 5000.0, 1)
        cat.add_product(p1)
        assert Category.product_count == 1
        assert Category.category_count == 1
        assert len(cat._Category__products) == 1

    def test_multiple_products_update_count_correctly(self):
        cat = Category("Laptops", "All laptops")
        p1 = Product("Laptop 1", "Desc", 1000.0, 1)
        p2 = Product("Laptop 2", "Desc", 1200.0, 1)
        cat.add_product(p1)
        cat.add_product(p2)
        assert Category.product_count == 2
        assert Category.category_count == 1
        assert len(cat._Category__products) == 2

    def test_category_products_getter_returns_list(self):
        cat = Category("Phones", "All phones")
        p = Product("Phone", "Good phone", 1000.0, 10)
        cat.add_product(p)
        result = cat.products
        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0] is p

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

    def test_category_str_empty(self):
        cat = Category("Пустая", "Нет товаров")
        assert str(cat) == "Пустая, количество продуктов: 0 шт."

    def test_category_str_with_products(self):
        p1 = Product("Телефон 1", "Описание", 1000.0, 5)
        p2 = Product("Телефон 2", "Описание", 2000.0, 10)
        cat = Category("Смартфоны", "Все смартфоны", [p1, p2])
        assert str(cat) == "Смартфоны, количество продуктов: 15 шт."

    def test_category_str_single_product(self):
        p = Product("Только один", "Описание", 500.0, 3)
        cat = Category("Категория", "Описание", [p])
        assert str(cat) == "Категория, количество продуктов: 3 шт."


class TestProductIterator:
    """Тесты для вспомогательного класса-итератора."""

    def test_iterate_over_products(self):
        p1 = Product("Phone 1", "Desc", 1000.0, 2)
        p2 = Product("Phone 2", "Desc", 2000.0, 3)
        p3 = Product("Phone 3", "Desc", 3000.0, 4)
        cat = Category("Phones", "All phones", [p1, p2, p3])

        iterator = ProductIterator(cat)
        result = list(iterator)
        assert result == [p1, p2, p3]

    def test_iterate_empty_category(self):
        cat = Category("Empty", "No products")
        iterator = ProductIterator(cat)
        result = list(iterator)
        assert result == []

    def test_iterate_single_product(self):
        p = Product("Single", "Desc", 100.0, 1)
        cat = Category("One", "Single product", [p])
        iterator = ProductIterator(cat)
        result = list(iterator)
        assert result == [p]

    def test_iterator_stop_iteration(self):
        p1 = Product("Phone 1", "Desc", 1000.0, 2)
        cat = Category("Phones", "All phones", [p1])
        iterator = ProductIterator(cat)

        first = next(iterator)
        assert first is p1

        with pytest.raises(StopIteration):
            next(iterator)

    def test_iterator_is_iterable(self):
        p1 = Product("Phone 1", "Desc", 1000.0, 2)
        p2 = Product("Phone 2", "Desc", 2000.0, 3)
        cat = Category("Phones", "All phones", [p1, p2])

        iterator = ProductIterator(cat)
        assert iter(iterator) is iterator

    def test_iterator_in_for_loop(self):
        p1 = Product("Phone 1", "Desc", 1000.0, 2)
        p2 = Product("Phone 2", "Desc", 2000.0, 3)
        p3 = Product("Phone 3", "Desc", 3000.0, 4)
        cat = Category("Phones", "All phones", [p1, p2, p3])

        collected = []
        for product in ProductIterator(cat):
            collected.append(product)

        assert collected == [p1, p2, p3]

    def test_iterator_does_not_modify_category(self):
        p1 = Product("Phone 1", "Desc", 1000.0, 2)
        p2 = Product("Phone 2", "Desc", 2000.0, 3)
        cat = Category("Phones", "All phones", [p1, p2])

        iterator = ProductIterator(cat)
        list(iterator)

        assert len(cat.products) == 2
