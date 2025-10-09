# @property = Decorator used to define a method as a property (it can be accessed like an attribute)
#             Benifit: Add additional logic when read(Getter), write(setter), Delete sttribute(delete)
# so property selalunya kita nak ubah each attribute dlm constructor kepada bentuk yang lain

class Rectangle:
    def __init__(self,width,height):
        self._width=width #self._ means attribute tu kita private kan means hanya guna dlm class tu je
        self._height=height

    @property
    def width(self):
        return f"{self._width:.1f}cm"
    
    @property
    def height(self):
        return f"{self._height:.1f}cm"
    
    @width.setter
    def width(self,new_width):# new_width adalah yg line 38 dia banding kan and masukkan dlm private attribute
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than 0")

    @height.setter
    def height(self,new_height):# new_height adalah yg line 39 dia banding kan and masukkan dlm private attribute
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than 0")

    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")
    
    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")





rectangle=Rectangle(3,4)

rectangle.width=5
rectangle.height=6

print(rectangle._width) # so bila attribute kita kene private buat same dekat object 
print(rectangle._height) # so bila attribute kita kene private buat same dekat object 
print()
print(rectangle.width)
print(rectangle.height)

del rectangle.width
del rectangle.height
