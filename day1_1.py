import csv
import re

with open('day1_data.txt', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    total = 0
    for row in reader:
        data = row[0]
        s = re.search('\d', data).start()
        e = re.search('\d', data[::-1]).start()
        digit1 = int(data[s])
        digit2 = int(data[::-1][e])

        row_total = digit1*10 + digit2
        total = total + row_total

    print(total)