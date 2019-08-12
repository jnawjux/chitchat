import os
import time
import sys
import spacy

bot_template = "BOT : {0}"
user_template = "USER : {0}"

def slow_print(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.05)

def speak_and_spell(text):
    print(bot_template.format(text) + '\n')
    os.system('say ' + text)

speak_and_spell("Hello how are you?")
inputString = input(user_template.format(""))