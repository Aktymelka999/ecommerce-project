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
        # Сбрасываем счетчики перед каждым тестом, чтобы они были независимы
        Category.category_count = 0
        Category.product_count = 0

    def test_category_creation_updates_category_count(self):
        # Создаем категорию без товаров
        cat = Category("Phones", "All phones")
        assert Category.category_count == 1
        assert Category.product_count == 0
        assert len(cat.products) == 0

    def test_add_product_updates_product_count(self):
        # Создаем категорию
        cat = Category("TVs", "All TVs")
        assert Category.category_count == 1
        assert Category.product_count == 0
        
        # Добавляем товар
        p1 = Product("TV 1", "Desc", 5000.0, 1)
        cat.add_product(p1)
        
        # Проверяем, что счетчик вырос
        assert Category.product_count == 1
        assert len(cat.products) == 1

    def test_multiple_products_update_count_correctly(self):
        cat = Category("Laptops", "All laptops")
        p1 = Product("Laptop 1", "Desc", 1000.0, 1)
        p2 = Product("Laptop 2", "Desc", 1200.0, 1)
        
        cat.add_product(p1)
        cat.add_product(p2)
        
        assert Category.product_count == 2
        assert len(cat.products) == 2
