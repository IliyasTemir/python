#1
class StringManipulator:
    def __init__(self):
        self.text = ""

    def getString(self):
    
        self.text = input("")

    def printString(self):
    
        print(self.text.upper())


obj = StringManipulator()
obj.getString()
obj.printString()

#2
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self):
        self.length = float(input(" "))

    def area(self):
        return self.length ** 2

shape = Shape()
print("", shape.area())

square = Square()
print("", square.area())

#3
class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self):
        self.length = float(input(""))
        self.width = float(input(""))

    def area(self):
        return self.length * self.width


shape = Shape()
print("", shape.area())

rectangle = Rectangle()
print("", rectangle.area())

#4

import math

class Point:
    def __init__(self):
        self.x = float(input(""))
        self.y = float(input(""))

    def show(self):
        
        print(f"({self.x}, {self.y})")

    def move(self):
        self.x = float(input(""))
        self.y = float(input(""))

    def dist(self, other_point):
    
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)


p1 = Point()
p2 = Point()

p1.show()  
p2.show()  

print("", p1.dist(p2))  

p1.move()
p1.show()
