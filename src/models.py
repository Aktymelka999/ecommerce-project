from typing import List, Optional


class Product:
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
    ) -> None:
        self.name: str = name
        self.description: str = description
        self.price: float = price
        self.quantity: int = quantity


class Category:
    # Атрибуты класса: общее количество категорий и товаров
    category_count: int = 0
    product_count: int = 0

    def __init__(
        self,
        name: str,
        description: str,
        products: Optional[List[Product]] = None,
    ) -> None:
        self.name: str = name
        self.description: str = description
        self.products: List[Product] = products if products is not None else []

        # Увеличиваем счётчики при создании объекта
        Category.category_count += 1
        Category.product_count += len(self.products)

    def add_product(self, product: Product) -> None:
        """Добавляет товар в категорию и обновляет счётчик."""
        self.products.append(product)
        Category.product_count += 1