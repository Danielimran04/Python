import math
##friends = 5
##friends = friends ** 2
##friends **= 2
##print(friends)

x=3.14
y=-4
z=5

#result=round(x) #dia round kan amik no bulat shaja
#result = abs(y) # abs is absolute semua dia positive kan value dia
#result=pow(4,3) # maksud dia 4 power of 3
#result=max(x,y,z) # dia cari mana value max antara 3 tu
#result=min(x,y,z) # dia cari minimum value

#print(math.pi) #untuk cari nilai pi kene import math
#print(math.e) # untuk cari nilai e
#result = math.sqrt(x)
#result=math.ceil(x) # nih dia outputkan nilai besar dia kalau point iaitu 4
#result=math.floor(x) # nih same je dia round kan 
#print(result)

print("Kita buat exercise area of circumference\n")
radius=float(input("Enter the radius of a circle: "))
circumference=2*math.pi*radius
print(f"The circumference is : {round(circumference,2)}\n")

print("EXERCISE FOR AREA OF CIRCLE")
radius=float(input("Enter the radius of a circle: "))
area=math.pi * pow(radius,2)
print(f"The area of circle is: {round(area,3)} cm\n")

print("cari hypotunus ")
a=float(input("Enter side A: "))
b=float(input("Enter side B: "))

c=math.sqrt(pow(a,2)+pow(b,2))

print(f"Side c is {c}")


