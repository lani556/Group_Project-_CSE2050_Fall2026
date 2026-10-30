import unittest
from store import Store
from product import Product

class TestStore(unittest.TestCase):


    def test_selection(self):
        pass
    def test_binary_search(self):
        pass
    def test_fewest_coins(self):
        pass

    def test_recursive_total(self):
        store = Store()

        self.assertEqual(store.recursive_catalog_total(), 0)
        mouse = Product("P300", "Mouse", 29.99)
        keyboard = Product("P100", "Keyboard", 59.99)
        headphones = Product("P200", "Headphones", 39.99)
        store.add_product(mouse)
        store.add_product(keyboard)
        store.add_product(headphones)
        self.assertEqual(store.recursive_catalog_total(), 129.97)

    def test_bubble_sort_al_sorted(self):
        store = Store()
        mouse = Product("P300", "Mouse", 29.99)
        keyboard = Product("P100", "Keyboard", 59.99)
        headphones = Product("P200", "Headphones", 39.99)
        store.add_product(keyboard)
        store.add_product(headphones)
        store.add_product(mouse)
        list = [p.get_id() for p in store.products]
        store.bubble_sort_products()
        new_list = [p.get_id() for p in store.products]
        self.assertEqual(list, new_list)

    def test_bubble_sort_rev_order(self):
        store = Store()
        mouse = Product("P300", "Mouse", 29.99)
        keyboard = Product("P100", "Keyboard", 59.99)
        headphones = Product("P200", "Headphones", 39.99)
        store.add_product(mouse)
        store.add_product(headphones)
        store.add_product(keyboard)
        rev_order = [p.get_id() for p in store.products]
        store.bubble_sort_products()
        sorted = [p.get_id() for p in store.products]
        self.assertEqual(sorted[::-1], rev_order)
    
    def test_insertion_sort_al_sorted(self):
        store = Store()
        mouse = Product("P300", "Mouse", 29.99)
        keyboard = Product("P100", "Keyboard", 59.99)
        headphones = Product("P200", "Headphones", 39.99)
        store.add_product(keyboard)
        store.add_product(headphones)
        store.add_product(mouse)
        list = [p.get_id() for p in store.products]
        store.insertion_sort_products()
        new_list = [p.get_id() for p in store.products]
        self.assertEqual(list, new_list)

    def test_insertion_sort_rev_order(self):
        store = Store()
        mouse = Product("P300", "Mouse", 29.99)
        keyboard = Product("P100", "Keyboard", 59.99)
        headphones = Product("P200", "Headphones", 39.99)
        store.add_product(mouse)
        store.add_product(headphones)
        store.add_product(keyboard)
        rev_order = [p.get_id() for p in store.products]
        store.insertion_sort_products()
        sorted = [p.get_id() for p in store.products]
        self.assertEqual(sorted[::-1], rev_order)

if __name__== "__main__":
    unittest.main()