#time.sleep(3) # nih program akan sleep cth letak 3 means 3 second akan sleep 
import time

my_time = int(input("Enter the time in seconds: "))

for x in range(my_time,0,-1): # nih cara manual untuk reversed selalu guna reversed je
    seconds = x % 60 # kita nak return kan reminder sebab nak cari berapa saat kan
    minutes =int(x/60)%60
    hours = int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME'S UP!")