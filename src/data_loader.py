import json
from typing import List
from .models import Product, Category


def load_products_from_json(file_path: str) -> List[Category]:
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Инициализируем результат пустым списком
    categories: List[Category] = []
    
    # .get(key, default) — если ключа нет, вернёт пустой список, а не None
    all_categories_data = data.get("categories", )
    
    for cat_data in all_categories_data:
        category = Category(cat_data["name"], cat_data["description"])
        
        # Защита: если у категории нет товаров, products_data станет пустым списком
        products_data = cat_data.get("products", )
        
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