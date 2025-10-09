import json

file_path="C:\\Users\\User\\Desktop\\PROJECT JUTA JUTA\\output.json"

try:
    with open(file_path,"r") as file:
        content= json.load(file)  
        print(content)
        print(content["age"]) # nih untuk nak tgk value from the key

except Exception:
    print("Something went wrong")