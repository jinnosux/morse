import speech_recognition as sr
r = sr.Recognizer()
m = sr.Microphone()

#set threhold level
with m as source: r.adjust_for_ambient_noise(source)
print("Set minimum energy threshold to {}".format(r.energy_threshold))

# obtain audio from the microphone
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)



letter_to_morse = {'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.', 
                   'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 
                   'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-',
                   'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..',
                   '0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....-',
                   '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.',
                   ' ':'/'}

message = r.recognize_google(audio)

def encode(message):
    morse = []

    for letter in message:
        letter = letter.lower()
        morse.append(letter_to_morse[letter])

    # We need to join together Morse code letters with spaces
    morse_message = " ".join(morse)
    
    return morse_message


encoded_message = encode(message)
print(f"Google recognized you said: {message}\nMorse encoded: {encoded_message}")
