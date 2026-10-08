from product import Product
from product_manager import ProductManager

manager = ProductManager()

manager.add_product(Product("Tablet", 500, 3))
manager.add_product(Product("Headphones", 80, 6))
manager.add_product(Product("Monitor", 200, 4))