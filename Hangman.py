import random
import hangman_stages
import sys
import os

words = ['over','round','nice','love','qurban','nape']


def select_word(words):
    return random.choice(words)


remaining_attempts = 6
guessed_letters = ""


def print_secret_word(secret_word,guessed_letters):
    for letter in secret_word:
        if letter in guessed_letters:
            print(" {} ".format(letter),end="")
        else:
            print(" _ ",end="")
    print("\n")


def is_guess_in_secret_word(guess, secret_word):
    if len(guess) > 1 or not guess.isalpha():
        print("Only single letters are allowed. Unable to continue...")
        sys.exit()
    else:
        if guess in secret_word:
            return True
        else:
            return False


def get_unique_letters(word):
    return "".join(set(word))


secret_word = select_word(words)

while remaining_attempts > 0 and len(guessed_letters) < len(get_unique_letters(secret_word)):

    guess = input("Guess a letter :")
    guess_in_secret_word = is_guess_in_secret_word(guess, secret_word)

    if guess_in_secret_word:
        if guess in guessed_letters:
            print("You already guessed this letter...")
        else:
            print("Good Work , The letter {} is the part of secret word.".format(guess))
            guessed_letters += guess
    else:
        print("Oh no ! The letter {} is not part of secret word".format(guess))
        remaining_attempts -= 1
    os.system("clear")
    print(hangman_stages.get_hangman_stage(remaining_attempts))
    print("\n{} attempts remaining\n".format(remaining_attempts))
    print_secret_word(secret_word, guessed_letters)
    print("\n\nNumber of letters guessed: {}\n".format(len(guessed_letters)))
if len(guessed_letters) == len(get_unique_letters(secret_word)):
    print("Congratulations!!! You won...")
    input("Press enter to continue")
else:
    print("You are lose ")
    input("Press ENTER to continue ")

