import os
import time
import sys
from textblob import TextBlob

bot_template = "BOT : {0}"
user_template = "USER : {0}"
starter = """
*************************
WELCOME TO THE GIBRAN-098
*************************
Ship Status: NULL
Security Check: NULL
"""

class InputAnalysis:
        def __init__(self, text):
            self.blob = TextBlob(text)
            self.pol = self.blob.sentiment[0]
            self.sent_state = ""

        def sentiment(self):
            if (self.pol > .25):
                return "good"
            elif (self.pol < .25):
                return "bad"    

def slow_print(text):
    """Diplsay text slower on the screen"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.05)

def speak_and_spell(text):
    """Display text and have the system read it once displayed"""
    print(bot_template.format(text))
    os.system('say ' + text)

print(starter)
speak_and_spell("Hello how are you?")
intro = InputAnalysis(input(user_template.format("")))

speak_and_spell("You sound " + intro.sentiment() + ". How can I help you today?")