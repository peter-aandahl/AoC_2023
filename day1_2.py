import csv
import re

with open('sample2.txt', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')

    letter_digits = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
                     'zero': 0}

    only_digits=''
    for row in reader:
        data = row[0]
        print(data)
        for letter in letter_digits:
            for i in range(0, len(data)):
                if data[i:].startswith(letter):
                    only_digits = only_digits + str(letter_digits[letter])
        print(only_digits)
        only_digits = ''