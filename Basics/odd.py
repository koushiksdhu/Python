# Write a program in python to find the greatest number.
a = int(input("Enter the first number: "))
b = int(input("Enter the first number: "))
c = int(input("Enter the first number: "))
if (a>b) and (a>c):
    print(a, " is greatest.")
elif (b>c):
    print(b, " is greatest.")
else:
    print(c, " is greatest.")
    
