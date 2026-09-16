from customer import Customer
from product import Product



class Store:


    def __init__(self):
        self.products = []
        self.customers = []

    def add_product(self, product):
        for item in self.products:
            if item.get_id() == product.get_id():
                return False

        self.products.append(product)
        return True

    
    def find_product(self, product_id):
        for item in self.products:
            if item.get_id() == product_id:
                return item

        return None

    def add_customer(self, customer):
        for c in self.customers:
            if c.get_id() == customer.get_id():
                return False

        self.customers.append(customer)
        return True

    def find_customer(self, customer_id):
        for c in self.customers:
            if c.get_id() == customer_id:
                return c
        return None

        


store = Store()
mouse = Product("P100", "Wireless Mouse", 29.99)
keyboard = Product("P101", "Keyboard", 59.99)
store.add_product(mouse)
store.add_product(keyboard)
customer = Customer("C100", "Alex")
store.add_customer(customer)
cart = customer.get_cart()
cart.add_product(mouse)
cart.add_product(keyboard)
print(cart.calculate_total())



