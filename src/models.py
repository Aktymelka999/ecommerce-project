from typing import Any, Dict, List, Optional


class Product:
    __slots__ = ("name", "description", "__price", "stock")

    def __init__(self, name: str, description: str, price: float, stock: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.stock = stock

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < self.__price:
            response = (
                input(
                    f"Цена понижается с {self.__price} до {new_price}. Подтвердить (y/n)? "
                )
                .strip()
                .lower()
            )
            if response != "y":
                print("Изменение цены отменено.")
                return

        self.__price = new_price

    def __str__(self) -> str:
        return f"{self.name}, {self.__price:.2f} руб. Остаток: {self.stock} шт."

    def __add__(self, other: "Product") -> float:
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты Product")
        return (self.__price * self.stock) + (other.__price * other.stock)

    @classmethod
    def new_product(
        cls,
        data: Dict[str, Any],
        products: Optional[List["Product"]] = None,
    ) -> "Product":
        new = cls(
            name=data["name"],
            description=data["description"],
            price=float(data["price"]),
            stock=int(data["stock"]),
        )

        if products is not None:
            for p in products:
                if p.name == new.name:
                    p.stock += new.stock
                    p.price = new.price
                    return p

        return new


class ProductIterator:
    """Итератор для перебора товаров категории."""

    def __init__(self, category: "Category") -> None:
        self._products = list(category.products)
        self._index = 0

    def __iter__(self) -> "ProductIterator":
        return self

    def __next__(self) -> Product:
        if self._index >= len(self._products):
            raise StopIteration
        item = self._products[self._index]
        self._index += 1
        return item


class Category:
    product_count: int = 0
    category_count: int = 0

    def __init__(
        self,
        name: str,
        description: str,
        products: Optional[List[Product]] = None,
    ) -> None:
        self.name = name
        self.description = description
        self.__products: List[Product] = products if products is not None else []

        Category.category_count += 1

    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> List[Product]:
        return list(self.__products)

    def __str__(self) -> str:
        total_quantity = sum(p.stock for p in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    @classmethod
    def new_product(cls, product_data: Dict[str, Any]) -> Product:
        return Product(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            stock=product_data["stock"],
        )
