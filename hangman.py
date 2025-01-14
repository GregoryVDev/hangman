import random
from words import words

def choice_word(words):
    word = random.choice(words)
    return word

def hangman():
    original_word = choice_word(words)
    word = original_word.upper()

    letter = set(word)

    print(letter)

hangman()