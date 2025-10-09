# while loops the condition always true
#makan=input("Tolong isi makan ape yang kau suka (tekan q untuk keluar): ")

#while not makan == "q":
    #print(f"{makan} adalah kegemarakn kauu")
    #makan=input("Tolong isi makan ape yang kau suka (tekan q untuk keluar)")
    
#print("TQ")

num = int(input("Enter a number between 1-10: "))

while num<1 or num >10:
    print(f"{num} is not valid please redo")
    num = int(input("Enter a number between 1-10: "))

print(f"Your number is: {num}")
