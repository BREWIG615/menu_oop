from Order.checkout import *
from Order.order import *
from inquire import *

customer = Order()
menu = Menu()

while True:
    print()
    print("To show order, press s")
    print("To place order, press p")
    print("To inquire about a specific item, press d")
    print("To quit, press q")

    action = input("What would you like to do: ").lower()
    print()

    if action == 's':
        if customer.orders:
            print("Your current order: ")
            for order in customer.orders:
                order.show()
        else:
            print("You have not yet placed an order.")

    elif action == 'd':
        item_type = 'Food'  # Example item type
        item_names = menu.get_item_names(item_type)

        # Print the item names for the specified type
        print(f"Your options for {item_type} items are:")
        for index, name in enumerate(item_names, 1):
            print(f"{index}. {name}")
    elif action == 'p':
        print("Your choice of food items are: Hot Dog, Burgers, Steak")
        print("1. Hot Dog")
        print("2. Burger")
        print("3. Steak")

        try:
            food_choice = int(input("Enter the number for your food selection: "))
            if food_choice == 1:
                food = "Hot Dog"
            elif food_choice == 2:
                food = "Burger"
            elif food_choice == 3:
                food = "Steak"
            else:
                print("Invalid food choice.")
                continue
        except ValueError as e:
            print(e)

        print(f"Your options for your drink items are: Seltzer, Beer, Wine\n")
        print("1. Seltzer")
        print("2. Beer")
        print("3. Wine")

        try:
            drink_choice = int(input("Enter the number for your drink selection: "))
            if drink_choice == 1:
                drink = "Seltzer"
            elif drink_choice == 2:
                drink = "Beer"
            elif drink_choice == 3:
                drink = "Wine"
            else:
                print("Invalid drink choice.")
                continue
        except ValueError as e:
            print(e)

        print(f"Your options for dessert items are: Cookies, Cake, Pie\n")
        print("1. Cookies")
        print("2. Cake")
        print("3. Pie")

        try:
            dessert_choice = int(input("Enter the number for your dessert selection: "))
            if dessert_choice == 1:
                dessert = "Cookies"
            elif dessert_choice == 2:
                dessert = "Cake"
            elif dessert_choice == 3:
                dessert = "Pie"
            else:
                print("Invalid dessert choice.")
                continue
        except ValueError as e:
            print(e)

        try:
            customer.add_item(Restaurant(food, drink, dessert))
        except ValueError as e:
            print(e)

    elif action == 'q':
        break

    else:
        print('That was not a valid selection')
