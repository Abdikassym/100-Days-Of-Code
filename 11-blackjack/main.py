import random
from art import logo

# Blackjack Project

# Our Blackjack House Rules

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_cards = []
dealer_cards = []


def show_cards():
    print(f"This is your cards {player_cards} and total score is {calculate_total(player_cards)}")
    print(f"This is one of dealer's card {dealer_cards[0]}")


def calculate_total(cards_to_calculate):
    total_score = 0
    for card_score in cards_to_calculate:
        total_score += card_score
    return total_score


def draw_a_card(deck):
    random_card = random.choice(cards)
    deck.append(random_card)
    return deck


def player_score():
    return calculate_total(player_cards)


def dealer_score():
    return calculate_total(dealer_cards)


def switch_ace_to_1(deck):
    deck = sorted(deck)
    deck[-1] = 1
    print(deck)
    return deck


# start of the game
game_is_on = True

while game_is_on:
    print(logo)
    print("Welcome to blackjack!")
    for start_card in range(2):
        draw_a_card(player_cards)
        draw_a_card(dealer_cards)
    show_cards()

    keep_thinking = True
    while keep_thinking:
        stand_or_hit = input("Would you like to hit another card (y) or stand? (n): ")
        if stand_or_hit == "y":
            player_cards = draw_a_card(player_cards)
            player_score()
            show_cards()
        else:
            keep_thinking = False
    while dealer_score() < 18:
        draw_a_card(dealer_cards)
        dealer_score()
        if dealer_score() > 21 and 11 in dealer_cards:
            dealer_cards = switch_ace_to_1(dealer_cards)
    player_points = 21 - player_score()
    dealer_points = 21 - dealer_score()
    if player_score() > 21 and dealer_score() > 21:
        print("DRAW!")
    elif player_score() <= 21 < dealer_score():
        print("Player won!")
    elif dealer_score() <= 21 < player_score():
        print("Dealer won!")
    elif player_score() == dealer_score():
        print("DRAW!")
    elif player_points < dealer_points:
        print("Player won!")
    else:
        print("Dealer won!")

    print(f"your total card score is {player_score()}")
    print(f"dealer's cards are {dealer_cards} and total score is {dealer_score()}")

    restart = input("\nWould you like to restart a game? y/n ")
    if restart == "n":
        game_is_on = False
    else:
        dealer_cards = []
        player_cards = []
