# nested loops = A loop within another loops (outer and inner)
for x in range(3): # nih iteration
    for y in range(1,10): # kerja iaitu nombor
        print(y,end=" ") # end maksud dia akan jadi selari nombor dia bukan kebawah kebawah
    print()

print()
rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))
symbols = input("Enter a symbols to use ")

for x in range(rows):
    for y in range(columns):
        print(symbols,end="")
    print()

