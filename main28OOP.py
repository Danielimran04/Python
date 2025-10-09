from CarClass28 import Car

# object = A "bundle" of related attributes (variables) and methods (functions)
#          Ex. phone,cup,book
#          You need  a "class" to create many object
#  class = (blueprint) used to design the structure and layout of an object



#           model   year  color for_sale
car1 = Car("Mustang",2024,"Red",False) # object
car2 = Car("Corvette",2025,"blue",True)
car3 = Car("Charger",2026,"Yellow",True)

print(car1) # dia akan bagi memory address car1 object located
print(car1.model) # access object dari model
print(car1.color)
print(car1.for_sale)

car1.drive()#call method
car1.stop()# call method
car2.drive()
car2.stop()
print()
car1.describe()
