from product import Product
#from store import Store - commenting out bc it gives an error when running unittest. Uncomment out if you want to test algorithms or test algorithms in the store.py file 
import store
def fewest_coins(coins , amount, coin_cache = None ):
  
  a = amount
  if coin_cache is None :
    coin_cache = {}
  for key in coin_cache.items():
      if coin_cache[key] == amount:
        return coin_cache[amount]
  for c in coins:
    if amount == c: 
      coin_cache[amount] = 1
    else:
      coin_count = amount // c 
      a = amount % c
      coin_cache[amount] = coin_count + fewest_coins(a, coins, coin_cache)  

  return coin_cache[amount]

  
  

"""this algorthim compares the product ids to find the largest and moves it to the end and repeats moving the next largest to the next spot """
def selection_sort(products):
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
  low = 0
  high =len(products) - 1
  if low > high:
    return -1

  mid = (low + high) // 2

  if products[mid].get_id() == products_id:
    return products[mid]
  elif products[mid].get_id() > products_id:
    return binary_search(products[low : mid - 1 ], products_id)
  else:
    return binary_search(products[mid + 1 : high], products_id)
      
  
      



  
def recursive_total_price(products):
  """Calculates the total price of products in a list, recursively"""
  if len(products) == 0:
    return 0
  else:
    return products[0].price + recursive_total_price(products[1:])

def bubble_sort(products):
  """Sorts products by id in-place via bubble sort"""
  for i in range(len(products) - 1):
    swapped = True
    for j in range(len(products) - 1 - i):
      if products[j].get_id() > products[j + 1].get_id():
        products[j], products[j+1] = products[j+1], products[j]
        swapped = True 
    if not swapped: break

def insertion_sort(products):
  """Sorts products by id in-place via insertion sort"""
  for i in range(1, len(products)):
    j = i
    while j > 0 and products[j - 1].get_id() > products[j].get_id():
      products[j], products[j-1] = products[j-1], products[j]
      j -= 1
  return products




if __name__ == "__main__":
  coins = [1,5,10,25]
  print(fewest_coins(coins,12))