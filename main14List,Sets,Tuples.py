# collection = single "Variable" used to store multiple values
# List = [] ordered and changeable.Duplicates OK
# Set = {} unordered and immutable, but Add/Remove OK. NO duplicates 
# Tuple = () ordered and unchangeable. Duplicates OK. Faster

print("**************** UNTUK METHOD LIST [] *****************")
fruits=["Apple","Orange","Banana","Coconut"]
print(len(fruits))# nak cari size fruits
print()
print("Pineapple" in fruits) # untuk nak tahu pineapple ade tak dalam fruits
fruits[0]="Pineapple" # untuk tukar index 0 jadi pineapple cth apple is index 0 tukar jadi pineapple
fruits.append("LEMON") # append is insert value dlm list
fruits.remove("Coconut")# untuk remove coconut dlm list
fruits.insert(0, "MANGGA") # insert function dia kita boleh insert mana mana index and tak buang value index asal index asal anjak kedepan
fruits.sort() # dia akan sort dlm alphabet
#fruits.reverse() # dia akan terbalikkan dari alphabet
#fruits.clear() # nih maksud dia buang semua value

for fruit in fruits:
    print(fruit)

print()
print("**************** UNTUK METHOD SET {} *****************")
buah={"PELAM","MANGGA","OREN","LIMAU"} # kalau kita print dia akan print unordered
print("pineapple" in buah)
#print(buah[0]) #dia akan dpt error sbb set dia unordered so takleh output specific 
buah.add("Grape")
buah.remove("PELAM") # kita takleh tukar set hanya boleh add and remove sahaja
#buah.pop()
#buah.clear()# nih hilang semua 
for x in buah:
    print(x)

print()
print("**************** UNTUK METHOD TUPLE () *****************")
buah1=("apple","strawberry","sprite","apple")
print(buah1.count("apple"))
print(buah1.index("strawberry"))

for buah in buah1:
    print(buah)