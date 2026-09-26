#Menu
food_menu={"Idli":30,"Dosa":40,"Fried Rice":80,"Sandwich":50,"Tea":15}
while(True):
    print("========== CANTEEN ==========")
    print("1. View Menu")
    print("2. Search Food")
    print("3. Exit")

    ch=int(input("Enter your choice:"))
    if(ch==1):
        print("========== CANTEEN MENU ==========")
        print("1. Idli          ₹30")
        print("2. Dosa          ₹40")
        print("3. Fried Rice    ₹80")
        print("4. Sandwich      ₹50")
        print("5. Tea           ₹15")
       
    elif(ch==2):
        food=input("Enter the food name:")
        if(food in food_menu.keys()):
            print(food,"is available.")
            print("Price: ₹",food_menu[food])
           
        else:
            print(food,"is not available")

    elif(ch==3):
        print("Thank you Have your food")
        break
          