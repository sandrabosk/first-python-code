""" Let's determine how much money you would make if you sold all of your food.

Create a variable called total and set it to zero.
Loop through the prices dictionary.
For each key in prices, multiply the number in prices by 
the number in stock. Print that value into the console and then add it to total.
Finally, outside your loop, print total.
 """
 
 prices = {
  "banana" : 4,
  "apple"  : 2,
  "orange" : 1.5,
  "pear"   : 3,
}
stock = {
  "banana" : 6,
  "apple"  : 0,
  "orange" : 32,
  "pear"   : 15,
}

shopping_list = ["banana", "orange", "apple"]

for key in prices:
  print key
  print "price: %s" % prices[key]
  print "stock: %s" % stock[key]
  
  
  """ Define a function compute_bill that takes one argument food as input.
In the function, create a variable total with an initial value of zero.
For each item in the food list, add the price of that item to total.
Finally, return the total. 
Ignore whether or not the item you're billing for is in stock.
Note that your function should work for any food list. 
"""
def compute_bill(food):
  total = 0
  for item in food:
    total = total + prices[item]
  return total
