import random


def diceplay():
    minimum = 1
    maximum = 6

    roll_again = "yes"

    while roll_again == "yes" or roll_again == "y":
        print("Rolling the dice...")
        print("The values are....")
        print(random.randint(minimum, maximum))
        print(random.randint(minimum, maximum))

        roll_again = input("\nPress y to roll the dice again, press any other key to quit \n").lower()
