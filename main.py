import tkinter as tk
from shop import Shop
from product import Product


def display_products():
    products = shop.products
    for product in products:
        label = tk.Label(root, text=f"{product.name} - Price: {product.price} - Quantity: {product.quantity}")
        label.pack()
    display_button.config(state=tk.DISABLED)  # 禁用按钮


root = tk.Tk()
root.title("TokaiSeouyoo's Shop")

shop = Shop("TokaiSeouyoo's shop")

product1 = Product("Apple", 5.0, 10)
product2 = Product("Banana", 3.0, 15)
product3 = Product("Orange", 4.0, 8)

shop.add_product(product1)
shop.add_product(product2)
shop.add_product(product3)

display_button = tk.Button(root, text="Display Products", command=display_products)
display_button.pack()

root.mainloop()
