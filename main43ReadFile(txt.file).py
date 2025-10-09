import os

file_path="C:\\Users\\User\\Desktop\\PROJECT JUTA JUTA\\output.txt"

try:
    with open(file_path,"r") as file:
        content=file.read()# baca file
        print(content)

except Exception:
    print("Something went wrong")