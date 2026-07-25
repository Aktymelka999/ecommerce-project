import json
from typing import List
from .models import Product


def load_products_from_json(file_path: str) -> List[Product]:
    """Загружает товары из JSON-файла с валидацией полей."""
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError("JSON должен содержать список товаров.")

    products = []
    for i, item in enumerate(data):
        if not isinstance(item, dict):
            raise ValueError(f"Элемент №{i} не является объектом (dict).")

        required_fields = ["name", "description", "price", "quantity"]
        for field in required_fields:
            if field not in item:
                raise ValueError(
                    f"В элементе №{i} отсутствует обязательное поле: {field}"
                )

        if not isinstance(item["name"], str) or not item["name"].strip():
            raise ValueError(
                "Поле 'name' в элементе №" f"{i} должно быть непустой строкой."
            )

        if not isinstance(item["description"], str):
            raise ValueError(
                f"Поле 'description' в элементе №{i} " "должно быть строкой."
            )

        if not isinstance(item["price"], (int, float)) or item["price"] < 0:
            raise ValueError(
                f"Поле 'price' в элементе №{i} " "должно быть числом >= 0."
            )

        if not isinstance(item["quantity"], int) or item["quantity"] < 0:
            raise ValueError(
                f"Поле 'quantity' в элементе №{i} " "должно быть целым числом >= 0."
            )

        product = Product(
            name=item["name"],
            description=item["description"],
            price=float(item["price"]),
            quantity=int(item["quantity"]),
        )
        products.append(product)

    return products
