# module = a file containing code you want to include in your program use 'import' to include a module (built-in or own)
#          useful to breakup a large program rusable seperate files 

import math as m
# or
import math
print(m.pi)
print(math.pi) # import math atau sebagai nih built in 
print()

print("------nih untuk nak import dile main 25 UTKimport----------")
import main25UTKImport as exp

result = exp.pi
result = exp.square(3)
result = exp.cube(3)
result = exp.circumference(3)
result = exp.area(3)

print(result)

