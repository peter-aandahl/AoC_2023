import csv


with open('sample2_1.txt', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    total = 0
    max_result = {'red': 12, 'green': 13, 'blue': 14}

    for row in reader:
        data = ' '.join([str(elem) for elem in row])
        game_id = data.split(':')[0].split(' ')[1]
        set_data = data.split(':')[1]
        no_sets = set_data.count(';')

        for i in range(0, no_sets):
            set = set_data.split(';')[i][1:].replace('  ', ' ').split(' ')
            set_dict = dict(map(lambda x: (set[x + 1], int(set[x])), range(len(set) - 1)[::2]))
            print(game_id, i,set_dict)
            if 'red' in set_dict.keys():
                print(max_result['red'])


        print("Next row")
