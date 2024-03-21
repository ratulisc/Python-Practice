"""
Build a number guessing game
"""

import random


def Guessing_Number():
    Guessed_number = random.randint(1, 50)
    turn = 0
    while True:
        guess = int(input("Enter your guessed number: "))
        turn += 1
        if guess > Guessed_number:
            print("Its very high.")
        elif guess < Guessed_number:
            print("Its too low.")
        else:
            print("You have guessed the number")
            break


Guessing_Number()
