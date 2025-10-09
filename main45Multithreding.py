# multithreading = Used to perform multiple tasks concurrently(Multitasking)
#                  Good for I/O bound tasks like reading files or fetching data from APIs
#                  Threading.Thread(target=my_function)

import threading
import time

def walk_dog(first,last):
    time.sleep(8)
    print(f"You finish walking the {first} {last}")

def take_out_trash():
    time.sleep(2)
    print("You take out the trash")

def get_mail():
    time.sleep(4)
    print("You get the email")

# chore 1 sampai 3 tu adalah variable untuk thread kerja yang mana dia akan cari mana time sleep paling rendah dulu dia outputkan dulu
# args tu maksud dia kita nak pass value dekat first and last first=scooby last=DOO
chore1 = threading.Thread(target=walk_dog,args=("Scooby","DOO"))
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

# sbb ape buat join method sbb line 37 kita nak buat output so kalau xde join method dia akan muncul first menyebabkan output tk cantik
# so join method adalah untuk biar thread buat kerja dulu
chore1.join()
chore2.join()
chore3.join()

print("All chores are complete!")

