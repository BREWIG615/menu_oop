import json

class Order:
    def __init__(self, food, drink, dessert):
        self.food_choices = ["Hot Dog", "Burger", "Steak"] # Ensure that I account for caps and mispelling
        if food not in self.food_choices:
            raise ValueError("Invalid value for \"food\" item.")
        self.food = food
        self.drink_choices = ["Seltzer", "Beer", "Wine"]
        if drink not in self.drink_choices:
            raise ValueError("Invalid value for \"drink\" item.")
        self.drink = drink
        self.dessert_choices = ["Cookies", "Cake", "Pie"]
        if dessert not in self.dessert_choices:
            raise ValueError("Invalid value for \"dessert\" item.")
        self.dessert = dessert

    def show(self):
        print("      for food you selected:         ", self.food)
        print("      for a drink you chose:         ", self.drink)
        print("      and for dessert you went with: ", self.dessert)

    def inspect(self, item_type):
        if item_type.lower() == 'food':
            return self.get_description('food')
        elif item_type.lower() == 'drink':
            return self.get_description('drink')
        elif item_type.lower() == 'dessert':
            return self.get_description('dessert')
        else:
            return "Invalid item type."
        
    def get_description(self, item_type):
        with open('menu.json', 'r') as f:
            menu_data = json.load(f)
            for item in menu_data[item_type]:
                if item['name'] == getattr(self, item_type):
                    return item['description']
            return "Description not found."