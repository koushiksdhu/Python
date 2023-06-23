import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
dict = {row.letter : row.code for(index, row) in data.iterrows()}   # Coverting DataFrame to Dictionary.

def gen_phonetic():
    word = input("Enter the word: ").upper()    # Taking input from the user and storing it inside variable name, word.
    
    try:
        # Accessing the value using the key.
        code_list = [dict[letter] for letter in word]       # IF the letter does not match with the dictionary key then exception is being handled.

    except KeyError:
        print("Invalid Name. Please Enter a Valid Name.\n")
        gen_phonetic()

    else:  
        print(code_list)

# OR

# # Directly using pandas DataFrame and accesing the data using DataFrame inbuilt iterator method -> iterrows().
# code_list = [row.code for l in word for (index, row) in data.iterrows() if l == row.letter] # iterrows() is used in DataFrame to iterate through each rows in proper format.
# # index and rows should always be used In case if we user iterrows() iterator method.
# print(code_list)

gen_phonetic()

