import csv


with open('sample2_1.txt', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    total = 0
    for row in reader:
        data = ' '.join([str(elem) for elem in row])
        id = data.split(':')[0].split(' ')[1]
        set_data = data.split(':')[1]
        no_sets = set_data.count(';')

        print(set_data, no_sets)