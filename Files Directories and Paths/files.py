# # Modes:
#     # -> read only = 'r'    : This mode is used to read the file.
#     # -> both read and write = 'r+' -> The r+ helps you read and write data onto an already existing file without truncating (Error if there is no such file). 
#     # -> write only = 'w' : This mode will delete the previous text and write the current text over it.
#     # -> both write and read = 'w+' -> The w+ mode on the other hand also allows reading and writing but it truncates the file (if no such file exists - a new file is created).
#     # -> append = 'a'   : This mode will append the current text with the previous text.
#     # -> append = 'a+'   : Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.




# # READING FILE:

# # Method 1: Opening the file -> Reading/Writing -> Closing the file:
# file = open("my_file.txt")       # Opening the file...(this file is only readable).
# contents = file.read()                   # Reading the file and storing it in the variable named content.
# print(contents)                          # Printing the content of the file in the console.
# file.close()                    # Closing the file ro reduce the burden.

# # Method 2: Automatically closing:
# with open("my_file.txt") as file:   # Opening the file...(this file is only readable).
#     contents = file.read()      # Reading the file and storing it in the variable named content.
#     print(contents)
# # It will automatically close down the file when the indent on the next line does not match.




# # WRITING FILE: Replacing the previous text.

# #with open("my_file.txt") as file:   # Opening the file...(this file is only readable). because the file is by default opened in read only mode.
#     #file.write("New Text.")
# # --> The above code will throw an error because by default, the file is opened in read only mode.

# with open("my_file.txt", mode = "w") as file:   # Opening the file in Write only mode.
#     file.write("This is the new text.")     # After executing this, all the previous text will be replaced by current passed text.
# # -> If the file is opened in write only mode then, it can't be read and vice-versa.
# # -> When we open a file in Write "w" mode and the file does not exist then it creates a new file.




# # WRITING FILE: appending the current text with the previous text.

# with open("my_file.txt", mode = "a") as file: # Opening the file in append mode.
#     file.write("\nThis is the appended text.")  # After executing this, current text will get appended with the previous text.

# with open("my_file.txt", mode = "w") as file: # Opening the file in append mode
#     file.write("105001452")
  

with open("my_file.txt", mode = "r") as file: # Opening the file in append mode
    data = file.read()
    print(type(data))
    print(data)
    
    
    
# ABSOLUTE FILE PATH: 

#   / -> Root(origin) : In Mac.
#   C:\ -> Root(origin) : In Windows toot folder is usually C drive or the drive in which Windows is being installed.
#   Absolute path name represents the complete name of a directory or file from the /(root or origin of the computer storage) directory downward.
#           Example: C:\Users\kkous\Desktop\Koushik.txt
#   Absolute file path always starts from the root.

# RELATIVE FILE PATH:

#   Relative path is defined as the path related to the present working directly or current working directly(PWD or CWD).
#   Relative paths make use of two special symbols:
#   A dot (.) and a double-dot (..)
#   Single dot(.) translate into the current directory and the parent directory.
#   Double dots are used for moving up in the hierarchy.
#   The directory where, we are currently working from is called Working Directory.
#   ./ signifies look in the current folder. (We can also write only the file name without writing ./)
#   ../ signifies come out of the current folder or one step back.
#   In MacOS, each of the path is seperated by forward slash /
#   In WindowsOS, each of the path is seperated by back slash \
#   But in python, either of the two can be used. 

# Return all lines in the file, as a list where each line is an item in the list object:
with open("my_file.txt") as file:
    print(file.readlines())     #The readlines() method returns a list containing each line in the file as a list item.
    
# Replacing Words:
txt = "I like Bananas."
revised_txt = txt.replace("Bananas", "Apples")
print(txt,"\n",revised_txt)

# Strip(): The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters.
txt = "      Banana     is delicious.            "
stripped_txt = txt.strip()  # Space is the default leading character to remove.
print(txt,"\n",stripped_txt)

        

    
    
    



