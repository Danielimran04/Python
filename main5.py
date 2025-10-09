# if = Do some code only if some condition is true 
# else dp something else
age=int(input("Enter your age: "))

if age>=18 and age<99:
    print("You are now signed up!")
elif age <0:
    print("You havent been born yet!")
elif age>100 and age<102:
    print("you to old")
else:
    print("You must be 18+ to sign up\n")