import json
from typing import List

from .models import Category, Product


def load_products_from_json(file_path: str) -> List[Category]:
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    categories: List[Category] = []
    all_categories_data = data.get("categories", [])

    for cat_data in all_categories_data:
        category = Category(cat_data["name"], cat_data["description"])
        products_data = cat_data.get("products", [])

        for prod_data in products_data:
            product = Product(
                name=prod_data["name"],
                description=prod_data["description"],
                price=float(prod_data["price"]),
                quantity=int(prod_data["quantity"]),
            )
            category.add_product(product)

        categories.append(category)

    return categories
