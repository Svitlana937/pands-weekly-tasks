# This program prints out a random fruit
import random
fruits = ('Apple', 'Orange', 'Banana', 'Pear')
# we want a random number of fruit to be chosen between 0 and length of the list - 1
index = random.randint(0, len(fruits) - 1)
fruit = fruits[index]
print("A random fruit: {}".format(fruit))