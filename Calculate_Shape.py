import math


class Shape:
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius**2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


shape_type = input(
    "Choose the type of shape (circle or c , triangle or t, rectangle or r): ").lower()

if shape_type == "circle" or shape_type == "c":
    radius = float(input("Enter the value for the radius of the circle: "))
    circle = Circle(radius)
    print("Circle area:", circle.calculate_area())
    print("Perimeter of a circle:", circle.calculate_perimeter())
elif shape_type == "triangle" or shape_type == "t":
    side1 = float(
        input("Enter the length of the first side of the triangle: "))
    side2 = float(
        input("Enter the length of the scound side of the triangle: "))
    side3 = float(
        input("Enter the length of the third side of the triangle: "))
    triangle = Triangle(side1, side2, side3)
    print("triangle area:", triangle.calculate_area())
    print("Perimeter of the triangle:", triangle.calculate_perimeter())
elif shape_type == "rectangle" or shape_type == "r":
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    rectangle = Rectangle(length, width)
    print("rectangle area:", rectangle.calculate_area())
    print("Perimeter of the rectangle:", rectangle.calculate_perimeter())
else:
    print("The Shape type is not correct!")
