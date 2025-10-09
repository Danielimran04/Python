
# multiple inheritance = inherit from more than one parent class
#                        C(A, B)

# multilevel inheritance = inherit from a parent which inherits from another parent 
#                          C(B) <- B(A) <- A
class Animal:#grandparent

    def __init__(self,name):
        self.name=name

    def eat(self):
        print(f"{self.name} animal is eating")

    def sleep(self):
        print(f"{self.name} animal is Sleeping")

class Prey(Animal):#(children of animal and parent for rabbit and fish)
    def flee(self):
        print(f"{self.name} is animal is fleeing")

class Predator(Animal):#(Children of Animal and parent for hawk and fish )
    def hunt(self):
        print(f"{self.name} animal is hunting")

class Rabbit(Prey):# children for prey
    pass

class Hawk(Predator):# children for predator
    pass

class Fish(Prey, Predator):#children for prey and predator
    pass

rabbit = Rabbit("Buggs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

fish.hunt()
fish.flee()

rabbit.eat()
rabbit.sleep()