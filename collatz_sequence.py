from time import sleep
from sys import exit

print('Collatz sequence.')
print('Enter a natural number.')
response = input('> ')
if not response.isdecimal() and response > 0:
    print('Incorrect format.')
    exit()
else:
    n = int(response)

print('''
The Collatz sequence is a sequence of numbers produced from a starting
number n, following three rules:
If n is even, the next n will be n // 2,
if n is odd, the next n will be 3n + 1,
if n is 1, the sequence stops.
''')

print(f'Start:\n{n}', end='')
while n != 1:
    if n % 2 == 0:
        n = n // 2
        print(f', {n}', end='', flush=True)
        sleep(0.1)
    elif n % 2 == 1:
        n = (3 * n) + 1
        print(f', {n}', end='', flush=True)
        sleep(0.1)
