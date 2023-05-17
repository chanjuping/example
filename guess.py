#!/usr/bin/env python

import random

def main():
    """Start a number guessing game between 1 - 100."""
    print("Guess the number!")

    x = random.uniform(10, 100)
    guess = None
    print(x)

    while x != guess:

        guess = int(input("Pick a number between 1 to 100: "))

        if x == guess:
            print("You cheated!")
        else:
            print("HAHAHAHAHAHA LMAO.")

main()