name = input("Enter your full name: ")
phone_number=input("Enter your phone number: ")

result= len(name) # dia akan count setiap string include space
print(result)
print("")

result1=name.find(" ") # yang nih dia akan dari first perkataan so dlm array is index 0 so dia akan kira sampai jumpa space baru berhenti
#                        cth: BRO CODE so B is index 0 and sampai jumpa space jadi 3
contoh_result1=name.find("o") # contoh dia nak input bro code so bro code IS 2 sbb lepas r
print(result1)
print(f"Ini contoh bila kita input name bro code: {contoh_result1}")
print("")

result2=name.rfind("o") # YANG NIH DIA AKAN KIRA LAST o cth bro code so dia kira sampai lepas c
print(f"ini dia kira bila lepas c: {result2}\n")
result3=name.rfind("q")
print(f"INI MAKSUD DIA dalam bracket name.find() atau name.rfind() tak dpt cari yang user input {result3}")
print("")

name=name.capitalize() # Ini maksud dia first word user input will be capitalized
print(name)
name=name.upper() # ini maksud dia semua jadi huruf besar bila user input
print(name)
name=name.lower() # ini maksud dia semua huruf jadi kecik
print(name)
print("")

reuslt4 = name.isdigit() # yg nih dia akan return true bila user input bagi nombor kalau string return false also input bro123 pun return false
result5 = name.isalpha() # yg nih dia akan return true bila string tak jarak contoh BroCode== true Bro code == false
print(reuslt4)
print(result5)
print("")

result6 = phone_number.count("-") # nih dia count - kat phone number
print(result6)
result7= phone_number.replace("-","#") # yg nih kita akan tukar - jadi #
print(result7)
