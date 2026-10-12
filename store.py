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

            order_id = f"O{self.order_counter + 1}"  # Generate a new order ID (?)
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
        ord_hist = []
        for i in self.orders[::-1]:
            if i.status == "PROCESSING":
                ord_hist.append(i)
        return ord_hist


#Testing
print("this is where testing begins")
# Create the store
store = Store()
customer1 = Customer("C001", "Customer 1")
product1 = Product("P001", "Product 1", 10.99)
store.add_customer(customer1)  
store.add_product(product1)
customer1.get_cart().add_product(product1)
order1 = store.checkout("C001")
print(order1)
print(store.get_order_history())

"""store = Store()
mouse = Product("P100", "Wireless Mouse", 29.99)
keyboard = Product("P101", "Keyboard", 59.99)
headphones = Product("P102", "Headphones", 39.99)
# Add products to the store
print(store.add_product(mouse)) # Output: True
print(store.add_product(keyboard)) # Output: True
print(store.add_product(headphones)) # Output: True
# Create two customers
alex = Customer("C100", "Alex")
sam = Customer("C101", "Sam")
# Add customers to the store
print(store.add_customer(alex)) # Output: True
print(store.add_customer(sam)) # Output: True
# Alex creates an order
alex_cart = alex.get_cart()
alex_cart.add_product(mouse)
alex_cart.add_product(keyboard)
print(alex_cart.calculate_total()) # Output: 89.98
print(alex_cart.is_empty()) # Output: False
alex_order = store.checkout("C100")
print(alex_order.get_id()) # Output: O1
print(alex_order.get_customer().get_name()) # Output: Alex
print(alex_order.calculate_total()) # Output: 89.98
print(alex_order.get_status()) # Output: PENDING
print(alex_cart.is_empty()) # Output: True
# Sam creates an order
sam_cart = sam.get_cart()
sam_cart.add_product(headphones)
print(sam_cart.calculate_total()) # Output: 39.99
sam_order = store.checkout("C101")
print(sam_order.get_id()) # Output: O2
print(sam_order.get_customer().get_name()) # Output: Sam
print(sam_order.get_status()) # Output: PENDING
# Process the orders
first_order = store.process_next_order()
print(first_order.get_id()) # Output: O1
print(first_order.get_status())