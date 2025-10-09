#              i i<11
for x in range(1,11):
    print(x)

print()

for x in reversed(range(1,5)):# nih backward
    print(x)

print()
#              i  (i<11 atau habis dekat 11) i+2  
for x in range(1 ,          11 ,              2):
    print(x)

print()

for x in range(1,15): # continue dia skip nombor 13 kalau break pula dia akan berhenti kat 13 je 
     if x == 13:
         continue
     else:
         print(x)
    