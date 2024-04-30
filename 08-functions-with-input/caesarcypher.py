alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

second_part_of_alphabet = alphabet[26:]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.


def caesar(text, shift, direction):
    code = ""
    if direction == "decode":
        shift *= -1
    for i in text:
        initial_position = alphabet.index(i)
        new_position = alphabet[initial_position + shift]
        code += new_position
    print(code)


caesar(text=text, shift=shift, direction=direction)

# def encrypt(text, shift):
#     code = ""
#     for i in text:
#         initial_position = alphabet.index(i)
#         new_position = alphabet[initial_position + shift]
#         code += new_position
#
#     print(code)
#
#
# def decrypt(text, shift):
#     code = ""
#     for i in text:
#         initial_position = alphabet.index(i)
#         new_position = second_part_of_alphabet[initial_position - shift]
#         code += new_position
#
#     print(code)
#
#
# if direction == "encrypt":
#     encrypt(text, shift)
# else:
#     decrypt(text, shift)
