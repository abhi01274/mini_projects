# Hangman Letter Game App

"""
Challenge 1

    We are going to make a "Hangman Letter" game 
    The computer will pick a word
    The player can guess it letter by letter or run out of chances.
    But if they make too many wrong guesses, they loose.
    If the player makes the right guesses he wins
    Cleaner interface and option to quit the game

Hint 1

    Step 1: Make a list of words, may be Fruits or vegetables 
    Step 2: Pick a random word from the list
    Step 3: Get a guess from the player 
    Step 4: Compare the guess to the secret number
    Step 5: If the player guesses the right number print player wins and computer lose.
    Step 6: If the player guesses the wrong number print player lose and computer wins.

Algorithm

    # import external libraries
    # make a list of word

    # pick a random word

    # draw  spaces
    # take guess
    # draw guessed letters, spaces and strikes
    # print out win / lose

"""
# import external libraries
import random 

# make a list if word
words = ['apple','banana','orange','coconut','strawberry','lime','grapefruit','lemon','kumquat','blueberry','melon']

while True:

    start = input("Press enter / return to start, or enter Q to quit")

    if start.lower() == 'q':
        break

# pick a random word
    secret_word = random.choice(words)
    bad_guesses = []
    good_guesses = []

    while len(bad_guesses) < 7 and len(good_guesses) != len (list( secret_word)):
        # draw  spaces
        # draw guessed letters, spaces and strikes
        for letter in secret_word:
            if letter in good_guesses:
                print ( letter , end='')
            else:
                print('_', end='')
                print ('')

        print('Strikes : {} / 7'.format(len(bad_guesses)))
        print ('')

        # take guess
        guess = input ("Guess a letter : ").lower()

        # draw guessed letters and strikes
        if  len(guess) != 1:
            print ("You can only guess a single letter !") 
            continue
        elif guess in bad_guesses or guess in good_guesses:
            print("You have already guess that letter")
            continue
        elif not guess.isalpha():
            print ("You can only guess letters !")
            continue
        # print out win / lose

        if guess in secret_word:
            good_guesses.append(guess)

        if len (good_guesses) == len ( list(secret_word)):
            print ("You win : The word was {}". format(secret_word))
            break
        else:
            bad_guesses.append(guess)
    
    else:   # else for the while 
        print ("You didn't guess it: my secret word was {}". format(secret_word))



"""
Challenge 2
    Screen is messy and rolls ups
    Convert the code into function 

    MAJOR REFACTORING OF THE CODE
"""

import os
import random 
import sys

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def draw(bad_guesses, good_guesses, secret_word):
    clear()
    print('Strikes : {} / 7'.format(len(bad_guesses)))

    print ('')

    for letter in bad_guesses :
        print(letter, end = ' ')
        print("\n\n")

    for letter in secret_word:
        if letter in good_guesses:
            print ( letter , end='')
        else:
            print('_', end='')
            print ('')


def get_guess(bad_guesses,good_guesses):
    while True:
        # take guess
        guess = input ("Guess a letter : ").lower()
        # draw guessed letters and strikes
        if  len(guess) != 1:
            print ("You can only guess a single letter ") 
            continue
        elif guess in bad_guesses or guess in good_guesses:
            print("You have already guess that letter")
            continue
        elif not guess.isalpha():
            print ("You can only guess letters !")
            continue
        else:
            return guess




def play ( done ):
    secret_word = random.choice(words)
    bad_guesses = []
    good_guesses = []

    while True:
        draw(bad_guesses, good_guesses, secret_word)
        guess = get_guess ( bad_guesses, good_guesses)

    if guess in secret_word:
        good_guesses .append(guess)
        found = True 
        for letter in secret_word:
            if letter not in good_guesses:
                found = False
                if found :
                    print ( "You win")
                    print("The secret word was {}".format(secret_word))
                    done= True
                else:
                    bad_guesses.append(guess)
                    if len(bad_guesses) == 1:
                        draw (bad_guesses, good_guesses, secret_word)
                        print ( "You Lost")
                        print ("The secret word was {}".format(secret_word))
                        done = True
                        if done:
                            play_again = input("Play again ? Y/n ").lower()
                        if play_again != 'n' :
                            return play(done=False)
                        else:
                            sys.exit()

def welcome():
    start = input("Press enter / return to start, or enter Q to quit")
    if start.lower() == 'q' :
        print("Bye")
        sys.exit()
    else:
        return True
        
    
print ( "Welcome to letter Guesses !")
done = False
while True:
    clear()
    welcome()
    play(done)



"""
Challenge 3
Read the words from a file

"""
with open('words.txt') as f:
    words = f.read().splitlines()





"""
Challenge 4
    Get the list of Internet after web scrapping
"""
