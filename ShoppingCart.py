import Product 

class ShoppingCart

    def __init__(self):
        self.cart = []
    

    def add_product(Product):
        self.cart.append(Product)


    def remove_product(self, product_id):
        oldcart = self.cart
        self.cart.remove(product_id)

        if len(oldcart) < len(self.cart):
            return True
        else:
            return False


    def get_items(self):
        return self.cart

    def calculate_total(self):
        sum_of_prices = 0.00

        for item in self.cart:
            sum_of_prices += item.get_price()
        
        return sum_of_prices 


    def is_empty(self):
        if len(self.cart) == 0:
            return True
        return False


ella = ShoppingCart()
ella.calculate_total()


