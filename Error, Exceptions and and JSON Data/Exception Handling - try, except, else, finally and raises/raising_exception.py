# Write a program to calculate BMI index.
# If the height is more than 3 then raise a ValueError with message "Human height should not be over 3 meters"

height = int(input("Enter the Height (in meter): "))
weight = int(input("Enter the Weight (in kgs): "))

if height == 0:
    raise ValueError("Invalid Height. Please Enter Valid Height.")
elif height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / (height ** 2)

print("BMI: %.2f" %bmi)

