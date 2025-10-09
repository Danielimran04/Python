from script1 import *

# kalau kita buang if __name__ == '__main__': 
#                           main()
# dan buang  def main(): kita akan dapat output dari script 1 bila kita run dkt script2
# thats why kita guna if __name__ == '__main__': 
#                           main() 
# supaya kalau kita nak guna yang tak penting dari script 1 just lock guna if statement sahaja

def favourite_drink(drink):
    print(f"Your favourite drink is: {drink}")

print("This is script2")
favourite_food("sushi")
favourite_drink("coffee")
print("GoodBye!")