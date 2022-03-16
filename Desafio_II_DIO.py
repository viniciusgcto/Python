from random import random

counter = 0
for x in range(6):
    number = random()
    if number > 0:
      counter += 1
       
print(counter,"Valores positivos")