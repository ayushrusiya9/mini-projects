print("Welcome!")

total = 0

while True:
    print("Anything else!")
    choice = int(input("1. Coffe  Rs.149\n2. Chai Rs. 20\n3. Pizza Rs. 199\n4. Burger Rs. 99\n5. Manchurian Rs. 89\n6. Noodles Rs.89\n7. Chicken Roll Rs. 149 \n8. Egg Roll Rs. 119\n9. Bill/Exit\nENTER ITEM NUMBER: "))

    if choice <= 9:

        if choice == 1:
            total = total + 149
            print("Coffe in making process............")
        elif choice == 2:
            total = total + 20    
            print("Chai in making process............")
        elif choice == 3:
            total = total + 199
            print("Pizza in making process............")
        elif choice == 4:
            total = total + 99
            print("Burger in making process............")
        elif choice == 5:
            total =  total + 89
            print("Manchurian inmaking process............")
        elif choice == 6:
            total = total + 89
            print("Noodles in making process............")
        elif choice == 7:
            total = total + 149
            print("Chicken Roll in  making process............")
        elif choice == 8:
            total = total + 119
            print("Egg Roll in making process............")
        elif choice == 9:
            print(f'YOUR TOTAL AMOUNT IS Rs.{total} -/ ONLY')
            break
    else:
        print('INVALID NUMBER!')    


print('THANKYOU!\nVISIT AGAIN :) ')