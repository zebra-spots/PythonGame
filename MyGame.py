#! /usr/bin/python
# Name: MyGame.py
# Author: Chris
# Revision v1.0
# Description: This is a game program.
"""
    Docstring: Use to play games. Import rock paper scissors game.
    TODO: create and import more games
"""
import sys
from rockpaperscissors import *
from hangman import *
from dice import *


def main():
    """ Call games here """
    while True:

        print("Which game?\n"
              "1: Rock paper scissors\n"
              "2: Hangman\n"
              "3: Dice\n"
              "q: Quit\n")
        userchoice = input("Make a choice: ")

        if userchoice == "1":

            while True:
                print(play())
                userin = input("\nPress q to quit, Or press any key to play again ")
                if userin.lower() == "q":
                    print("Quitting.......\n")
                    break

        elif userchoice == "2":
            print(playhangman())

        elif userchoice == "3":
            print(diceplay())

        else:
            print("Quitting.......")
            return 0




if __name__ == "__main__":
    main()
    sys.exit(0)
