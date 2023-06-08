# Shop Management System

## Introduction
This is a simple Shop Management System implemented in Python. It allows you to manage products in a shop, add new products, and display the list of available products.

## Installation
1. Clone the repository: `git clone https://github.com/ChlorophyTeio/Simple-Shop-Management.git`
2. Navigate to the project directory: `cd Simple-Shop-Management`

## Usage
1. Open the `main.py` file in a Python IDE or text editor.
2. Run the program to see the list of products in the shop.

## File Structure
- `main.py`: The entry point of the program. It creates shop and product objects and demonstrates the functionality of the system.
- `shop.py`: Contains the `Shop` class, which represents a shop and manages the products.
- `product.py`: Contains the `Product` class, which represents a product and its properties.

## Class Details
### Shop
The `Shop` class represents a shop and has the following methods:
- `__init__(self, name)`: Initializes the shop with a given name.
- `add_product(self, product)`: Adds a product to the shop's product list.
- `display_products(self)`: Displays the list of products in the shop.

### Product
The `Product` class represents a product and has the following methods:
- `__init__(self, name, price, quantity)`: Initializes a product with a given name, price, and quantity.
- `display_info(self)`: Displays the information of the product.

## Contributions
Contributions to this project are welcome. If you find any issues or want to add new features, feel free to submit a pull request.

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
