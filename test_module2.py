import unittest
from order import Order
from order_queue import OrderQueue
from stack import Stack
from store import Store
from customer import Customer
from product import Product

class TestStore(unittest.TestCase):

    def test_checkout(self):
        store = Store()
        customer1 = Customer("C001", "Customer 1")
        customer2 = Customer("C002", "Customer 2")
        product1 = Product("P001", "Product 1", 10.99)
        store.add_customer(customer1)
        store.add_customer(customer2)
        store.add_product(product1)
        customer1.get_cart().add_product(product1)

        # existing customer
        order1 = store.checkout("C001")
        self.assertIsNotNone(order1)
        self.assertEqual(store.find_order(order1.get_id()), order1)
        self.assertEqual(order1.get_status(), "PENDING")
        self.assertEqual(store.order_counter, 1)
        self.assertEqual(len(store.orders), 1)
        self.assertEqual(store.order_queue.queue[0], order1)
        # existing customer, empty cart
        order2 = store.checkout("C002")  
        self.assertIsNone(order2)
        # non-existing customer
        order3 = store.checkout("C003")  
        self.assertIsNone(order3)

    def test_processing(self):
        store = Store()
        customer1 = Customer("C001", "Customer 1")
        product1 = Product("P001", "Product 1", 10.99)
        store.add_customer(customer1)  
        store.add_product(product1)
        customer1.get_cart().add_product(product1)

        self.assertEqual(store.process_next_order(), None)
        
        order1 = store.checkout("C001")
        self.assertEqual(store.process_next_order(), order1)
        self.assertEqual(order1.get_status(), "PROCESSING")
        self.assertEqual(len(store.processed_orders.items), 1)


    def test_order_history(self):
        store = Store()
        customer1 = Customer("C001", "Customer 1")
        product1 = Product("P001", "Product 1", 10.99)
        store.add_customer(customer1)  
        store.add_product(product1)
        customer1.get_cart().add_product(product1)
        order1 = store.checkout("C001")
        self.assertEqual(store.get_order_history(), [])
        
        store.process_next_order()
        self.assertEqual(store.get_order_history(), [order1])

    def test_add_product(self):
        store = Store()
        product1 = Product("P001", "Product 1", 10.99)

        # new product
        self.assertTrue(store.add_product(product1))
        # duplicate product
        self.assertFalse(store.add_product(product1))

    def test_find_product(self):
        store = Store()
        product1 = Product("P001", "Product 1", 10.99)
        store.add_product(product1)

        # existing product
        self.assertEqual(store.find_product("P001"), product1)
        # non-existing product
        self.assertIsNone(store.find_product("P002"))

    def test_add_customer(self):
        store = Store()
        customer1 = Customer("C001", "Customer 1")

        # new customer
        self.assertTrue(store.add_customer(customer1))
        # duplicate customer
        self.assertFalse(store.add_customer(customer1))

    def test_find_customer(self):
        store = Store()
        customer1 = Customer("C001", "Customer 1")
        store.add_customer(customer1)
        # existing customer
        self.assertEqual(store.find_customer("C001"), customer1)
        # non-existing customer
        self.assertIsNone(store.find_customer("C002"))

class TestOrder(unittest.TestCase):
    def test_order_creation(self):
        pass

    def test_total(self):
        pass

class TestLinkedList(unittest.TestCase):
    pass

class TestStack(unittest.TestCase):
    def test_LIFO_order(self):
        pass

    def test_peek(self):
        pass

    def test_pop(self):
        pass

class TestOrderQueue(unittest.TestCase):
    def test_FIFO_order(self):
        pass
    def test_peek(self):
        pass

    def test_dequeue(self):
        pass
    



unittest.main()
