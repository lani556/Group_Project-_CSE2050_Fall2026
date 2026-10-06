from order import Order
from stack import Stack
from order_queue import OrderQueue
from customer import Customer
from product import Product



class Store:
    """A store class with customers and products. You can add and find both customers and products"""

    def __init__(self):
        """Initializes a store class with an empty list of products and customers"""
        self.products = []
        self.customers = []
        self.orders = []
        self.processed_orders = Stack()
        self.order_queue = OrderQueue()  # Initialize an empty order queue
        self.order_counter = len(self.orders)  # Initialize order counter based on existing orders


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

    def find_order(self, order_id):
        """Finds an order in the store by its order id"""
        for order in self.orders:
            if order.get_id() == order_id:
                return order
        return None

    def get_orders(self):
        """Returns the list of orders in the store"""
        return self.orders

    def checkout(self, customer_id):
        customer = self.find_customer(customer_id)
        if customer is None:
            return None  # Customer not found
        else:
            cart = customer.get_cart()
            if cart.is_empty():
                return None  # Cart is empty

            ##Need to implement this with OrderQueue
            order_id = f"O{self.order_counter + 1:03d}"  # Generate a new order ID (?)
            new_order = Order(order_id, customer, cart.get_items())
            self.orders.append(new_order) 
            self.order_queue.enqueue(new_order)  
            self.order_counter += 1  
            cart.clear()
            return new_order

    def process_next_order(self):
        """Processes the next order in the queue"""
        if self.order_queue.is_empty():
            return None  # No orders to process
        else:
            order = self.order_queue.dequeue() 
            order.set_status("PROCESSING")  
            self.processed_orders.push(order)
            return order

    def get_order_history(self):
        """Returns a list of all processed orders"""
        return self.processed_orders.items

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



