
import pytest
from src.models import Product, Category


class TestProduct:
    def test_product_initialization(self):
        product = Product(
            name="Laptop",
            description="Powerful laptop for developers",
            price=999.99,
            quantity=10,
        )
        assert product.name == "Laptop"
        assert product.description == "Powerful laptop for developers"
        assert product.price == 999.99
        assert product.quantity == 10


class TestCategory:
    def test_category_initialization_with_products(self):
        p1 = Product("Mouse", "Wireless mouse", 29.99, 50)
        p2 = Product("Keyboard", "Mechanical keyboard", 79.99, 30)
        category = Category("Electronics", "All electronic devices", [p1, p2])

        assert category.name == "Electronics"
        assert category.description == "All electronic devices"
        assert len(category.products) == 2
        # Самое важное: сравниваем элементы списка, а не весь список с одним объектом
        assert category.products[0] is p1
        assert category.products[1] is p2

    def test_category_initialization_without_products(self):
        category = Category("Books", "All kinds of books")
        assert category.name == "Books"
        assert category.products == []

    def test_category_counters_on_creation(self):
        Category.category_count = 0
        Category.product_count = 0

        p1 = Product("Book A", "Description A", 15.0, 100)
        p2 = Product("Book B", "Description B", 20.0, 50)
        Category("Books", "All books", [p1, p2])

        assert Category.category_count == 1
        assert Category.product_count == 2

    def test_category_counters_on_add_product(self):
        Category.category_count = 0
        Category.product_count = 0

        category = Category("Toys", "All toys")
        p = Product("Toy Car", "Red toy car", 9.99, 200)
        category.add_product(p)

        assert Category.category_count == 1
        assert Category.product_count == 1