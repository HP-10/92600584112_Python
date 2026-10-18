class A:
    def show(self):
        print("From Class A.")

class B:
    def show(self):
        print("From Class B.")

class C(A,B):
    pass

obj = C()
print("== Method Resolution Order ==")
obj.show()

class point:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y

    def __sub__(self, U):
        return self.X - U.X, self.Y - U.Y

obj_1 = point(50,30)
obj_2 = point(20,10)

obj_3 = obj_1 - obj_2
print("== Magic Method ==")
print(obj_3)