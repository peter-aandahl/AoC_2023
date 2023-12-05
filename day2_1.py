import csv


with open('sample2_1.txt', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    total = 0
    for row in reader:
        data = ' '.join([str(elem) for elem in row])
        game_id = data.split(':')[0].split(' ')[1]
        set_data = data.split(':')[1]
        no_sets = set_data.count(';')

        for i in range(0, no_sets):
            set = set_data.split(';')[i][1:].replace('  ', ' ').split(' ')
            print(game_id, i, set)


        print("Next row")
