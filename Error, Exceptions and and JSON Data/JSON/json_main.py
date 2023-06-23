# ------------------------------------------------ NOTES -----------------------------------------------------------------

# JSON means Java Script Object Notation.
# JSON is used to store a data in a much fancier format.
# This is something that is designed specially for JavaScript.
# Because, It has such a simple structure and is so easy to understand and work with so, that it has been adopted by many different fields including python.
# This is one of the most popular way for transfering data, especially when you're transferring data over the Internet.
# JSON is similar to more alike DICTIONARY in python.
# JSON is mainly composed of a bunch of NESTED lISTS and DICTIONARY and it is having a KEY-VALUE pair.

# To work with JSON Data in Python, We use the inbuilt JSON Library. The mainly use json functions are:
# Write: json.dump()
# Read: json.load()
# Update: json.update()

# json.dump() and json.load() is used to SERIALIZE and DESERIALIZE JSON data to PYTHON DICTIONARIES and vice versa and allows us the free interchange of information.

# json.update() function is having 3 step approach:
# 1. Opening the JSON file in Read mode.
# 2. Reading the old data.
# 3. Updating old data with new data.
# 4. Opening tyhe JSON file in Write mode. 
# 5. Dumping the updated data.

# -------------------------------------------------- PRACTICAL ------------------------------------------------------------

import json

write_dict = {
    "MyData1" : {
    "Name" : "Koushik Sadhu",
    "Department" : "Information Technology",
    "Address" : "Kolkata, India",
    "Email" : "kkoushikssadhu@gmail.com",
    "Contact Number" : 7992321676
    }
}

new_data = {
    "MyData2" : {
    "Name" : "Pranay Gupta",
    "Department" : "Information Technology",
    "Address" : "Kolkata, India",
    "Email" : "pranayguptamain@gmail.com",
    "Contact Number" : 9874563210
    }
}


# Writing data in JSON file:
with open("data.json", 'w') as f:       # if we don't want to overwrite the data all the time then we may open the file in append mode or we can also use json.update() function.
    json.dump(write_dict, f, indent = 4)      # dictionary_name and data_file_name is passed as a parameter inside json.dump() function.
    
# Loading Data from JSON file:
with open('data.json', 'r') as f:
    load_dict = json.load(f)        # returns dictionary.
    print(load_dict)

# Updating the data:
with open('data.json', 'r') as f:
    data = json.load(f)             # Reading the data.
    data.update(new_data)           # Updating the old data with new data.
    with open('data.json', 'w') as f:   # Opening the JSON file in write mode.
        json.dump(data, f, indent = 4)   # Dumping the updated data.
      
