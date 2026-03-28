import csv

with open("dummy_files/2026-03-25_employees.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if int(row["salary"]) > 60000:
            print(row)


