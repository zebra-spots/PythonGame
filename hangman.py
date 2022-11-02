#! /usr/bin/python
# Name: hangman.py
# Author: Chris
# Revision v1.0
# Description: This is a hangman game.

import random


def playhangman():
	playername = input("What is your name? ")

	words = '''Aragorn Arwen Bilbo Balin Boromir Denethor Elrond Eomer Eowyn Faramir Frodo \
	Galadriel Gandalf Gimli Gollum Isildur Legolas Merry Pippin Sam Saruman Sauron Shelob Treebeard Wormtongue'''
	words = words.split(' ')

	word = random.choice(words)

	guesses_allowed = 6
	guesses = []
	done = False

	print("Hello", playername, "welcome to hangman")
	print("Guess the Lord of the Rings charachter!")

	while not done:
		for letter in word:
			if letter.lower() in guesses:
				print(letter, end="")
			else:
				print("_", end=" ")
		print("\n")
		print(guesses)
		print("")

		guess = input(f"Remaining Lives {guesses_allowed}, Next Guess:")
		guesses.append(guess.lower())

		if not guess.isalpha():
			print("Only enter letters")
			continue
		elif len(guess) > 1:
			print("Only enter a single letter")
			continue

		if guess.lower() not in word.lower():
			guesses_allowed -= 1
			if guesses_allowed == 0:
				break

		done = True
		for letter in word:
			if letter.lower() not in guesses:
				done = False

	if done:
		print("Well done", playername, "You correctly guessed", word,"\n")

	else:
		print("Game over! Unlucky", playername, "The word was:", word,"\n")
