# iterable = an object/collection that can return its element one at a time,
#            allowing it to be iterated over in a loop

my_dictionary = {"A":1, "B":2, "C":3}

for key in my_dictionary:
    print(key,end=" ")

print()

for values in my_dictionary.values():
    print(values,end=" ")

print()
print()

for key , value in my_dictionary.items():
    print(f"{key} = {value}")