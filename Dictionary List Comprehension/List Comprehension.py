# List Comprehension:
# new_list = [(expression) for item in items]

# Method 1; Ordinary methid ->
numbers = [1, 2, 3, 4]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)
print(new_list)
    
# Method 2: The above task is performed using list Comprehension:
numbers = [1, 2, 3, 4]
new_list = [n + 1 for n in numbers] # List Comprehension.
print(new_list)

# Write a program in python to calculate the sqaure of each number present in the list:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square_list = [n * n for n in numbers]  # Each element i.e., n is doubled and stored inside another list named, square_list.
print(square_list)
# OR
print([n * n for n in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])

# Copying list:
import copy
l1 = [1, 2, 3, 4]
l2 = copy.copy(l1)
l1[1] = 10
print(l1)
print(l2)

# Increasing character by 1 using ord() and chr() method.
# ord() return the correspoding ASCII value of the character and after adding integer to it, chr() again converts it into character.
a = 'A'
print(chr(ord(a)+1))

# Using String:
# Converting string to list:
name = "Koushik Sadhu"
new_list = [letter for letter in name]
print(new_list)    # Each individual letters will be stored in the list named as, new_list.

# Converting list to string:
a = str(new_list)
s = ""
for each in new_list:
    s += each
print(s)

# List comprehension using range() function:
new_list = [i * 2 for i in range(1, 5)]
print(new_list)