import os
import time
import sys
import spacy
from textblob import TextBlob

nlp = spacy.load('en')

bot_template = "BOT : {0}"
user_template = "USER : {0}"

class InputAnalysis:
        def __init__(self, text):
            self.blob = TextBlob(text)
            self.pol = self.blob.sentiment[0]
            self.subj = self.blob.sentiment[1]
            self.sent_state = ""

        def sentiment(self):
            if (self.pol > .25) & (self.subj > .5):
                return "good"
            elif (self.pol > .25) & (self.subj < .5):
                return "okay"
            elif (self.pol < .25) & (self.subj > .5):
                return "busy"
            elif (self.pol < .25) & (self.subj < .5):
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

speak_and_spell("Hello how are you?")
intro = InputAnalysis(input(user_template.format("")))

speak_and_spell("You sound " + intro.sentiment() + ". How can I help you today?")