# Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible by 7
# but not a multiple of 5, and store them in a separate list. Finally, print the list.
# Constraint: use only while loop for iteration

list_one_to_hundred = list(range(1, 101))
final_list = []

counter = 0
while counter != 100:
    if list_one_to_hundred[counter] % 7 == 0 and list_one_to_hundred[counter] % 5 != 0:
        final_list.append(list_one_to_hundred[counter])
    counter += 1

print(final_list)
