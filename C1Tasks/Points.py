class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y 

    def __str__(self):
        return f'Dot: {self.x, self.y}'        

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b

    def __eq__ (self, others):
        return self.a == others.a and self.b == others.b

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def square(self):
        return 3.14 * (self.radius ** 2)

p1=Dot(1,2)
p2=Dot(1,2)
print(p1==p2)
print(str(p1))
print(p2)

rec_1 = Rectangle(11, 13)
rec_2 = Rectangle(10, 13)
print(rec_1 == rec_2)

circle = Circle(4)
print(circle.square())