from src.models import Product, Category

def main():
    
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)

    
    category_phones = Category("Смартфоны", "Все смартфоны", [product1, product2, product3])
    category_tvs = Category("Телевизоры", "Все телевизоры", [product4])

    
    product5 = Product("Pixel 8", "128GB, Obsidian", 90000.0, 3)
    category_phones.add_product(product5)

    
    print("=== Результаты работы ===")
    print(f"Количество категорий: {Category.category_count}")
    print(f"Общее количество товаров: {Category.product_count}")
    
    print(f"\nВ категории '{category_phones.name}' товаров: {len(category_phones.products)}")
    print(f"В категории '{category_tvs.name}' товаров: {len(category_tvs.products)}")

if __name__ == "__main__":
    main()