order= input("Hi! Welcome to Cafeko. Are you ready to order, or would you like to take a look at our menu? yes/no: ")

drinks = {
        1: ("Espresso", 100),
        2: ("Americano", 120),
        3: ("Cappuccino", 150),
        4: ("Latte", 160),
        5: ("Iced Coffee", 140),
        6: ("Matcha Latte", 180)
}
pastries = {
        7: ("Blueberry Muffin", 90),
        8: ("Chocolate Chip Cookie", 70),
        9: ("Cheesecake Slice", 150 ,)
    }
if order.lower() == "yes":  
    print("Here's our menu:")
    print("DRINKS:")
    for number,(name,price) in drinks.items():
        print(f"{number}. {name} - ₱{price}")
   
    print("PASTRIES:")
    for number,(name,price) in pastries.items():
        print(f"{number}. {name} - ₱{price}")
else:
    print("Let us know when you're ready!")
    exit()

total = 0
buylist = []

while True:
        order1= int(input("What would you like to order? (Enter the number of the item you want to order): "))
        if order1 in drinks:
             name,price= drinks[order1]
        elif order1 in pastries:
             name,price= pastries[order1]
        else:
            print("Invalid item number. Please try again.")
            continue 
    
        total += price
        print(f"You added {name} ₱{price} ")
        buylist.append(name)

        order2 =input("Would you like anything else? (yes/no): ")
   
        if order2.lower() == "no":
                 print(f"Alright, here's your order {buylist}, your total is ₱{total:.2f}. Thank you for your order!")
                 break
        
while True: 
    payment = float(input("Please enter amount of payment: "))
    if(float(payment)>= total):
        forchange = payment - total
        fortotal = print(f"I received ₱{payment:.2f} Your change is ₱{forchange:.2f} ")
        print("Thank you so much for your purchase! Have a great day.")
        exit()
    else:
        print("Invalid! please input a right amount")

                 
                       




