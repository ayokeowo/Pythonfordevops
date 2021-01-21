#Rooll two six-sided dice, each with faces containing 1 to 6 spots
#Calculate the sume of the spots on the two upward faces
#


import random

def roll_dice ():
    """
    Roll two dice and return their face values as a tuple
    """
    die1 = random.randrange(1,7)
    die2 = random.randrange(1,7)
    sums = die1 + die2

    return (die1, die2, sums)

die_values = roll_dice()

print (die_values)



