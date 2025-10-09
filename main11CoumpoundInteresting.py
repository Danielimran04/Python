# phyton compound caluclator
principle=0
rate=0
time=0

while principle <=0:
    principle=float(input("Please input the principle: "))
    if principle <=0:
        print("principle cannot be less than 0")

while rate <=0:
    rate=float(input("Please input rate: "))
    if rate <=0:
        print("rate cannot be less than 0")

while time <=0:
    time=float(input("Please input time: "))
    if time <=0:
        print("time cannot be less than 0")

total = principle * pow((1+(rate/100)),time)
print(f"Balance after {time} year/s: ${total:.2f}")


