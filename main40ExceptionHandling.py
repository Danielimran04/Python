# exception = An event that interrupts the flow of a program
#             (ZeroDivisionError = 1/0, TypeError= 1 + "1" ,ValueError= int("pizza"))
#             1.try,2.Except,3.finally

try:
    number=int(input("Enter a number: "))
    print(1/number)

except ZeroDivisionError:# nih kita bahaagi kosong 
    print("You cant divide by 0 IDIOT!!")
except ValueError:# nih bila kita masukkan bende yang salah 
    print("Enter only number bruhh")
except Exception: # except exception nih maksud dia kalau user masuk sesuatu yang bukan ZeroDivisionError,ValueError dia akan keluar except Exception
    #if kita buang value ZeroDivisionError and ValueError dia akan keluar except Exception
    #disebabkan ade zerodicvision and value error menyebabka exception tu tkde buat ape ape untuk code nih
    print("Something went wrong!")
finally: # dia akan execute bende betul atau kita masukkan error
    print("Do some cleanup here")


