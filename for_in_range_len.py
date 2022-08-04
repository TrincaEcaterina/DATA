
from operator import index
import random
# Task 1: Fill up a list with numbers like 100,200,....,900

#numbers=[]
#for n in range(-50, 51):
# numbers.append(n)

# FILL SHORTHAND

# numbers = [ n for n in range(1,10)]
numbers=[random.randint(-50, 51) for n in range(0,10)]


# Task 2: using the loop print the list

for i in range(1,10):
    print (i,numbers[i])

#HW: modify the code to fill the list with 9 random values in the range [-50,50]