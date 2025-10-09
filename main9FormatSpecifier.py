#.(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces 
# :03 = allocates and zero pad that many spaces 
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# : = insert a space before positive numbers
# :, = comma separator

price1 = 3000.14159
price2 = -9870.65
price3 = 1200.34

print(f"Price 1 is ${price1:.1f}") #1f maksud dia 3 tempat perpuluhan yang dia tak bundarkan
print(f"Price 2 is ${price2:.1f}")
print (f"Price 3 is ${price3:.1f}")
print()
print(f"Price 1 is ${price1:10}") #yg nih maksud dia jarakkan sepuluh spaces 
print(f"Price 2 is ${price2:10}")
print (f"Price 3 is ${price3:10}")
print()
print(f"Price 1 is ${price1:010}") # nih maksud dia tambah 0 yang memenuhi 10 jarak spaces cth 010=viasa but 020=01,02,03,04,05
print(f"Price 2 is ${price2:010}")
print (f"Price 3 is ${price3:010}")
print()
print(f"Price 1 is ${price1:<10}") # all these number is justify to left
print(f"Price 2 is ${price2:<10}")
print (f"Price 3 is ${price3:<10}")
print()
print(f"Price 1 is ${price1:>10}") # right justify
print(f"Price 2 is ${price2:>10}")
print (f"Price 3 is ${price3:>10}")
print()
print(f"Price 1 is ${price1:^10}") # nombor jadi center
print(f"Price 2 is ${price2:^10}")
print(f"Price 3 is ${price3:^10}")
print()
print(f"Price 1 is ${price1:+}") # nombor kita nak letak positive sign price 2 kan negative so takleh positive
print(f"Price 2 is ${price2:+}")
print(f"Price 3 is ${price3:+}")
print()
print(f"Price 1 is ${price1:,}") # nih dia letak koma untuk ribu 
print(f"Price 2 is ${price2:,}")
print(f"Price 3 is ${price3:,}")
print()
print(f"Price 1 is ${price1:+,.2f}") # kita gabung kan mcm nih pun boleh
print(f"Price 2 is ${price2:+,.2f}")
print(f"Price 3 is ${price3:+,.2f}")