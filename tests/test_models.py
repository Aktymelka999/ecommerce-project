import pytest
from src.models import Product, Category


class TestProduct:
    def test_product_initialization(self):
        product = Product("Test Phone", "Description", 1000.0, 5)
        assert product.name == "Test Phone"
        assert product.description == "Description"
        assert product.price == 1000.0
        assert product.quantity == 5


class TestCategory:
    @pytest.fixture(autouse=True)
    def reset_counters(self):
        Category.category_count = 0
        Category.product_count = 0

    def test_category_initialization_and_counts(self):
        p1 = Product("Phone 1", "Desc", 1000.0, 1)
        p2 = Product("Phone 2", "Desc", 2000.0, 2)
        category = Category("Phones", "All phones", [p1, p2])

        assert category.name == "Phones"
        assert len(category.products) == 2
        assert Category.category_count == 1
        assert Category.product_count == 2

    def test_add_product_updates_count(self):
        p1 = Product("TV 1", "Desc", 5000.0, 1)
        category = Category("TVs", "All TVs", [])

        assert Category.category_count == 1
        assert Category.product_count == 0

        category.add_product(p1)

        assert Category.product_count == 1
        assert p1 in category.products
