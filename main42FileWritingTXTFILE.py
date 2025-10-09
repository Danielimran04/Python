# python writing files(.txt, .json, .csv)
txt_data = "I like nasi goreng"
file_path = "output.txt" # kalau mcm nih dia akan buat file dekat dlm folder kita buat sekarang
file_path2= "C:/Users/User/Desktop/output.txt" # yg nih pulak kita nak letak file tu dekat desktop
employees = ["Eugene","Squidward","Spongebob","Patrick"]


# with = nih is open and close file dia akan open bila kita buaat sesuatu and dh habis dia akan close sendiri
# w = write file
#file=file_path
# mode = "w" is dia akan write if dh buat run lagi dia tak keluar print exception
# mode ="x" is dia akan write and kalau bende tu file tu dh buat dia takkan buat lagi dia akan keluar ouput exception kita buat
# mode = "a" is dia akan append if dia dh write bende same pun dia append 
try:
    #                  mode
    with open(file_path,"x") as file:
        file.write(txt_data)
        print(f"txt file '{file_path}' was created") # file letak dekat folder

except FileExistsError:
    print("The file already exist")

try:      
 #                      mode
    with open(file_path2,"a") as file:
        file.write("\n" + txt_data)
        print(f"txt file '{file_path2}' was created")# file letak dekat desktop
except FileExistsError:
    print("The file already exist")

try:
    with open(file_path,"x") as file:
        for employee in employees: # so employee takleh masuk mcm biasa  kene buat forloops
            file.write("\n"+ employee + ", ")
            print(f"txt file {file_path2} was created")
except FileExistsError:
    print("That file already exists!")

        



