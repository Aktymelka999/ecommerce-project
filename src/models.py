from typing import List

class Product:
    __slots__ = ("name", "description", "price", "quantity")  # Опционально: экономия памяти и защита от опечаток
    
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    # Классовые переменные (общие для всех категорий)
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description
        
        # Инициализация экземпляра: каждый объект получает СВОЙ пустой список
        self.products: List[Product] = []
        
        # Увеличиваем счётчик категорий
        Category.category_count += 1

    def add_product(self, product: Product) -> None:
        """Добавляет товар и обновляет глобальный счётчик."""
        self.products.append(product)
        Category.product_count += 1
        