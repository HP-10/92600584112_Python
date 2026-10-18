from abc import ABC, abstractmethod

class Shape():
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drwaing a Circle.")

class Wallet:
    def __init__(self, money):
        self.__money = money

    def get_money(self):
        print(self.__money)

c=Circle()
print("== Abstraction ==")
c.draw()

w=Wallet(5000)
print("== Encapsulation ==")
w.get_money()