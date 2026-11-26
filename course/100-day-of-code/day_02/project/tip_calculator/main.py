print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip_percent = float(input("How much tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill?"))

tip_amount = bill * tip_percent / 100
total_bill = bill + tip_amount
amount_per_person = total_bill / number_of_people
print("Each person should pay " + str(round(amount_per_person, 2)))