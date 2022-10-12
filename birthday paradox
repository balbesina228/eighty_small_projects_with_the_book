from datetime import date, timedelta
from random import randint

def get_birthdays(num_of_birthdays):
    birthdays = []
    for i in range(num_of_birthdays):
        start_of_year = date(2000, 1, 1)
        random_number_of_birthdays = timedelta(randint(0, 364))
        birthday = start_of_year + random_number_of_birthdays
        birthdays.append(birthday)
    return birthdays

def get_match(birthdays):
    if len (birthdays) == len(set(birthdays)):
        return None
    for a, birthday_a in enumerate(birthdays):
        for b, birthday_b in enumerate(birthdays[a+1:]):
            if birthday_a == birthday_b:
                return birthday_a

print('''
Birthday Paradox, by Al Sweigart al@inventwithpython.com
The Birthday Paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.
(It's not actually a paradox, it's just a surprising result.)
''')

months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:
    print('How many birthday shall I generate?')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        num_birthdays = int(response)
        break

print(f'\nHere are {num_birthdays} birthdays:')
birthdays = get_birthdays(num_birthdays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(', ', end='')
    month_name = months[birthday.month - 1]
    date_text = f'{month_name} {birthday.day}'
    print(date_text, end='')

match = get_match(birthdays)
print('\nIn this simulation:')
if match != None:
    month_name = months[match.month - 1]
    date_text = f'{month_name} {match.day}'
    print(f'Multiple people have a birthday on {date_text}')
else:
    print('There are no matching birthdays.')

print(f'\nGenerating {num_birthdays} for 100000 times...')
input('Press Enter to begin...')

sim_match = 0
for i in range(100_000):
    if i % 10_000 == 0:
        print(f'{i} simulations run.')
    birthdays = get_birthdays(num_birthdays)
    if get_match(birthdays) != None:
        sim_match +=1
print('100 000 simulations run.')

probability = round(sim_match / 100_000 * 100, 2)
print(f'''
Out of 100,000 simulations of {num_birthdays} people, there was a
matching birthday in that group {sim_match} times. This means
that {num_birthdays} people have a {probability} % chance of
having a matching birthday in their group.
That\'s probably more than you would think!
''')
