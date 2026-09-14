# Customer Module

from cart import Cart

class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
        self.cart = []

    def get_id(self):
        return f"{self.customer_id}"

    def get_name(self):
        return f"{self.name}" 

    def get_cart(self):
        return self.cart

