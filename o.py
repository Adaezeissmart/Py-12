class Cat:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info (self):
        print(f"I am a cat and my name is {self.name}. I am {self.age}years old.")
    def make_sound(self):
        print("Meow Meow")

class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f"I am a dog my name is {self.name}. I am {self.age}years in dog years")
    def make_sound(self):
        print("Woof Bark")
cat1 = Cat("Oreo", 3)
dog1 = Dog("Hulk", 9)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()