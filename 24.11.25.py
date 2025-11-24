import csv

path = "users.csv"

with open(path, "r", encoding="UTF-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0], " - ", row[1])