import random

low = 1
high = 100
options = ("rock","paper","scissors")
cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]

number = random.randint(low,high) # nih computer pick random in range 1-100
number1=random.random() # nih maksud dia pick numbe rin rang 0 and 1
option=random.choice(options) # random choose
random.shuffle(cards)# dia shuffle card

print(number)
print(number1)
print(option)
print(cards)
