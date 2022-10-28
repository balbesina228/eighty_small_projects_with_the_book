from random import randint

print('''Carrot in a Box, by Al Sweigart al@inventwithpython.com
This is a bluffing game for two human players. Each player has a box.
One box has a carrot in it. To win, you must have the box with the
carrot in it.

This is a very simple and silly game.

The first player looks into their box (the second player must close
their eyes during this). The first player then says "There is a carrot
in my box" or "There is not a carrot in my box". The second player then
gets to decide if they want to swap boxes or not.
''')
input('Enter anything to begin...')
player_one_name = input('Player 1, enter your name: ').capitalize()
player_two_name = input('Player 2, enter your name: ').capitalize()
player_names = player_one_name[:13].center(13) + ' ' + player_two_name[:13].center(13)

print(f'''
HERE ARE TWO BOXES:
  __________     __________
 /         /|   /         /|
+---------+ |  +---------+ |
|   RED   | |  |   GOLD  | |
|   BOX   | /  |   BOX   | /
+---------+/   +---------+/
''')
print(player_names, '\n')
print(f'{player_one_name}, you have a RED box in front of you.')
print(f'{player_two_name}, you have a GOLD box in front of you.\n')
print(f'{player_one_name}, you will get to look into your box.')
print(f'{player_two_name}, close your eyes and don\'t look!!!')
input(f'When {player_two_name} has closed their eyes, enter anything...\n')
print(f'{player_one_name}, here is the inside of your box:')

if randint(1,2) == 1:
    carrot_in_first_box = True
else:
    carrot_in_first_box = False
if carrot_in_first_box:
    print('''
   ___VV____
  |   VV    |
  |   VV    |
  |___||____|   __________
 /    ||   /|  /         /|
+---------+ | +---------+ |
|   RED   | | |   GOLD  | |
|   BOX   | / |   BOX   | /
+---------+/  +---------+/
  (carrot!)
    ''')
    print(player_names)
else:
     print('''
   _________
  |         |
  |         |
  |_________|   __________
 /         /|  /         /|
+---------+ | +---------+ |
|   RED   | | |   GOLD  | |
|   BOX   | / |   BOX   | /
+---------+/  +---------+/
(no carrot!)
     ''')
     print(player_names)

input('Enter anything to continue...')
print('\n'* 20)
print(f'{player_one_name}, tell {player_two_name} to open their eyes.')
input('Enter anything to continue...')
print(f'{player_one_name}, say one of the following sentences to {player_two_name}:')
print('''
1) There is a carrot in my box.
2) There is not a carrot in my box.\n''')
input('Then enter anything to continue...\n')

print(f'{player_two_name}, do you want to swap boxes with {player_one_name}? YES/NO')
while True:
    response = input('> ').upper()
    if not (response.startswith('Y') or response.startswith('N')):
        print(f'{player_two_name}, enter YES or NO.')
    else:
        break
first_box = 'RED '
second_box = 'GOLD'
if response.startswith('Y'):
    carrot_in_first_box = not carrot_in_first_box
    first_box, second_box = second_box, first_box
print(f'''
HERE ARE THE TWO BOXES:
  __________    __________
 /         /|  /         /|
+---------+ | +---------+ |
|   {first_box}  | | |   {second_box}  | |
|   BOX   | / |   BOX   | /
+---------+/ +---------+/
''')
input('Enter anything to reveal the winner...\n')
if carrot_in_first_box:
    print(f'''
   ___VV____     _________
  |   VV    |   |         |
  |   VV    |   |         |
  |___||____|   |_________|
 /    ||   /|  /         /|
+---------+ | +---------+ |
|   {first_box}  | | |   {second_box}  | |
|   BOX   | / |   BOX   | /
+---------+/  +---------+/
''')
else:
    print(f'''
   _________     ___VV____
  |         |   |   VV    |
  |         |   |   VV    |
  |_________|   |___||____|
 /         /|  /    ||   /|
+---------+ | +---------+ |
|   {first_box}  | | |   {second_box}  | |
|   BOX   | / |   BOX   | /
+---------+/  +---------+/
''')
print(player_names)
if carrot_in_first_box:
    print(f'{player_one_name} is the winner!')
else:
    print(f'{player_two_name} is the winner!')
print('Thanks for playing!')
