#TODO: Catch the exception and make sure the code runs without crashing.

fruits = ["Apple", "Pear", "Orange"]

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("No such index exist.")
    else:
        print(fruit + " pie")

make_pie(4)