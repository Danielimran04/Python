# if __name__==__main__ : (This script can be imported OR run standalone)
# function and classses in this module can be reused without the main block of code executing 

def favourite_food(food):
    print(f"Your favourite food is {food}")


def main():
    print("This is script1")
    favourite_food("pizza")
    print("GoodBye")
    


if __name__ == '__main__':
    main()

