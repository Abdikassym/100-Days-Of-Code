import random
from art import logo
from replit import clear

restart = True

while restart:
    clear()
    print(logo)
    answer = random.randint(1, 100)
    print(answer, "is answer")

    game_difficulty = input("Choose the difficulty of your game 'Hard' or 'Easy' (h/e): ")
    if game_difficulty == "h":
        lives = 5
    else:
        lives = 10
    game_is_on = True

    while game_is_on:
        guess = int(input("Guess the number between 1 and 100: "))
        if guess > answer:
            lives -= 1
            print(f"Too high, you have {lives} lives left")
        elif guess < answer:
            lives -= 1
            print(f"Too high, you have {lives} lives left")
        else:
            print(f"You have won! The correct answer is {answer}")
            game_is_on = False
        if lives == 0:
            print(f"You have lost, the answer is {answer}")
            game_is_on = False

    if input("Would you like to restart a game? y/n ") == "n":
        restart = False
        print("Goodbye!")
