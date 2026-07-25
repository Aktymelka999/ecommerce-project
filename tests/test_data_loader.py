import pytest
import os
from src.data_loader import load_products_from_json
from src.models import Product


class TestDataLoader:
    def test_load_valid_json(self, tmp_path):
        # Создаём временный JSON-файл
        json_file = tmp_path / "products.json"
        json_file.write_text(
            """
            [
              {"name": "Mouse", "description": "Wireless", "price": 29.99, "quantity": 50},
              {"name": "Keyboard", "description": "Mechanical", "price": 79.99, "quantity": 30}
            ]
            """
        )

        products = load_products_from_json(str(json_file))

        assert len(products) == 2
        assert isinstance(products[0], Product)
        assert products[0].name == "Mouse"
        assert products[1].name == "Keyboard"

    def test_missing_field_raises_error(self, tmp_path):
        json_file = tmp_path / "bad_products.json"
        # Убрали поле quantity
        json_file.write_text(
            """
            [
              {"name": "Bad Item", "description": "No quantity", "price": 10.0}
            ]
            """
        )

        with pytest.raises(ValueError, match="отсутствует обязательное поле: quantity"):
            load_products_from_json(str(json_file))

    def test_invalid_type_raises_error(self, tmp_path):
        json_file = tmp_path / "bad_types.json"
        # quantity — строка вместо числа
        json_file.write_text(
            """
            [
              {"name": "Bad Type", "description": "Wrong type", "price": 10.0, "quantity": "many"}
            ]
            """
        )

        with pytest.raises(ValueError, match="должно быть целым числом"):
            load_products_from_json(str(json_file))