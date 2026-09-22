import json

import pytest

from src.data_loader import load_products_from_json


class TestDataLoader:
    @pytest.fixture
    def valid_json_path(self, tmp_path):
        data = {
            "categories": [
                {
                    "name": "Electronics",
                    "description": "Gadgets",
                    "products": [
                        {
                            "name": "Mouse",
                            "description": "Wireless",
                            "price": 29.99,
                            "quantity": 50,
                        },
                        {
                            "name": "Keyboard",
                            "description": "Mechanical",
                            "price": 79.99,
                            "quantity": 30,
                        },
                    ],
                },
                {
                    "name": "Books",
                    "description": "Reading",
                    "products": [
                        {
                            "name": "Python Book",
                            "description": "Learn Python",
                            "price": 15.99,
                            "quantity": 100,
                        },
                    ],
                },
            ],
        }
        file_path = tmp_path / "products.json"
        file_path.write_text(json.dumps(data))
        return file_path


def test_load_valid_json_returns_categories(valid_json_path):
    categories = load_products_from_json(str(valid_json_path))

    assert len(categories) == 2
    assert isinstance(categories, list)

    first_cat = categories[0]
    second_cat = categories[1]

    assert isinstance(
        first_cat, type(categories[0])
    )  
    assert isinstance(second_cat, type(categories[1]))

    assert first_cat.name == "Electronics"
    assert second_cat.name == "Books"


    assert len(first_cat._Category__products) == 2
    
