# Dictionary Comprehension:
# new_dictionary = {new_key : new_value for item in items}  # Curly braces is used in the case of Dictionary.
# OR
# new_dictionary = {new_key : new_value for (key, value) in dict.items()}  # Looping through each of the keys and values in all of the items of the dictionary.
# OR
# new_dictionary = {new_key : new_value for item in items}  # Conditional Checking.
# new_dictionary = {new_key : new_value for (key, value) in dict.items() if (condition)}   # Conditional Checking.

dict = {"Koushik" : 1, "Koushik" : 2, "Koushik" : 3, "Koushik" : 4}
print(dict)             # If all the keys are same then the last key value pairs will only get printed. So, In dictionary keys must be unique.
print(dict["Koushik"])  # We can fetch the value by using dictionary_name and passing the key inside a square bracket.


# Generate a random score of each of the names of a list and store the name and score as a (key, value) pairs inside a dictionary.
import random
names = ["Koushik", "Shuvam", "Pranay", "Anmol", "Udayan", "Adarsh"]
name_score_dict = {name : random.randint(1, 100) for name in names}
print(name_score_dict)


# Create one dictionary and store the name and score of the student whose has passed the exam:
passed_dict = {name : score for (name, score) in name_score_dict.items() if score >= 50}    # items() function is a set-like object providing a view on Dictionaries items
print(passed_dict)

# You are going to use dictionary comprehension to create a dictionary called result that takes each word in the given sentence and calculates the number of letter in each words.
sentence = "What is the Airspeed Velocity of an Unladden Swallow ?"
# sentence_to_list = sentence.split()     # By defaault, the parameter passed is (" ")in the split method.
# print(sentence_to_list)
word_length_dict = {word : len(word) for word in sentence.split()}
print(word_length_dict)

# You are going to use Dictionary Comprehension to create a Dictionary called weather_f that take each temperature in degree celsius and convert it into degree fahrenheit.
weather_c = {
    "Monday" : 12,
    "Tuesday" : 14,
    "Wednesday" : 15,
    "Thursday" : 14,
    "Friday" : 21,
    "Saturday" : 22,
    "Sunday" : 24
}
weather_f = {day : (temp_in_c * 9 / 5) + 32 for (day, temp_in_c) in weather_c.items()}
print(weather_f)

