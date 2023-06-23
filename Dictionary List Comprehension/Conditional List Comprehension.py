# Conditional List Comprehension
# new_list = [(expression) for each_item in list if (expression)]

# Square the element :
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [(num ** 2) for num in numbers if (num % 2 == 0)]    # (num ** 2) is same as (num * num).
print(even_numbers)
odd_numbers = [(num * num) for num in numbers if (num % 2 != 0)]
print(odd_numbers)

# Print the name whose length is 4 or less than 4:
names = ["Kous", "Soub", "Tapa", "Purn", "Tapas", "Purnima", "Koushik", "Soubhik"]
names_of_length_4 = [name for name in names if len(name) <= 4]
print(names_of_length_4)

# Convert the name to the upper case whose length is greater than 4:
names = ["Kous", "Soub", "Tapa", "Purn", "Tapas", "Purnima", "Koushik", "Soubhik"]
upper_names = [name.upper() for name in names if len(name) > 4]
print(upper_names)