# Single Inheritance
class Food():
    def __init__(self,price):
        self.price = price
    def show_price(self):
        print(f"Price is: Rs.{self.price}")
        
class Pizza(Food):
    def add_toppings(self):
        print("Extra cheese and jalapenos added.")
        
# Multilevel Inheritance
class Dessert(Food):
    def taste(self):
        print("This food tastes very sweet.")
        
class Icecream(Dessert):
    def freeze(self):
        print("Keep it in the freezer so it does not melt.")

# Multiple Inheritance
class BakeryItem:
    def bake(self):
        print("Baking inside a hot oven.")
        
class SweetItem:
    def add_sugar(self):
        print("Adding white sugar.")
        
class Cake(BakeryItem, SweetItem):
    def decorate(self):
        print("Adding chocolate on top.")

print("\n=== Restaurant Menu ===")
p = Pizza(299)
p.show_price()
p.add_toppings()

ic = Icecream(99)
ic.show_price()
ic.taste()
ic.freeze()

c = Cake()
c.bake()
c.add_sugar()
c.decorate()