#! /usr/bin/python
# Name: numberguessing.py
# Author: Chris
# Revision v1.0
# Description: This program .

import random


def guessplay():
    num = random.randint(1, 20)

    while True:

        userguess = input("Guess a number between 1 and 20: ")
        print(f"Guess: {userguess}")

        if userguess.isdigit():
            usernumber = int(userguess)

            if usernumber == num:
                print("\nMatch!")
                print(f"Well done, you correctly guessed {num}")
                break

            elif usernumber < num:
                print("Higher")

            else:
                print("lower")

        else:
            print("Choose a number")
            continue
