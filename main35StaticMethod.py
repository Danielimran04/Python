# Static Methods = A method that belong to a class rather than any object from that class (instance)
#                  Usually used for general utility functions

# Instance methods = Best for operations on instances of the class (Objects)
# Static methods = Best for utility functions that do not need access to class data

#instance method basically mcm kita buat OOP to kene create object dari class and then object tu boleh guna ape ape dlm class
# static method = takyah guna object amik je class lepastu dahh boleh access dhh

class Employee:
    def __init__(self,name,position):
        self.name=name 
        self.position=position

    def get_info(self):
        return f"{self.name}={self.position}"
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager","Cashier","Cook","Janitor"]
        return position in valid_positions # position == valid_postions
    
employee1 = Employee("Eugune","Manager")
employee2 = Employee("LEMAN","Manager")
employee3 = Employee("SUMAN","Manager")

print(Employee.is_valid_position("Manager"))
print(employee2.get_info())
print(employee1.get_info())