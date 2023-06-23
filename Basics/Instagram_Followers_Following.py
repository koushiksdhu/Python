class User:
    def __init__(self, user_id, username): # Parameterized Constructor
        self.id = user_id
        self.name = username
        self.followers = 0
        self.following = 0
    
    # Adding method to a class
    def follow(self, user):
        user.followers += 1
        self.following += 1
        print("You started following", user.name)

acc1 = User("koushiksdhu", "Koushik Sadhu")
acc2 = User("shuvamchodhury", "Shuvam Chodhury")
print("User ID: ",acc1.id)
print("User Name: ", acc1.name)
print("Followers: ", acc1.followers)
print("Following: ",acc1.following)
acc1.follow(acc2)
print("User ID: ",acc1.id)
print("User Name: ", acc1.name)
print("Followers: ", acc1.followers)
print("Following: ",acc1.following)

print("User ID: ",acc2.id)
print("User Name: ", acc2.name)
print("Followers: ", acc2.followers)
print("Following: ",acc2.following)
acc2.follow(acc1);
print("User ID: ",acc2.id)
print("User Name: ", acc2.name)
print("Followers: ", acc2.followers)
print("Following: ",acc2.following)
print('\n')
print('\n')
