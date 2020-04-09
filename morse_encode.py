letter_to_morse = {'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.', 
                   'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 
                   'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-',
                   'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..',
                   '0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....-',
                   '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.',
                   ' ':'/'}

message = input("Please enter a message:\n")


def encode(message):
    morse = []

    for letter in message:
        letter = letter.lower()
        morse.append(letter_to_morse[letter])

    # We need to join together Morse code letters with spaces
    morse_message = " ".join(morse)
    
    return morse_message


encoded_message = encode(message)
print(f"Message: {message}\nMorse encoded: {encoded_message}")
