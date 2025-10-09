#Shopping cart main 14
foods=[]
prices=[]
total=0

while True:
    food=input("Enter a food to buy (q to quit): ")
    if food.lower()=="q":
        break
    else:
        price=float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)
    
print()
print("***********************THE CART OF THE FOODS**********************")
for food in foods:
    print(f"{food:<15}", end="")   # keep printing on same line
print()  # new line after foods

# second loop for prices
for price in prices:
    total=total+price
    print(f"${price:<14,.2f}", end="")  # match spacing with foods
print()
print()
print(f"Your total is ${total}")
        
    