from sys import exit

print('''
Fibonacci Sequence, by Al Sweigart.

The Fibonacci sequence begins with 0 and 1, and the next number is the
sum of the previous two numbers. The sequence continues forever:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987...
''')

while True:
    while True:
        print('Enter the Nth Fibonacci number you wish to calculate',
              '(such as 5, 10, 100, 9999) or "QUIT" to quit.')
        response = input('> ').upper()
        if response == 'QUIT':
            print('Thanks for playing!')
            exit()
        if response.isdecimal() and int(response) != 0:
            nth = int(response)
            break
        print('Wrong format.')
        continue

    print()
    if nth == 1:
        print('0\nThe #1 Fibonacci number is 0.')
        continue
    elif nth == 2:
        print('0, 1\nThe #2 Fibonacci number is 1.')
        continue
    if nth >= 10000:
        print('''
WARNING: This will take a while to display on the
screen. If you want to quit this program before it is
done, press Ctrl-C.
''')
        input('Press Enter to begin...')
    second_to_last_number = 0
    last_number = 1
    fib_numbers_calculated = 2
    print('0, 1, ', end='')
    while True:
        next_number = second_to_last_number + last_number
        fib_numbers_calculated += 1
        print(next_number, end='')
        if fib_numbers_calculated == nth:
            print(f'\n\nThe #{nth} Fibonacci number is {next_number}.')
            break
        print(', ', end='')
        second_to_last_number = last_number
        last_number = next_number
