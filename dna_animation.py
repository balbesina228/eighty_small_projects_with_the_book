from sys import exit
from random import randint
from time import sleep

pause = 0.15

rows = [
    '         ###',
    '       #{}-{}#',
    '      #{}---{}#',
    '     #{}-----{}#',
    '    #{}------{}#',
    '   #{}------{}#',
    '   #{}-----{}#',
    '    #{}---{}#',
    '     #{}-{}#',
    '       ###',
    '     #{}-{}#',
    '     #{}---{}#',
    '    #{}-----{}#',
    '    #{}------{}#',
    '     #{}------{}#',
    '      #{}-----{}#',
    '       #{}---{}#',
    '        #{}-{}#'
]

try:
    print('DNA animation by Al Sweigart.\nPress Ctrl-C to quit.')
    row_index = 0
    while True:
        row_index += 1
        if row_index == len(rows):
            row_index = 0

        if row_index == 0 or row_index == 9:
            print(rows[row_index])
            sleep(pause)
            continue

        random_selection = randint(1,4)
        if random_selection == 1:
            left_nucleotide, right_nucleotide = 'A', 'T'
        elif random_selection == 2:
            left_nucleotide, right_nucleotide = 'T', 'A'
        elif random_selection == 3:
            left_nucleotide, right_nucleotide = 'G', 'C'
        elif random_selection == 4:
            left_nucleotide, right_nucleotide = 'C', 'G'

        print(rows[row_index].format(left_nucleotide, right_nucleotide))
        sleep(pause)
        continue

except KeyboardInterrupt:
    exit()
