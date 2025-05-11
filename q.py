class Hamster:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info (self):
        print(f"I am a hamster and my name is {self.name}. I am {self.age}years old.")
    def make_sound(self):
        print("Squeak Squeak")

class Snake:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f"I am a snake my name is {self.name}. I am {self.age}years in snake years")
    def make_sound(self):
        print("Hiss Hiss")
hamster1 = Hamster("Oreo", 3)
snake1 = Snake("Hulk", 9)

for animal in (hamster1, snake1):
    animal.make_sound()
    animal.info()