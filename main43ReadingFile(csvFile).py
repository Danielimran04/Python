import csv

file_path="C:/Users/User/Desktop/PROJECT JUTA JUTA/output.csv"

try:
    with open(file_path,"r") as file:
        content= csv.reader(file) 
        for line in content: # for every line print content
         print(line[1]) # [] = column output kalau xde [] dia akan keluar sebijik dlm file

except Exception:
    print("Something went wrong")