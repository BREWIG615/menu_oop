import json
import os

class Menu:
    def __init__(self, filename='menu.json'):
        self.filename = filename
        self.menu_data = self.load_menu_data()

    def load_menu_data(self):
        try:
            with open(self.filename, 'r') as f:
                menu_data = json.load(f)
                return menu_data
        except FileNotFoundError:
            print("Menu file not found.")
            return {}
        
    def get_item_names(self, item_type):
        if item_type in self.menu_data:
            return [item['name'] for item in self.menu_data[item_type]]
        else:
            return []
        
    def get_item_description(self, item_type, item_name):
        for item in self.menu_data:
            if item['type'] == item_type and item['name'] == item_name:
                return item['description']
        return "Description not found."
        
if  __name__ == "__main__":
    desc = Menu()

    item_type = input("Enter the item type here (food, drink, or dessert): ")
    item_name = input("Enter the item name here: ")

    try:
        description = desc.get_item_description(item_type, item_name)
        print("Item Description:", description)
    except ValueError as e:
        print(e)