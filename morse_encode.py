import sys
import pygame
import time
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

s = input("For audio, press 1.\nFor a text, press 2:\n")
if s == "1":
    ONE_UNIT = 0.5
    THREE_UNITS = 3 * ONE_UNIT
    SEVEN_UNITS = 7 * ONE_UNIT
    PATH = 'morse_sound_files/'

    pygame.init()

    for char in message:
	    if char == ' ':
		    print (' '*7 )
		    time.sleep(SEVEN_UNITS)
	    else:
		    pygame.mixer.music.load(PATH + char.upper() + '_morse_code.ogg')
		    pygame.mixer.music.play()
		    time.sleep(THREE_UNITS)
    print(f"Google recognized you said: {message}\nMorse encoded: {encoded_message}")
elif s == "2" :
    
    print(f"Google recognized you said: {message}\nMorse encoded: {encoded_message}")
else :
    print("wrong option")
