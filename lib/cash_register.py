#!/usr/bin/env python3
"""
  Add items of varying quantities and prices
  Calculate discounts
  Keep track of what's been added to it
  Void the last transaction
 """
# class CashRegister:
  
#   def __init__(self, discount= 0):
#     self.discount = discount
#     self.total = 0
#     self.items = []
#     self.prices = []
#     # self.add_items = True

#   # def reset(self):
#   #   self.total=0
#   #   self.items=[]

#   def add_item(self, title, price, quantity=1):
#     # reset = []
#     # if self.add_item:
#     if type(title) == str and price >= 0:
#       if quantity != 0:
#         self.total += price *quantity 
        
#       else:
#         self.total += price
      
#       for _ in range(quantity):
#         self.items.append(title) 
#         self.prices.append(price)
#       return self.items
      
#     return ""
      
#     # self.items.clear()
  


#   def apply_discount(self):
#     if self.discount:
#      self.total = float((self.total * (1.0-0.2)))
#      print(f"After the discount, the total comes to ${self.total:.0f}.")
#     else:
#       print("There is no discount to apply.")

  
#   def void_last_transaction(self):
#         if self.items:
#             # Assuming each item contributes equally to the total
#             item_price = self.total / len(self.items)
#             self.total -= item_price
#             print(f"Voided last transaction: {item_price:.2f}")

#             if not self.items:
#                 self.total = 0.0
#                 print("All items removed. Total reset to 0.0.")
#         else:
#             print("No items to void.")


class CashRegister:
    def __init__(self, discount=0):
        # Initialize CashRegister with an optional discount, defaulting to 0.
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, item, price, quantity=1):
        # Add an item to the register with a specified price and optional quantity.
        self.total += price * quantity
        # Add the item to the items list based on the specified quantity.
        self.items.extend([item] * quantity)
        # Record the transaction details in the previous_transactions list.
        self.previous_transactions.append({"item": item, "quantity": quantity, "price": price})

    def apply_discount(self):
        # Apply a discount to the total if a discount is set.
        if self.discount:
            self.total = int(self.total * (1 - self.discount / 100))
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        # Void the last transaction by subtracting its cost from the total.
        if not self.previous_transactions:
            return "There are no transactions to void."
        last_transaction = self.previous_transactions.pop()
        self.total -= last_transaction["price"] * last_transaction["quantity"]
        # Remove the items from the items list based on the last transaction's quantity.
        self.items = self.items[:-last_transaction["quantity"]]