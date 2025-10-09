# validate user input exercise
# 1. username is no more than 12 character
# 2. username must not contain digits
# 3. username must not contain space

username = input("Enter a username: ")

if len(username) > 12 :
    print("Your username must not more than 12 character")
elif not username.find(" ")==-1:
    print("Your username cant be more than 12 character")
elif not username.isalpha():
    print("Your username cant contain digits")
else:
    print(f"welcome {username}")