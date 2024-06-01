import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
lives = 7

answer = random.choice(word_list)

hidden_word = ["_" for i in answer]

end_of_game = False

while not end_of_game:
    print(hidden_word)
    print(stages[lives - 1])
    print(f"you have {lives} left")
    guess = input(f"Guess a letter in the word {answer}: ").lower()

    for letter in range(len(answer)):
        if guess == answer[letter]:
            hidden_word[letter] = guess

    if guess not in answer:
        lives -= 1

    if "_" not in hidden_word:
        end_of_game = True
        print("You have won!")
    elif lives == 0:
        end_of_game = True
        print("Game over!")




