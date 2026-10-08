import random
from product import Product
from product_manager import ProductManager
from cart import Cart

manager = ProductManager()

manager.add_product(Product("Laptop", 800, 5))
manager.add_product(Product("Mouse", 25, 10))
manager.add_product(Product("Keyboard", 50, 7))

cart = Cart()

selected_products = random.sample(manager.products, 3)

for product in selected_products:
    cart.add_product(product)

print("Cart contents:")
cart.display_cart()

print(f"Total cart value: {cart.total_cart_value()}")