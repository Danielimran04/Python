
def happy_birthday(name,age): # function 
    print(f"Happy birthday to {name}")
    print(f"You are {age} years old")
    print("Happy birthday to you!")
    print()

happy_birthday("ahmad",21)# call function
happy_birthday("leman",31)
happy_birthday("umaw",22)
happy_birthday(21,"wwe")
# baca
# dlm function python kalau kita isi dlm parameter dia terbalik cth 11...21 tu akan jadi name and wwe akan jadi age bila dia hantar kat declare function

def display_invoice(username,amount,due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")
    print()

display_invoice("JoeSchmo",100.01,"01/02")

# return = statement used to end a function and send a result back to the caller

def add(x,y):
    z=x+y
    return z

def substract(x,y):
    z=x-y
    return z

def multiply(x,y):
    z=x*y
    return z

def divided(x,y):
    z=x/y
    return z

print(add(1,2))
print(substract(1,2))
print(multiply(1,2))
print(divided(1,2))



