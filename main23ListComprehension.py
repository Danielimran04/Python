# list comprehension = A concise way to create lists in python
#                      Compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]

doubles = [x * 2 for x in range(1, 11)]
triples = [y * 3 for y in range(1,11)]
squares = [z*z for z in range(1, 11)]

print(doubles)
print(triples)
print(squares)
print()

fruits = ["apple","orange","banana","coconut"]
fruits = [fruit.upper() for fruit in fruits]
print(fruits)
print()
buah_char = ["apple","orange","banana","coconut"]
buah_char = [buahs[0] for buahs in buah_char]
print(buah_char)
print()

numbers=[1,-2,3,-4,5,-6,8,-7]
positive_nums = [num for num in numbers if num>=0]
negative_nums = [num for num in numbers if num < 0]
even_nums = [num for num in numbers if num % 2== 0]
odd_nums = [num for num in numbers if num % 2 == 1]

print(positive_nums)
print(negative_nums)
print(even_nums)
print(odd_nums)
print()

