# python file detection
import os

file_path = "C:\\Users\\User\\Desktop\\test" # so file test tu dekat dlm folder

if os.path.exists(file_path):
    print(f"The location test.txt exist")

    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("Thats is a directory")

else:
    print("That Location doesnt exist")