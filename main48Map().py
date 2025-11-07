# map(function, collection) = Applies a given function to all items in a collection

def c_to_f(temp):
    return(temp *9/5) + 32

celsius_temps = [0.0, 10.0, 20.0, 30.0, 40.0, 50.0]

fahrenheit_temps = map(c_to_f,celsius_temps)

fahrenheit_lists = list(map(c_to_f,celsius_temps))


print("OUTPUT FOR fahrenheit_temps")
for temp in fahrenheit_temps:
    print(temp)# nih dia akan print kan each of the celsius_temps 

print()

print("OUTPUT FOR fahrenheit_lists")
print(fahrenheit_lists)


print()
#kalau taknak guna function pun boleh kita guna kan 

fahrenheit_lambda = list(map(lambda temp: (temp*9/5)+32, celsius_temps))

print(fahrenheit_lambda)


# boleh jugak kita masukkan dua nombor atau lebih sekaligus

print()
user_input = input("Masukkan nombor dalam satu line: ")

numbers = map(int, user_input.split()) #yang split dia akan pecah kan satu per satu ikut space contoh 23 3 so dia akan pecah kan 23 and 3 dan tambah kan sebab kita kan ade int
#int tu adalah salah satu built in function dlm python mcm int(), str(),float(),bool()

jumlah = sum(numbers)

print(f"Jumlah: {jumlah}")