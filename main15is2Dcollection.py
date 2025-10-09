fruits = ["apple","orange","banana","coconut"]
vegetable = ["celery","carrots","potatoes"]
meats = ["chicken","fish","turkey"]

groceries = [fruits,vegetable,meats]

print(groceries) #dia akan print entire row
print(groceries[0])# dia akan print fruits punya list kalau [1] dia akan print vegetale dan seterusnya
#              row column
print(groceries[0][0]) # dia akan print row 0 index and column 0 index dan output apple
print()
print("EXERCISE BUAT NUM PAD")
num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*",0,"#"))

for row in num_pad:
    for num in row:
        print(num,end=" ")
    print()