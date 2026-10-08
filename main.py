import random
from product import Product
from product_manager import ProductManager
from cart import Cart

manager = ProductManager()

manager.add_product(Product("Tablet", 500, 3))
manager.add_product(Product("Headphones", 80, 6))
manager.add_product(Product("Monitor", 200, 4))

cart = Cart()

selected_products = random.sample(manager.products, 3)

for product in selected_products:
    cart.add_product(product)

print("Cart contents:")
cart.display_cart()

print(f"Total cart value: {cart.total_cart_value()}")