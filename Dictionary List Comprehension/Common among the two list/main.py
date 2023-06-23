# Method 1: Brute Force.Method.
# Opening file1.txt and Reading and then storing it inside a list1.
with open("Dictionary List Comprehension\\\Common among the two list\\file1.txt") as file1:
    data1 = file1.read()
list1 = [int(i) for i in data1 if not i.__eq__("\n")]
print("List 1",list1)

# Opening file2.txt and reading and then storing it inside a list2.
with open("Dictionary List Comprehension\\\Common among the two list\\file2.txt") as file2:
    data2 = file2.read()
list_2 = [int(i) for i in data2 if not i.__eq__("\n")]
print("List 2:",list_2)

# Taking out the common element from both the list using list comprehension:
list_common = [element for element in list1 if element in list_2]
print("Common List:",list_common)



# Method 2: Optimized Method.
with open("Dictionary List Comprehension\\\Common among the two list\\file1.txt") as file1:
    data1 = file1.readlines()
with open("Dictionary List Comprehension\\\Common among the two list\\file2.txt") as file2:
    data2 = file2.read()
list_common = [int(element) for element in data1 if element in data2]
print("Common List:",list_common)