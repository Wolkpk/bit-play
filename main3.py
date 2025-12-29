import numpy as np

# create 6 sided "die"
die_sides = int(input("Enter number of sides for dice (6/12): "))
die = range(1, die_sides + 1)

# set number of rolls
num_rolls = int(input("Enter number of times you want to roll the dice: "))

# roll the die the set amount of times
results = np.random.choice(die, size=num_rolls, replace=True)
print(results)
