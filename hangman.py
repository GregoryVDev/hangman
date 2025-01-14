import random
from words import words

def choice_word(words):
    word = random.choice(words)
    return word

print(choice_word(words))