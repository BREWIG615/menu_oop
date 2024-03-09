import json
import os

from order import *

class Checkout:
    def __init__(self):
        self.checkouts = []

    def add_item(self, item):
        self.checkouts.append(item)

if __name__ == "__main__":
    customer = Checkout()

    food = input("Enter your food selection here: ")
    drink = input("Enter your drink selection here: ")
    dessert = input("Enter your dessert selection here: ")

    try: 
        customer = Order(food, drink, dessert)

        customer.show()
        customer.add_item(customer)
    except ValueError as e:
        print(e)