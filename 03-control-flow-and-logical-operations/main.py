height = int(input("What is your height? "))

if height >= 120:
    age = int(input("How old are you? "))
    if age < 12:
        print("Welcome to a roller coaster!")
        print("Your price is 5$!")
    elif 18 > age >= 12:
        print("Welcome to a roller coaster!")
        print("You owe me 7$ now!")
    else:
        print("Welcome to a roller coaster!")
        print("For you it will be 12$!")
else:
    print("Sorry, you are too short for this :c")













