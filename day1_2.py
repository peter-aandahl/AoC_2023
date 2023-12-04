import csv

with open('day1_data.txt', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')

    digits = {'one': '1',
              'two': '2',
              'three': '3',
              'four': '4',
              'five': '5',
              'six': '6',
              'seven': '7',
              'eight': '8',
              'nine': '9',
              'zero': '0',
              '1': '1',
              '2': '2',
              '3': '3',
              '4': '4',
              '5': '5',
              '6': '6',
              '7': '7',
              '8': '8',
              '9': '9',
              '0': '0'}

    total = 0

    for row in reader:
        data = row[0]
        #print(data)
        n=0
        first_number = ''
        for i in range(0,len(data)):
            for x in digits:
                if data[n:].startswith(x) and first_number == '':
                    first_number = digits[x]
            n = n + 1

        data = row[0][::-1]
        n=0
        last_number = ''
        for i in range(len(data), 0, -1):
            for x in digits:
                if data[n:].startswith(x[::-1]) and last_number == '':
                    last_number = digits[x]
            n = n + 1

        row_total = first_number + last_number

        total = total + int(row_total)

    print(total)