from product import Product
def fewest_coins(coins, amount):
  coin = [.01,.05,.10,.25]
  cache = {}

def selection_sort(products):
  """this algorthim compares the product ids to find the largest and moves it to the end and repeats moving the next largest to the next spot """"
  length = len(products)
  for i in range(length - 1):
    max = 0
    sort = length - i
    for j in range(sort):
      if products[j].get_id() > products[max].get_id():
        max = j

      if sort - 1 != max:
        products[sort - 1], products[max] =  products[max], products[sort - 1]

def binary_search(products, product_id):
  pass
def recursive_total_price(products):
  pass

def bubbble_sort(products):
  pass
def insertion_sort(products):
  pass