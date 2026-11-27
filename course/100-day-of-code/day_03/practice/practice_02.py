# Program to check the user input odd or event

user_input = int(input("Enter a number: "))
if user_input % 2 == 0:
    print("The number " + str(user_input) + " is event.")
else:
    print("The number " + str(user_input) +" is odd.")