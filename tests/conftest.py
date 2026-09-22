import json
import tempfile

import pytest


@pytest.fixture
def valid_json_path():
    data = {
        "categories": [
            {
                "name": "Electronics",
                "description": "All electronics",
                "products": [
                    {
                        "name": "Mouse",
                        "description": "Wireless mouse",
                        "price": 29.99,
                        "quantity": 50,
                    },
                    {
                        "name": "Keyboard",
                        "description": "Mechanical keyboard",
                        "price": 79.99,
                        "quantity": 30,
                    },
                ],
            },
            {
                "name": "Books",
                "description": "All books",
                "products": [],
            },
        ],
    }

    with tempfile.NamedTemporaryFile(
        mode="w",
        suffix=".json",
        delete=False,
        encoding="utf-8",
    ) as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        path = f.name

    yield path
