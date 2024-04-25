print("Hello! Welcome to the Treasure Island! Your mission is to find a treasure!")

if input("Left or right? ").lower() == "left":
    if input("You went the right way. You are in front of a river? Swim or Wait? ").lower() == "wait":
        choice = input("There are 3 doors appeared in front of you.\n"
                       "Red, blue and yellow. Which one do you choose? ").lower()
        if choice == "red":
            print("Burnt by fire. Game over")
        elif choice == "blue":
            print("Eaten by beasts. Game over")
        elif choice == "yellow":
            print("Treasure! You win!")
        else:
            print("You haven't picked anything. Burnt by sun ray.")
    else:
        print("You were attacked by orcs. Game over")
else:
    print("You fall into a hole. Game over")

