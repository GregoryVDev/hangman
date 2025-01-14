import random
import string

from words import words

def choice_word(words):
    word = random.choice(words)
    return word

def hangman():
    original_word = choice_word(words)
    word = original_word.upper()

    letter = set(word)
    alphabet = set(string.ascii_uppercase)
    letters_used = set()
    essai = 6

    while len(letter) > 0 and essai > 0:
        print("Vous avez", essai, "essai(s) et vous avez utilisé les lettres suivantes:", ','.join(letters_used))
        list = [letters if letters in letters_used else "_" for letters in word]
        print("Le mot actuel est: ", ' '.join(list))

        letter_choice = input("Entrer une lettre").upper()
        if letter_choice in alphabet - letters_used:
            letters_used.add(letter_choice)
            if letter_choice in letter:
                letter.remove(letter_choice)
                essai = 6
            else:
                essai -= 1
                print("Il vous reste", essai, "essai(s)")
        elif letter_choice in letters_used:
            print("Vous avez déjà utilisé cette lettre")
        else:
            print("Votre choix est invalide, merci de saisir une lettre")
    if essai == 0:
        print("Vous avez perdu le mot était", word)
    else:
        print("Le mot a deviné est", word, "vous avez gagné")


hangman()