print("Welcome to the Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
final_bill = 0

if size == 'S':
    final_bill = 15
    if pepperoni == 'Y':
        final_bill += 2

elif size == 'M':
    final_bill = 20
    if pepperoni == 'Y':
        final_bill += 3

elif size == 'L':
    final_bill = 25   
    
else:
    print("Wrong input. Try again!")

if extra_cheese == 'Y':
    final_bill += 1

print("Your final bill is: $" + str(final_bill) + ".")

