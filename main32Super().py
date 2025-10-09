# super() = function used in a child class to call methods from a parents class (superclass)
#           Allows you to extend the functionallity of the inherited methods 

class Shape: #parent class
    def __init__(self,color,is_filled):
        self.color=color
        self.is_filled=is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self,color,is_filled,radius):
        super().__init__(color,is_filled)# yg nih dia amik semua constructor dari parent
        self.radius=radius

    def describe(self):
        print(f"It is a circle with an area of {3.14 * self.radius * self.radius}cm")
        super().describe()# yg nih dia amik function dari parent class

class Square(Shape):
    def __init__(self,color,is_filled,width):
        super().__init__(color,is_filled)# yg nih dia amik semua constructor dari parent
        self.width=width

    def describe(self):
        print(f"It is a square with an area of {self.width * self.width}cm")
        super().describe()# yg nih dia amik function dari parent class

class Triangle(Shape):
    def __init__(self,color,is_filled,width,height):
        super().__init__(color,is_filled)# yg nih dia amik semua constructor dari parent
        self.width=width
        self.height=height

    def describe(self):
        print(f"It is a triangle with an area of {0.5 * self.width * self.height}cm")
        super().describe()# yg nih dia amik function dari parent class


circle = Circle(color="red",is_filled=True,radius=5)
square = Square(color="Blue",is_filled=False,width=6)
triangle = Triangle(color="Yellow",is_filled=True,width=7,height=8)

print(square.color)
print(square.is_filled)
print(f"{square.width}cm")
print()
circle.describe()
print()
square.describe()
print()
triangle.describe()