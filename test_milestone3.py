import unittest
from store import Store
from product import Product
import algorithms

class TestStore(unittest.TestCase):


    def test_selection_sort(self):
        store = Store()

        mouse = Product("P300", "Mouse", 29.99)
        keyboard = Product("P100", "Keyboard", 59.99)
        headphones = Product("P200", "Headphones", 39.99)
        store.add_product(mouse)
        store.add_product(keyboard)
        store.add_product(headphones)
        store.selection_sort_products()

        select = [p.get_id() for p in store.products]
        self.assertEqual(select, ["P100", "P200", "P300"])
        
        store.selection_sort_products()
        self.assertEqual(select,["P100", "P200", "P300"])

    def test_selection_sort_reversed(self):
        store = Store()

        mouse = Product("P300", "Mouse", 29.99)
        headphones = Product("P200", "Headphones", 39.99)
        keyboard = Product("P100", "Keyboard", 59.99)
        store.add_product(mouse)
        store.add_product(headphones)
        store.add_product(keyboard)
        store.selection_sort_products()

        select = [p.get_id() for p in store.products]
        self.assertEqual(select, ["P100", "P200", "P300"])
 
    def test_binary_search(self):
        store = Store()

        mouse = Product("P300", "Mouse", 29.99)
        keyboard = Product("P100", "Keyboard", 59.99)
        headphones = Product("P200", "Headphones", 39.99)

        store.add_product(keyboard)
        store.add_product(headphones)
        store.add_product(mouse)

        self.assertEqual(algorithms.binary_search(store.products, "P100"), 0)
        self.assertEqual(algorithms.binary_search(store.products, "P200"), 1)
        self.assertEqual(algorithms.binary_search(store.products, "P400"), -1)  
    
    def test_binary_search_product(self):
        store = Store()

        mouse = Product("P300", "Mouse", 29.99)
        keyboard = Product("P100", "Keyboard", 59.99)
        headphones = Product("P200", "Headphones", 39.99)

        store.add_product(keyboard)
        store.add_product(headphones)
        store.add_product(mouse)

        self.assertEqual(store.binary_search_product("P100"), keyboard)
        self.assertEqual(store.binary_search_product("P200"), headphones)
        self.assertEqual(store.binary_search_product("P400"), None)

    def test_fewest_coins(self):
        store = Store()
        coins = [1,5,10]
        mouse = Product("P300", "Mouse", 0)
        keyboard = Product("P100", "Keyboard", 20)
        headphones = Product("P200", "Headphones", -1)
        store.add_product(mouse)
        store.add_product(keyboard)
        store.add_product(headphones)

        self.assertEqual(store.calculate_change(coins,mouse.get_price()), 0)
        self.assertEqual(store.calculate_change(coins,keyboard.get_price()), 2)
        self.assertEqual(store.calculate_change(coins, headphones.get_price()), -1)
        

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