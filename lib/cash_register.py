#!/usr/bin/env python3

class CashRegister:

  def __init__(self, discount=0):
    self.total = 0
    self.discount = discount
    self.items = []
    self.previous_transaction = []

  def add_item(self, item, price, quantity=1):
    self.total += price * quantity
    for i in range(quantity):
            self.items.append(item)
    self.previous_transaction.append({"item": item, "price": price, "quantity": quantity})


  def apply_discount(self):
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
      self.total = int(self.total * (1 - (self.discount/100)))
      print(f"After the discount, the total comes to ${self.total}.")
    

  def items_list(self):
    return self.items

  def void_last_transaction(self):
    if not self.previous_transaction:
            return "There are no transactions to void."
    self.total -= ( self.previous_transaction[-1]["price"] * self.previous_transaction[-1]["quantity"] )

      

  def empty_transaction(self):
    self.items = []

  def get_total(self):
    return self.total
  
