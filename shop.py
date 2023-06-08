class Shop:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_products(self):
        print(f"Shop Name: {self.name}")
        print("Product List:")
        for product in self.products:
            product.display_info()
            print("---------")
