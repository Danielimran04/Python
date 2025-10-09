#input() = A function that prompts the user to enter data returns the entered data as a string
name = input("What is your name: ")
age=input("how old are you?")
print(f"Hello {name}")
print(f"You are {age} years old\n")
#kita takleh change value in input because in python input semua string
#so kita buat cmni
age=int(age)
age=age+1
print(f"Your age if plus 1 is:{age}\n")

#atau kita boleh buat cmni
age=int(input("how old are you again?: "))
age=age + 2
print(f"Your age if plus 2 is: {age}\n\n")

#Exercise 1 rectangle area calc
print("NOW KITA BUAT EXERCISE\n")
length=float(input("Enter the length:"))
width=float(input("Enter your width:"))
area=length*width
print(f"The area of rectangle is :{area}cm ")

             