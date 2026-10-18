class Animal:
    def speak(self):
        print("Animal makes some sound.")

class Dog(Animal):
    def speak(self):
        print("Woof! Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow! Meow!")

print("== Method Overriding ==")
dog = Dog()
dog.speak()

cat = Cat()
cat.speak()