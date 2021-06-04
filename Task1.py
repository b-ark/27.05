# Write a Python program to get the largest number from a list of random numbers with the length of 10
# Constraints: use only while loop and random module to generate numbers

from random import randint

random_list = []

counter = 0
while counter != 10:
    random_list += [randint(0, 10)]
    counter += 1

print(random_list)
max_number = max(random_list)
print('Largest number is ', max_number)
