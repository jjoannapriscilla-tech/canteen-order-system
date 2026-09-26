import orders
import menu

while True:
    print("\n========== CANTEEN ORDER SYSTEM ==========")
    print("1. View Menu")
    print("2. Search Food")
    print("3. Add Food to Order")
    print("4. Remove Food from Order")
    print("5. View Order")
    print("6. View Total")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        menu.view_menu()

    elif choice == 2:
        menu.search_food()

    elif choice == 3:
        food = input("Enter food name: ")

        if food in menu.food_menu:
            quantity = int(input("Enter quantity: "))
            orders.add_item(food, menu.food_menu[food], quantity)
            print("Item added to order.")

        else:
            print("Food is not available.")

    elif choice == 4:
        food = input("Enter food name to remove: ")

        if orders.remove_item(food):
            print("Item removed from order.")
        else:
            print("Item not found in order.")

    elif choice == 5:
        orders.view_order()

    elif choice == 6:
        total = orders.calculate_total()
        print("Total Bill: ₹", total)

    elif choice == 7:
        print("Thank you! Have your food.")
        break

    else:
        print("Invalid choice.")
  