from customer import Customer
from product import Product



class Store:
    """A store class with customers and products. You can add and find both customers and products"""

    def __init__(self):
        """Initializes a store class with an empty list of products and customers"""
        self.products = []
        self.customers = []

    def add_product(self, product):
        """Add products to the store's product lists"""
        for item in self.products:
            if item.get_id() == product.get_id(): #If an item in the store has the same product id as the product you want to add, it will not add the item
                return False

        self.products.append(product)
        return True

    
    def find_product(self, product_id):
        """Returns the product by the product id"""
        for item in self.products:
            if item.get_id() == product_id: #Will only return product if the product id is in the store
                return item

        return None

    def add_customer(self, customer):
        """Adds a new customer to the Store's customer list"""
        for c in self.customers:
            if c.get_id() == customer.get_id():
                return False

        self.customers.append(customer)
        return True

    def find_customer(self, customer_id):
        """Finds a customer in the store by their customer id"""
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



