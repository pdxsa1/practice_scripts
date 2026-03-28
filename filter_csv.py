import csv

with open("../dummy_files/employees.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if int(row["salary"]) > 60000:
            print(row)


