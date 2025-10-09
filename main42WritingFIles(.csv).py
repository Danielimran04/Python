import csv
employee = [["Name", "Age", "Job"],
            ["Spongebob", 30,"Cook"],
            ["Patrick", 37, "Unemployed"],
            ["Sandy",27,"Scientist"]]

file_path="C:\\Users\\User\\Desktop\\PROJECT JUTA JUTA\\output.csv"

try:
    with open(file=file_path,mode="w",newline="") as file:
        writer = csv.writer(file)
        for row in employee:
            writer.writerow(row)
        print(f"CSV file {file_path} was created")
except FileExistsError:
    print("The file already exist")