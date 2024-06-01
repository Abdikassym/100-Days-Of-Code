print("Welcome to Pizza Hut")
size = input("Which size of pizza do you prefer? S/M/L: ").lower()
pepperoni = input("Would you like to add some extra pepperoni? Y/N: ").lower()
cheese = input("Would you like to add some extra cheese? Y/N: ").lower()
bill = 0

if size == "small" or size == "s":
    bill += 20
elif size == "medium" or size == "m":
    bill += 25
elif size == "large" or size == "l":
    bill += 30
if pepperoni == "yes" or "y":
    bill += 5
else:
    pass

if cheese == "yes" or "y":
    bill += 5
else:
    pass


print(f"Cost of your pizza now is {bill}$")



