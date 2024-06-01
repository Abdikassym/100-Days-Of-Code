# Text to morse code converter

# TODO: 1. Create dictionary of morse alphabet
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


# TODO: 2. Receive input from user
text_to_convert = input("Input the text that you want to convert to MORSE CODE: ")


def text_to_morse(text):
    result = ""
    for symbol in text:
        try:
            if symbol == " ":
                result += " "
            else:
                result += f"{MORSE_CODE_DICT[symbol.capitalize()]} "
        except KeyError:
            result += symbol
    return result


print(text_to_morse(text_to_convert))

