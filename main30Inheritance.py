# inheritance = Allows a class to inherit attributes and methods from another class
#               child(parent)

class Animal:
    def __init__(self,name):
        self.name=name
        self.is_alive=True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")


class Mouse(Animal):
    def speak(self):
        print("SQUID!")


dog = Dog("Scooby")
cat= Cat("Uin bin baby")
mouse = Mouse("Mickey")

print(cat.name)
print(cat.is_alive)
cat.eat()
cat.sleep()
cat.speak()
