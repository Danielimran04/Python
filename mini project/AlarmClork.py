import time
import datetime
import pygame


def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file="C:\\Users\\User\\Desktop\\PROJECT JUTA JUTA\\BELAJAR PHYTON\\mini project\\glue song.mp3"
    is_running=True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S") #nih kita nak amik current masa dan strftime maksud dia nak tukar format
        print(current_time)

        #keluar program
        if current_time == alarm_time:
            print("Wake Up !!!!")

            #nih untuk kita nak masukkkan lagu
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            choice = input("Are you wake up (y/n): ")
            if choice== "y" or "Y":
                is_running=False
                pygame.mixer.music.play()


            
            
                
                
        time.sleep(1) # nih kita outputkan setiap 1 saat

    print("HAVE A NICE DAY DANIEL!!!!")
 

if __name__ == "__main__":# main
    alarm_time=input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)