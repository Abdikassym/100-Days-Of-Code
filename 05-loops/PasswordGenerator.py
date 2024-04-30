import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

amount_of_letters = int(input('How many letters would you like in your password? '))
amount_of_numbers = int(input('How many numbers would you like in your password? '))
amount_of_symbols = int(input('How many symbols would you like in your password? '))

final_password = []

for i in range(amount_of_letters):
    final_password.append(random.choice(letters))

for i in range(amount_of_numbers):
    final_password.append(random.choice(numbers))

for i in range(amount_of_symbols):
    final_password.append(random.choice(symbols))


random.shuffle(final_password)

final_password = ''.join(final_password)
print(final_password)
