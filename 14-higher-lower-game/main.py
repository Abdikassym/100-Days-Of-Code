from art import logo, vs
from game_data import data
from random import choice
from replit import clear


def compare(first, second):
    if first['follower_count'] > second['follower_count']:
        return "a"
    else:
        return 'b'


def show_score(score):
    if score > 0:
        print(f"You're right! Current score: {score}")


def higher_lower():
    game_is_on = True
    score = 0

    first_person = choice(data)

    # cycle of game starts here
    while game_is_on:

        data.remove(first_person)
        print(logo)
        second_person = choice(data)

        show_score(score)

        print(
            f"Compare A: {first_person['name']}, a {first_person['description']}, from {first_person['country']} test{first_person['follower_count']}")
        print(vs)
        print(
            f"Compare B: {second_person['name']}, a {second_person['description']}, from {second_person['country']} test-{second_person['follower_count']}")

        guess = input("Who has more followers? Type 'A' or 'B'").lower()
        if guess == compare(first_person, second_person):
            score += 1
            clear()
            first_person = second_person
        else:
            clear()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            return


higher_lower()