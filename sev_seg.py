"This module is meant to be imported rather than run."

"""Seven segment indicator, the segments are the letters from A to G:
 __A__
|     |    All the digits are shown on the indicator:
F     B    __       __  __        __   __  __   __   __
|__G__|   |  |   |  __| __| |__| |__  |__    | |__| |__|
|     |   |__|   | |__  __|    |  __| |__|   | |__|  __|
E     C
|__D__|"""

def get_sev_seg_str(number, min_width=0):
    number = str(number).zfill(min_width)
    rows = ['', '', '']
    for i, numeral in enumerate(number):
        if numeral == '.':
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += '.'
            continue
        elif numeral == '-':
            rows[0] += '    '
            rows[1] += ' __ '
            rows[2] += '    '
        elif numeral == '0':
            rows[0] += ' __ '
            rows[1] += '|  |'
            rows[2] += '|__|'
        elif numeral == '1':
            rows[0] += '    '
            rows[1] += '   |'
            rows[2] += '   |'
        elif numeral == '2':
            rows[0] += ' __ '
            rows[1] += ' __|'
            rows[2] += '|__ '
        elif numeral == '3':
            rows[0] += ' __ '
            rows[1] += ' __|'
            rows[2] += ' __|'
        elif numeral == '4':
            rows[0] += '    '
            rows[1] += '|__|'
            rows[2] += '   |'
        elif numeral == '5':
            rows[0] += ' __ '
            rows[1] += '|__ '
            rows[2] += ' __|'
        elif numeral == '6':
            rows[0] += ' __ '
            rows[1] += '|__ '
            rows[2] += '|__|'
        elif numeral == '7':
            rows[0] += ' __ '
            rows[1] += '   |'
            rows[2] += '   |'
        elif numeral == '8':
            rows[0] += ' __ '
            rows[1] += '|__|'
            rows[2] += '|__|'
        elif numeral == '9':
            rows[0] += ' __ '
            rows[1] += '|__|'
            rows[2] += ' __|'

        if i != len(number) - 1:
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += ' '

    return '\n'.join(rows)

if __name__ == '__main__':
    print('''
This module is meant to be imported rather than run.
For example, this code:
 import sev_seg
 myNumber = sevseg.getSevSegStr(42, 3)
 print(myNumber)

...will print 42, zero-padded to three digits:
 __        __ 
|  | |__|  __|
|__|    | |__ 
''')
