# Customer Module

from cart import ShoppingCart

class Customer:
    def __init__(self, customer_id, name):
        """Initialize an instance of a customer with a customer id, name, and an empty shoping cart"""
        self.customer_id = customer_id
        self.name = name
        self.cart = ShoppingCart() #Creates an empty shopping cart

    def get_id(self):
        """Returns customer id of customer"""
        return f"{self.customer_id}"

    def get_name(self):
        """Returns the name of the customer"""
        return f"{self.name}" 

    def get_cart(self):
        """Returns the list of products in the customer's cart."""
        return self.cart

