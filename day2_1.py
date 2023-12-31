import csv


with open('day2_data.txt', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    total = 0
    max_result = {'red': 12, 'green': 13, 'blue': 14}

    for row in reader:
        data = ' '.join([str(elem) for elem in row])
        game_id = data.split(':')[0].split(' ')[1]
        set_data = data.split(':')[1]
        no_sets = set_data.count(';')+1

        red = green = blue = True
        for i in range(0, no_sets):
            set = set_data.split(';')[i][1:].replace('  ', ' ').split(' ')
            set_dict = dict(map(lambda x: (set[x + 1], int(set[x])), range(len(set) - 1)[::2]))
            #print(game_id, i,set_dict)
            if 'red' in set_dict.keys():
                 red = max_result['red'] >= set_dict['red']
            if 'green' in set_dict.keys():
                green = max_result['green'] >= set_dict['green']
            if 'blue' in set_dict.keys():
                blue = max_result['blue'] >= set_dict['blue']

            if not(red and green and blue):
                game_id = 0

        total = total + int(game_id)

    print(total)
