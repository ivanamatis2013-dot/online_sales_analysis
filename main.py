from product import Product
from product_manager import ProductManager

manager = ProductManager()

manager.add_product(Product("Laptop", 800, 5))
manager.add_product(Product("Mouse", 25, 10))
manager.add_product(Product("Keyboard", 50, 7))

print("Available products:")
manager.display_products()

print(f"Total inventory value: {manager.total_inventory_value()}")