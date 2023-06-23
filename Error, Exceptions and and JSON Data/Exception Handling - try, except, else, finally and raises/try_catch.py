# HANDLING EXCEPTIONS

# ---------------------------------------------- NOTES -----------------------------------------------------------

# If you don't have any file in your file and you're trying to open that file. Then what you think, What will happen ?
# A FileNotFound error will be thrown and program will get terminated, as no such file or directory exist inside the folder and after that line no code is been executed.
# To avoid the program termination when such situation arises, Try and Catch comes into existence.
# A try-catch block is used to mitigate errors in code and prevent program crashing during runtime.
# It 'tries' a block of code that could give an error.
# If the error (exception) is raised, it will execute a different block of code rather than crash the program. 

# Types of error:

# KeyError: If in Dictionary there is only one key-value pair and we are trying to access the key which is not present in that dictionary, then it will throw this erroe.
# IndexError: If we are having a listof n items and we are trying to access the index which is greater than n. Then this error is being thrown.
# TypeError: This type of error is thrown due to type mismatch, Like, if we are concatenating string with an integer than this type of error is being thrown.
# FileNotFoundError: If the file which we are trying to read does not exist in the folder.
# ValueError: If there is any Error in value.
# IndexError: When that index does not exist.

# In programming we basically catch this exceptions so that it doesn't have to fail catastrophically.

# There are mainly four keywords used for Handling exceptions: try, except, else, finally, raise.

# try: It contains the block of code in which you're thinking that error may be thrown or might cause an exception.
# except: This block of code gets executed when the error is being thrown by the try block. Executed in case of exception/error only.
# else: This block of code gets executed when no error is being thrown or If there were no exceptions.
# finally: This block gets executed irrespective of error. It means this block will always get executed no matter if there is an exception or not.
# raise: This keyword is used to raise a own exception.

# with open("Data.txt", "r") as filename:
#     str = filename.read()   # will throw FileNotFound error.
    
try:                                # try block.
    f = open("Data.txt", "r")
except:                             # catch block.
    print("There was an error.")    # It is pointless to print this line. Instead, open a file in write mode so that if that file doesn't exist exist than new file will be created.
    f = open("Data.txt", "w")       # opening file in write mode.
    
# Using except clasuse, If there is more than one error in a try block then only the first exception will be thrown and the second exception will not be checked.

# To catch a specific exception you need to mention the error explicitly, like:
try:                                                                        # try block
    f = open("Data.txt", 'r')
    dict = {1:"Me"}
    print(dict[2])

except KeyError as error_message:        # Mentioning the KeyError explicitly.               # except block which is same as catch block.        
    print(f"No such key named {error_message} exist in the dictionary.\n")

except FileNotFoundError as error_message:        # Mentioning the FileNotFoundError explicitly.        
    print("No such file exists.\n")
    
else:                                                                       # else block
    # This block gets triggered if not a single exceptions is being thrown. If a single exception gets thrown then this else block will not get triggered.
    # Just assumne except as if block and else as else block. If except block(which we can say it if block for understanding purpose) gets triggered than else block will not get triggered.and vice-versa.
    content = f.read()
    print(content)
    
finally:            # It will get executed irrespective of any error being thrown.
    # f.close()       # Closing the file.
    # print("File was Closed.")
    # raise TypeError                                     # Raising Exception by writing the name of the error.
    raise FileNotFoundError("This is an error that I made up.")      # Raising Exception with message.
    
    

    

    
