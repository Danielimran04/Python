# indexing = accessing elements of a sequence using [] (indexing operation)
#            [start: end : step]
credit_number="1234-5678-9012-3456"

print(credit_number[0]) # nih dia output kan index first
print(credit_number[:4]) # stop at index 4
print(credit_number[5:9]) # start index 5 stop index 9
print(credit_number[5:]) # start index 5 until end
print(credit_number[-1]) # dia akan outputkan nombor 6 blkg sekali
print(credit_number[::2]) # dia akan lompat next step when dekat step kedua
print("")

last_digit=credit_number[-4:]
print(f"xxxx-xxxx-xxxx-{last_digit}")