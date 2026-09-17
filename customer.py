# Customer Module

from cart import ShoppingCart
from product import Product

class Customer:
    """A customer class where each customer has a shopping cart. You can return the customer id, name, and cart"""
    def __init__(self, customer_id, name):
        """Initialize an instance of a customer with a customer id, name, and an empty shoping cart"""
        self.customer_id = customer_id
        self.name = name
        self.cart = ShoppingCart() #Creates a ShoppingCart object with an empty cart as a list

    def get_id(self):
        """Returns customer id of customer"""
        return f"{self.customer_id}"

    def get_name(self):
        """Returns the name of the customer"""
        return f"{self.name}" 

    def get_cart(self):
        """Returns the list of products in the customer's cart."""
        return self.cart

"""Testing"""

# c1 = Customer("c100", "Sam")
# c2 = Customer("c101", "Lani")

# pr1 = Product("P100", "Dunkin", 6.99)
# pr2 = Product("P101","Chair", 25.99)

# assert c1.get_name() == "Sam", "Wrong Name"
# assert c2.get_name() == "Lani", "Wrong Name"

# assert c1.get_id() == "c100", "Wrong id"
# assert c2.get_id() == "c101", "Wrong id"

# print(c1.get_cart())
# print(c2.get_cart())

# cart1 = c1.get_cart()
# c1.cart.add_product(pr1)
# cart2 = c1.get_cart()

# assert c1.cart.is_empty() == False
# assert c2.cart.is_empty() == True

# assert cart1 == cart2, "Different carts"


