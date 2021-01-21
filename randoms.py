
#Question: Write a conditional expression to simulate 20 coin flips, displaying H for heads and T for tails all on the same line, each separated by a space.

import random

#My own code
for x in range(0,20):
    rand = random.randrange(0,2)
    if rand == 1:
        print ('H', end=' ')
    else:
        print ('T', end=' ')

#Teacher's code
for i in range(20):
    print('H' if random.randrange(2) == 0 else 'T',end=' ')