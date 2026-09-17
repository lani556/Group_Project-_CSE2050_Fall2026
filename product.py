#Product Module

class Product:
    """Product class that creates product objects. You can return the product id, name, and price"""
    def __init__(self, product_id, name, price):
        """Initializes a product object with a Product ID, name, and price"""
        self.product_id = product_id
        self.name = name
        self.price = price

    def get_id(self):
        """Returns the product id as a string"""
        return f"{self.product_id}"

    def get_name(self):
        """Returns the product name as a string"""
        return f"{self.name}"

    def get_price(self):
        """Returns the price of the product as a float"""
        return self.price



