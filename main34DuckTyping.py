# Duck Typing = Another way to achieve polymorphism besides Inheritance
#               Object must have the minimum necessary attributes/methods
#               If it looks like a duck and quaks like a duck,it must be a duck

class Animal:
    alive=True

class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Meow")

class Car:
    alive = False
    def speak(self):
        print("HONK")

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)

# CAR kan bukan animal and child of the parent so kalau nak same category sikit mcm value parent animal 
# so kita buat cmni duck typing dekat duck typing CAR nih mesti dia punya function adalah sama supaya boleh tiru gaya dia
# and kalau nak amik class variable(alive) kene buat sendiri dekat dalam class CAR 