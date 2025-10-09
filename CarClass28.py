
class Car:# class
    #self = this object is creating
    # after slef attribute dia dlm parameter so dlmpython wajib lah self nih

    def __init__(self, model, year, color, for_sale): #constructor
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
    
    #method are the class that can perform
    def drive(self):
        print(f"You drive a {self.color} {self.model}")
    
    def stop(self):
        print(f"You stop the {self.color} {self.model}")

    def describe(self):
        print(f"{self.year}  {self.model} {self.color}")