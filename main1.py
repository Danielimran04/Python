# ini untuk output boleh je guna "" atau ''
print("aku hebat")
print('aku memang hebat\n')

#variable (String)
first_name="DANIEL"
food="nasi goreng"
email="daniel@123.gmail.com"
print(first_name)
# kita boleh jugak guna variable along with text so kene tambah f means f-String
print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email is: {email}\n")

#Integer
age=21
quantity=3
num_of_stud=30

print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_stud} students\n")

#float
price=10.99
gpa=3.9
distance= 5.5
print(f"The price is ${price}")
print(f"Your gps is: {gpa}")
print(f"You ran {distance} KM\n")

#boolean
is_student = True
print(f"Are you a student: {is_student}\n")

#type casting= the process of converting a variable from one data type to another
#str(),int(),float(),bool()
name="DANIEL"
name1=""
age=21
gpa=3.5
is_student=True

print(type(name)) #untuk kita tahu data type variable dia

gpa=int(gpa) #kita type casting kan float gpa to int gpa
print(gpa)

age=float(age)
print(age)

age=str(age)
print(age)#so ini kita outputkan string so bila output kan dia jadi 21.0 dalam string
print(type(age))
age += "1"
print(age)

#SO BILA VARIABLE DIA XDE VALUE DIA AKAN JADI FALSE IF ADE JADI TRUE
name= bool(name)
print(name)

name1=bool(name1)
print(name1)
