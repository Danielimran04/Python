# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals = {"USA":"WASHINGTON D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia":"Moscow"}

print(capitals.get("USA")) # nih akan cari key value dari usa 
if capitals.get("Russia"):
    print("The capital  exist")
else:
    print("The capital doesn't exist")

print()
capitals.update({"Germany":"Berlin"})# disebabkan key dia takde so dia tambah baru
capitals.update({"USA":"Kuala Lumpur"}) # nih dia akan tukar usa jadi kuala lumpur
print(capitals)
print()
capitals.pop("China") # maksud dia remove china
print(capitals)
#capitals.popitem()# pop item will remove last item such as germany
#print(capitals)
#capitals.clear() # nih dia buang semua
keys = capitals.keys() # untuk kita nak tahu cari keys
for key in keys:
    print(key)
print()
values = capitals.values() # untuk kita nak cari values entire key
for value in values:
    print(value)

print()
# kalau nak output semua kita buat cmni
for key, value in capitals.items():
    print(f"{key}:{value}")