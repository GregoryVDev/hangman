import random
import string

from words import words

score = 0
player = ""

def choice_word(words):
    word = random.choice(words)
    return word

def again():
    replay = input("Souhaitez-vous continuer à jouer? (O = Oui, N = Non)")
    # Tant que les 4 lettres n'ont pas été tapé, on va afficher de nouveau ce message
    while replay not in {"O", "o", "N","n"}:
        replay = input("Souhaitez-vous continuer à jouer? (O = Oui, N = Non)")
    if replay == "O" or replay == "o":
        hangman()
    elif replay == "N" or replay == "n":
        print("A bientôt")
        exit()

def name():
    player = input("Merci de saisir votre nom:")
    player = player.capitalize()
    if not player.isalpha() or len(player) < 3:
        print("Le nom que vous avez saisi est invalide")
        return name()
    else:
        return player

def hangman():

    global player
    if player == "":
       player = name()

    global score

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
        print(player, ",vous avez perdu le mot était", word)
        again()
    else:
        print(player, ",le mot à deviné est", word, "vous avez gagné")
        score += 10
        print("Votre score est:", score)
        again()

hangman()