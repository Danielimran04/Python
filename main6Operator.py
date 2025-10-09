# logical operator OR = atleast one condition must be true 
#                  AND = both condtion must be true
#                  NOT = inverts the codition (not false, not True)

# exp1
temp=float(input("Please enter the outdoor temperature "))
is_sunny = input("Is it sunny outside? (yes/no): ").lower()== "yes"


if temp >= 28 and is_sunny:
    print("It is hot outside")
    print("It is sunny")
elif temp <=0 and is_sunny:
    print("It is cold outside")
    print("It is sunny")
elif temp >= 28 and not is_sunny:
    print("It is hot outside")
    print("It is Cloudy")
elif temp <=0 and not is_sunny:
    print("It is COLD outside")
    print("It is cloudy")
elif 28 > temp >0 and not is_sunny:
    print("It is WARM outside")
    print("It is CLOUDY")
