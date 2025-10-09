import json

employee = {
    "name": "Spongebob",
    "age": 30,
    "job": "cook"
}

file_path = "C:\\Users\\User\\Desktop\\PROJECT JUTA JUTA\\output.json"

try:
    with open(file_path,"w") as file:
        json.dump(employee, file, indent=4)# dump method= is to convert dictionary(employee) to json string to output
        print(f"json file '{file_path}' was created")
except FileExistsError:
    print("That File already Exists")