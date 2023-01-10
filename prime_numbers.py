from math import sqrt
from sys import exit


def main():
    print('''
Prime Numbers, by Al Sweigart al@inventwithpython.com
Prime numbers are numbers that are only evenly divisible by
one and themselves. They are used in a variety of practical
applications, but cannot be predicted. They must be
calculated one at a time.\n
    ''')
    while True:
        print('Enter a number to start searching for primes from: ')
        response = input('> ')
        if response.isdecimal():
            num = int(response)
            break
    input('Press Ctrl-C at anytime to quit. Press Enter to begin...')
    while True:
        if is_prime(num):
            print(str(num), end=', ', flush=True)
        num += 1


def is_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True

    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
