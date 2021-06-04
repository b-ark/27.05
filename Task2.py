# Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list containing the common
# integers between the 2 initial lists without any duplicates.
# Constraints: use only while loop and random module to generate numbers

from random import randint

random_list_1 = []
random_list_2 = []

counter = 0
while counter != 10:
    random_list_1 += [randint(0, 10)]
    random_list_2 += [randint(0, 10)]
    counter += 1

final_list = list(set(random_list_1) & set(random_list_2))

print(f'Common between {random_list_1} and {random_list_2} ---> {final_list}')
