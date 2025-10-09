# conditional expresssion = A one-line shortcut for the if-else statement (ternary operator)
#                           Print or assign one of two values based on a condtion
#                           X if condtion else Y

#num=6
#result = "EVEN" if num % 2 == 0 else "ODD" 
#print(result)

num = 5
a=6
b=7
age = 13
temperature = 30
user_role="guest"

max_num = a if a > b else b
min_num = a if a<b else b
status = "Adult" if age>= 18 else "Child"
access_level="FUll Access" if user_role=="admin" else "Limited Access"

print(access_level)
