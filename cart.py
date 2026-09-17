
from product import Product 

class ShoppingCart:
    """ This class creatings Shopping Carts for customers, adds and removes products, calculates total of cart
    and checks if the list is empty"""
    def __init__(self):
        """Constructor intializes an empty cart as a list"""
        self.items = []
    
    def add_product(self, Product):
        """Adds new products to the shopping cart."""
        self.items.append(Product)

    def remove_product(self, product_id):
        """Removes products from the shopping cart by Product Id"""
        oldcart = len(self.items)
        for item in self.items :
            if item.get_id() == product_id:
                self.items.remove(item)
                break
        if oldcart> len(self.items):
            return True
        else:
            return False


    def get_items(self):
        """Returns the cart list"""
        return self.items

    def calculate_total(self):
        """Returns the total value of the cart as a float"""
        sum_of_prices = 0.00

        for item in self.items:
            sum_of_prices += item.get_price()
        
        return sum_of_prices 


    def is_empty(self):
        """Checks if the cart is empty"""
        if len(self.items) == 0:
            return True
        return False

#Test Cases for each of the functions

ella = ShoppingCart()
print(ella.calculate_total())
print(ella.is_empty())

apple = Product("4050", "Apples(1lbs)", 2.99)
pasta = Product("1100", "Rigatoni ", 0.99)
vitamin_water = Product("9005", "Lime Gatorade", 1.09)
ella.add_product(apple)
ella.add_product(pasta)
ella.add_product(vitamin_water)
print(ella.get_items())
print(ella.is_empty())
print(ella.calculate_total())
print(ella.remove_product(apple.get_id()))
print(ella.get_items()) 
