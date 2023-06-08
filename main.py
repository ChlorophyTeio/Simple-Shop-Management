from shop import Shop
from product import Product

# Create shop objects
shop = Shop("TokaiSeouyoo's shop")

# Create commodity objects
product1 = Product("Apple", 5.0, 10)
product2 = Product("Banana", 3.0, 15)
product3 = Product("Orange", 4.0, 8)

# Add items to the shop
shop.add_product(product1)
shop.add_product(product2)
shop.add_product(product3)

# Show the list of products in the shop
shop.display_products()
