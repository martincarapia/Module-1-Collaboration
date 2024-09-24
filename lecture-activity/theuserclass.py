"""
Create a program that Makes a class called User.
Create two attributes called first_name and last_name, and then
Create several other attributes that are typically stored in a user profile.
Make a method called describe_user() that prints a summary of the user’s information.
Make another method called greet_user() that prints a personalized greeting to the user.
Create fivel instances representing different users, and call both methods for each user
"""

class User():

    def __init__(self, first_name: str = "John", last_name: str = "Doe", age: int = "20", height_in_centimeters: float = "180.2") -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height_in_centimeters = height_in_centimeters

    def describe_user(self) -> None:
        print(
            f"{self.first_name} {self.last_name} aged {self.age} years old and standing at {self.height_in_centimeters} cm" 
        )
    
    def greet_user(self) -> None:
        print(f"Hello {self.first_name} {self.last_name}. How are you today? I hope you're doing great")

myuser = User("Martin", "Carapia", 18, 180.2)
aung_user = User("Aung", "Aung", 16, 175)
jacksan_user = User("Jack", "Ball", 17, 190)
logan_user = User("Logan", "Ghast", 13, 100)
obeth_user = User("Obeth", "Cruz", 30, 200)

myuser.describe_user()
myuser.greet_user()

aung_user.describe_user()
aung_user.greet_user()

jacksan_user.describe_user()
jacksan_user.greet_user()

logan_user.describe_user()
logan_user.greet_user()

obeth_user.describe_user()
obeth_user.greet_user()

