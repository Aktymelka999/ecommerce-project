import pytest
import json
from pathlib import Path
from src.data_loader import load_products_from_json
from src.models import Category, Product

class TestDataLoader:
    @pytest.fixture
    def valid_json_path(self, tmp_path):
        data = {
            "categories": [
                {
                    "name": "Electronics",
                    "description": "Gadgets",
                    "products": [
                        {"name": "Mouse", "description": "Wireless", "price": 29.99, "quantity": 50},
                        {"name": "Keyboard", "description": "Mechanical", "price": 79.99, "quantity": 30}
                    ]
                },
                {
                    "name": "Books",
                    "description": "Reading",
                    "products": [
                        {"name": "Python Book", "description": "Learn Python", "price": 15.99, "quantity": 100}
                    ]
                }
            ]
        }
        file_path = tmp_path / "products.json"
        file_path.write_text(json.dumps(data))
        return file_path
    def test_load_valid_json_returns_categories(self, valid_json_path):
        categories = load_products_from_json(str(valid_json_path))
        
        # Проверяем, что вернулись 2 категории
        assert len(categories) == 2
        
        # Проверяем, что categories — это список
        assert isinstance(categories, list)
        
        # Проверяем типы элементов внутри списка
        first_cat = categories[0]
        second_cat = categories[1]
        
        assert isinstance(first_cat, Category)
        assert isinstance(second_cat, Category)
        
        # Проверяем имена, чтобы убедиться, что данные загрузились верно
        assert first_cat.name == "Electronics"
        assert second_cat.name == "Books"
        
        # Проверяем количество товаров в первой категории
        assert len(first_cat.products) == 2
