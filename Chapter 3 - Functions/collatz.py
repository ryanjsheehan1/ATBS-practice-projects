"""Collatz Sequence Program
The Collatz conjecture is one of the most famous unsolved problems in mathematics. The conjecture asks whether repeating
 two simple arithmetic operations will eventually transform every positive integer into 1. It concerns sequences of
 integers in which each term is obtained from the previous term as follows: if the previous term is even, the next term
 is one half of the previous term. If the previous term is odd, the next term is 3 times the previous term plus 1. The
 conjecture is that these sequences always reach 1, no matter which positive integer is chosen to start the sequence.
 Source: https://en.wikipedia.org/wiki/Collatz_conjecture
"""

# Number of steps for Collatz sequence to complete
steps = 0


def collatz(number):
    """Performs Collatz sequence on input number recursively until it reaches 1"""
    global steps
    if number == 1:
        print('Collatz Complete in %d steps' % steps)
    elif number % 2 == 0:
        print(int(number // 2))
        steps += 1
        collatz(number // 2)
    else:
        print(int(number * 3 + 1))
        steps += 1
        collatz(number * 3 + 1)


# User input
try:
    collatz(int(input('Choose any integer greater than 1: ')))
except ValueError:
    print('Non-Integer entered, program will exit')

