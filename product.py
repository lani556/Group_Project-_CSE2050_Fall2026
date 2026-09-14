#Product Module

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def get_id(self):
        return f"{self.product_id}"

    def get_name(self):
        return f"{self.name}"

    def get_price(self):
        return f"{self.price}"

pr1 = Product(1, "Product 1", 10.99)

print(pr1.get_id())
print(pr1.get_name())
print(pr1.get_price())