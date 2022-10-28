from datetime import timedelta, date

months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

print('Enter a year.')
while True:
    response = input('> ')
    if response.isdecimal():
        year = int(response)
        break
    print('Incorrect format.')
    continue
print('Enter a month.')
while True:
    response = input('> ')
    if response.isdecimal() and 1 <= int(response) <= 12:
        month = int(response)
        break
    print('Incorrect format.')
    continue

week_separator = '+----------' * 7
blank_row = '|' + (' ' * 10)
cal_text = ''
cal_text += (' ' * 34) + months[month - 1] + ' ' + str(year) + '\n'
cal_text += '|  - SUN - |  - MON - |  - TUE - |  - WED - |  - THU - |  - FRI - |  - SAT - | \n'

current_date = date(year, month, 1)
while current_date.weekday() != 6:
    current_date -= timedelta(days=1)

while True:
    cal_text += week_separator + '+\n'
    for i in range(7):
        if current_date.day == 9 and current_date.month == 5:
                cal_text += '|' + str(current_date.day).rjust(2) + ' Win Day'
        else:
            cal_text += '|' + str(current_date.day).rjust(2) + '        '
        current_date += timedelta(days=1)
    cal_text += '|\n'
    cal_text += blank_row * 7 + '|\n'

    if current_date.month != month:
        cal_text += week_separator + '+'
        break
print(cal_text)
