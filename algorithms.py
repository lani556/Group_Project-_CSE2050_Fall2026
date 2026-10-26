from product import Product
from store import Store 
def fewest_coins(coins, amount, coin_cache = None ):
  coins.sorted(reverse = True)
  a = amount
  if coin_cache is None :
    coin_cache = {}
  if amount in coin_cache : return coin_cache[amount]
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
  pass
def recursive_total_price(products):
  if len(products) == 0:
    return 0
  else:
    return products[0].price + recursive_total_price(products[1:])

def bubbble_sort(products):
  for i in range(len(products) - 1):
    swapped = True
    for j in range(len(products) - 1 - i):
      if products[j].get_id() > products[j + 1].get_id():
        products[j], products[j+1] = products[j+1], products[j]
        swapped = True 
    if not swapped: break
  return products

def insertion_sort(products):
  for i in range(1, len(products)):
    j = i
    while j > 0 and products[j - 1].get_id() > products[j].get_id():
      products[j], products[j-1] = products[j-1], products[j]
      j -= 1
    return products




if __name__ == "__main__":
  coins = [1,5,10,25]
  print(fewest_coins(coins,12))