#!/usr/bin/python3
import csv

# open the file in the write mode
# f = open('people.csv', 'w')
#
# writer = csv.writer(f)
#
# writer.writerow(row)
#
# f.close()

header = ['name', 'age', 'campus']
data = [
    ['muller', 21, 'Egerton'],
    ['wilson', 22, 'Moi university']
]

with open('people.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    writer.writerow(header)
    writer.writerows(data)
