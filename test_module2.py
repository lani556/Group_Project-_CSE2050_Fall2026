import unittest
from order import Order
from order_queue import OrderQueue
from stack import Stack
from store import Store
from customer import Customer
from product import Product
from linkedList import linkedList

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

    #These I don't think are necessary but doesn't hurt our grade to keep them.
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
        order1 = Order("O001", "C001", ["Pepsi", "Coke"])
        self.assertEqual(order1.get_id(), "O001")
        self.assertEqual(order1.get_customer(), "C001")
        self.assertEqual(order1.get_status(), "PENDING")
        self.assertEqual(order1.get_items(), ["Pepsi", "Coke"])

    def test_total(self):
        product1 = Product("P001", "Product 1", 10.99)
        product2 = Product("P002", "Product 2", 12.99)
        order1 = Order("O001", "C001", [product1, product2])

        self.assertEqual(order1.calculate_total(), 10.99+12.99)

class TestLinkedList(unittest.TestCase):

    def test_add_first(self):
        ll1 = linkedList()
        l = ["apples","bananas", "juice"]
        count = 0
        for item in l:
            ll1.add_first(item)
            count += 1
            self.assertEqual(ll1.get_first(), item)
            self.assertEqual(ll1.size(), count)

    def test_add_last(self):
        ll2 = linkedList()
        l = ["apples","bananas", "juice"]
        count = 0
        last = l[0]
        for item in l:
            ll2.add_last(item)
            count += 1
            self.assertEqual(ll2.get_first(), last)
            self.assertEqual(ll2.size(), count)
            last = item

        



    def test_remove_first(self):
        pass
    def test_isempty(self):
        pass
    

class TestQrderQueue(unittest.TestCase):
    def test_FIFO_order(self):
        queue1 = OrderQueue()
        self.assertIsNone(queue1.dequeue())
        queue1.enqueue("how")
        queue1.enqueue("are")
        queue1.enqueue("you")
        self.assertEqual(queue1.queue[0], "how")
        self.assertEqual(queue1.queue[-1], "you")

        
    def test_peek(self):
        queue1 = OrderQueue()
        self.assertIsNone(queue1.peek())
        queue1.enqueue("how")
        queue1.enqueue("are")
        queue1.enqueue("you")
        self.assertEqual(queue1.peek(), "how")

    def test_dequeue(self):
        queue1 = OrderQueue()
        self.assertIsNone(queue1.dequeue())
        queue1.enqueue("how")
        queue1.enqueue("are")
        queue1.enqueue("you")

        self.assertEqual(queue1.dequeue(), "how")
        self.assertEqual(queue1.queue, ["are", "you"])

class TestStack(unittest.TestCase):
    def test_LIFO_order(self):
        pass
    def test_peek(self):
        pass

    def test_pop(self):
        pass
    



unittest.main()
