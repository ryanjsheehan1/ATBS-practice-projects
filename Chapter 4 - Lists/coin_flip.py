"""Coin Flip Streaks
Runs n = 10,000 simulations of flipping a coin 100 times. Prints
percentage chance of 100 coin flips containing a streak of six heads
or tails in a row for all simulations.
"""

import random

number_of_streaks = 0

# Simulations where n = 10,000
for experiments in range(10000):

    coin_flips = []

    # Flips a coin 100 times
    for flips in range(100):
        coin_flips.append(random.randint(0, 1))

    streak = 0

    # Counts streaks of head or tails
    for i in range(len(coin_flips)):
        if i == 0:
            pass
        elif coin_flips[i] == coin_flips[i-1]:
            streak += 1
        else:
            streak = 0

        if streak == 6:
            number_of_streaks += 1
            break

print('Chance of streak: %s%%' % (number_of_streaks / 10000 * 100))
