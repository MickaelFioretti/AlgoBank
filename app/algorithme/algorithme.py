import csv

actions = []
with open("./data/dataset1_Python+P7.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    next(csv_reader)  # Ignorer l'en-tête
    for row in csv_reader:
        name = row[0]
        price = float(row[1])  # Convertir en float
        profit = float(row[2])  # Convertir en float
        actions.append((name, price, profit))


print(actions)
