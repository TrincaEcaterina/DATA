### one dimensional array find maxium

from random import randint
import random


data = [1,5,0,10,15,0,15]
# maximal = max (data)
#print (maximal)
maximal = data[0]
for i in range(len(data)):
    if data[i] > maximal:
        maximal = data[i]
print(maximal)

minimal = data[1]
for i in range(len(data)):
    if data[i] < minimal:
        minimal = data[i]
print(minimal)

data_value=random.randrange(len(data))
print(data[data_value])
# HW: find minimal
# HW: check if the value exist 
# HW: choice one value random
