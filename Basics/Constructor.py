


class User:
    #pass # Pass is used as a placeholder for future code. It is used when developer is unsure what code to provide.
   """ def __init__(self):
        print("New Object is created")


User1 = User()"""

"""User1.roll = 10800220027
#User1.name = "Koushik Sadhu"
#print(User1.name,"\n", User1.roll, sep = "")"""

"""User2 = User()"""

# Parameterized Constructor 
class User:
    def __init__(self, name, roll):
        self.name = name;
        self.roll = roll;
        
student1 = User('Koushik', 10800220027)
print(student1.name)
print(student1.roll)
print('\n')

# Default Value without passing in constructor




    
