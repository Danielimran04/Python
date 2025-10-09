import datetime
#                    year,month,day
date = datetime.date(2025,  1,   2) #set date into variable
today = datetime.date.today() # untuk nk tahu date harini
#                  jam,  minit, saat
time = datetime.time(12,  30,    0) #untuk set time in java
now = datetime.datetime.now() # untuk nak tahu masa dan tarikh sekarang
#                 jam,minit,saat       day,month,year
now = now.strftime("%H:%M:%S             %d-%m-%Y")
#                                   DATE         TIME
target_datetime=datetime.datetime(2015, 1, 2, 12, 30, 1)
current_datetime=datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target has not passed")

print(date)
print(today)
print(time)
print(now)
