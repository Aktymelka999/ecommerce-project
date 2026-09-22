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


class Category:
    product_count: int = 0

    def __init__(
        self,
        name: str,
        description: str,
        products: Optional[List[Product]] = None,
    ) -> None:
        self.name = name
        self.description = description
        self.__products: List[Product] = products if products is not None else []

    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        result = ""
        for p in self.__products:
            result += f"{p.name}, {p.price} руб. Остаток: {p.stock} шт.\n"
        return result

    @classmethod
    def new_product(cls, product_data: Dict[str, Any]) -> Product:
        return Product(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            stock=product_data["stock"],
        )
