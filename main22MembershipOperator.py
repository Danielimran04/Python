# membershipOperator = used to test whether a value is found in a sequence (string,list,set,or dictionary)
#                       1.in
#                       2.not in

word ="APPLE"

letter = input("Guess a letter in the secret word: ")

if letter not in word:
    print(f"{letter} was not found")
else: 
    print(f"The letter is a {letter}")

print()
print("EXERCISE 2:")
print()

student=["ALI","ABU","LEMAN"]
name=input("Please enter your name: ")
if name in student:
    print(f"Your name is in the list")
    print(f"WELCOME {name}")
else:
    print(f"your name {name} not in the list ")

print()
print("EXERCISE 3:")
print()

grades={"Sandy":"A",
        "Squidward":"B",
        "Spongebob":"C",
        "Patrick":"D"}

pelajar = input("Please enter the name of the students: ")

if pelajar in grades:
    print(f"{pelajar}'s grade is {grades[pelajar]}")# grades[pelajar] means cari key values
else: 
    print(f"{pelajar} was not found")

print()
print("EXERCISE 3:")
print()

email = input("try your email: ")
if "@" in email and ".com" in email:
    print("your email is valid ")
else:
    print("You must be lost something icons")