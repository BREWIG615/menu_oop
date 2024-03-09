from checkout import *
from order import *
from inquire import *

customer = Checkout()

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
        if customer.checkouts:
            print("Your current order: ")
            for checkout in customer.checkouts:
                checkout.show()
        
        else:
            print("You have not yet placed an order.")
    
    elif action == 'd':
        print("Your choice of items are: food, drink, or dessert")
        print("1. food")
        print("2. drink")
        print("3. dessert")
        try:
            item_choice = int(input("Enter the number for your food selection: "))
            if item_choice == 1:
                item_type = "food"
            elif item_choice == 2:
                item_type = "drink"
            elif item_choice == 3:
                item_type = "dessert"
            else:
                print("Invalid item choice.")
                continue
        except ValueError as e:
            print(e)

            #item_type = input("Enter the item type here (food, drink, or dessert): ")
        item_names = menu.get_item_names(item_type)
        print(f"Your options for {item_type} items are:")
        for index, name in enumerate(item_names, 1):
            print(f"{index}. {name}")
        item_name = input("\nEnter the item name here: \n")
        try:
            description = menu.get_item_description(item_type.capitalize(), item_name)
            print("Item Description:", description)
        except ValueError as e:
            print(e)    
    # if action == 'd':
    #     print("Your choice of items are: food, drink, or dessert")
    #     print("1. food")
    #     print("2. drink")
    #     print("3. dessert")
    #     try:
    #         item_choice = int(input("Enter the number for your food selection: "))
    #         if item_choice == 1:
    #             item_type = "food"
    #         elif item_choice == 2:
    #             item_type = "drink"
    #         elif item_choice == 3:
    #             item_type = "dessert"
    #         else:
    #             print("Invalid item choice.")
    #             continue
    #     except ValueError as e:
    #         print(e)

    #     print(f"Your options for your item names are: Hot Dog, Burger, Steak, Seltzer, Beer, Wine, Cookies, Cake, Pie\n")
    #     print("1. Hot Dog")
    #     print("2. Burger")
    #     print("3. Steak")   
    #     print("4. Seltzer")
    #     print("5. Beer")
    #     print("6. Wine")   
    #     print("7. Cookies")
    #     print("8. Cake")
    #     print("9. Pie")   
    #     try:
    #         name_choice = int(input("Enter the number for your name selection: "))
    #         if name_choice == 1:
    #             item_name = "Hot Dog"
    #         elif name_choice == 2:
    #             item_name = "Burger"
    #         elif item_choice == 3:
    #             item_name = "Steak"
    #         elif name_choice == 4:
    #             item_name = "Seltzer"
    #         elif name_choice == 5:
    #             item_name = "Beer"
    #         elif item_choice == 6:
    #             item_name = "Wine"
    #         elif name_choice == 7:
    #             item_name = "Cookies"
    #         elif name_choice == 8:
    #             item_name = "Cake"
    #         elif item_choice == 9:
    #             item_name = "Pie"
    #         else:
    #             print("Invalid name choice.")
    #             continue
    #     except ValueError as e:
    #         print(e)
    #     try:
    #         menu = Menu()
    #         description = menu.get_item_description(Menu(item_type, item_name))
    #     except ValueError as e:
    #         print(e)
        
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
            customer.add_item(Order(food, drink, dessert))
        except ValueError as e:
            print(e)

    elif action == 'q':
        break

    else:
        print('That was not a valid selection')
