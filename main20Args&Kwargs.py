# *args = allowe you to pass multiple non-key arguments
# **kwargs = allows you to pass multiple keyword-arguments
#              * unpacking operator

# basically *args nih is kita boleh letak ape ape dekat function call takyah like focus more 
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(add(1,2,3,4,5,6,7,8,9,10))

# tak semestinya nak guna args boleh je ape ape janji ade *
def display_name(*name):
    for x in name:
        print(x,end=" ")
    
display_name("MUHAMAD","DANIEL","IMRAN","BIN","ABU","BAKAR")
print("\n")
print("--------------------KWARGS METHOD---------------------------------\n")

#BASICALLY KWARGS FUNCTION DIA KITA BOLEH GUNA DICTIONARY

def print_address(**kwargs):
    for key in kwargs.values():
        print(key)
    print()
    for key in kwargs.keys():
        print(key)
    print()
    for key,value in kwargs.items():
        print(f"{key}:{value}")
    print()



print_address(street="123 Fake St.",
              city = "Detroit",
              state= "MI",
              zip = "54321")

print("\n")
print("-----------SHIPPING LABEL-------------")
print()

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg,end=" ")
    print()
    if "apartment" in kwargs:
     print(f"{kwargs.get('street')} {kwargs.get('apartment')}")
    else:
        print(f"{kwargs.get('street')}")
              
    print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('zip')}")

shipping_label("DR.","Spongebob","Squarepants",
               street="123 Fake St.",
               apartment ="#100",
              city = "Detroit",
              state= "MI",
              zip = "54321")