from random import random
from random import randint
import Constants as Keys


def response(user_input):
    string = str(user_input) + " is " + str(round(random() * 100)) + "% sagzan! " + double_emoji()
    print(string)
    return string


def double_emoji():
    return str(Keys.emojis[randint(0, len(Keys.emojis) - 1)] + Keys.emojis[randint(0, len(Keys.emojis) - 1)])
