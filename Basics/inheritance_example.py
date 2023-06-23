class Animal:
    def __init__(self):     # __init__() method let's the class initialize the object attributes amd serves for other purpose. It is same as constructor in other object oriented programming languages.
        self.num_of_eyes = 2
        print("No. of eyes:", self.num_of_eyes)

# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
        
    def breathe(self):
        print("(Inhale, Exhale)", end = " ")
        
class Fish(Animal):             # class Fish inheriting from Animal class.
    def __init__(self):         # Default constructor of the current class.
        super().__init__()      # calling parent class constructor using super() keyworrd.
        
    def breathe(self):          # Method Overriding.
        super().breathe()       # calling parent class breathe method using super keyword.
        print("Breathing under water")
        
    def swim(self):
        print("Moving in water.")    
        
# Creating object of the above class Fish.

illish = Fish()                # Creating object of the class Fish (Which is inheriting from Animal class).
illish.breathe()                # Calling parent class method from child class object (because child class is inherited from the parent class).
illish.swim()                   # Calling same class method.


