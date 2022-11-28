from random import shuffle, randint

gold = 'gold'
silver = 'silver'
bronze = 'bronze'
star_face = [
"+-----------+",
"|     .     |",
"|    ,O,    |",
"| 'ooOOOoo' |",
"|   `OOO`   |",
"|   O' 'O   |",
"+-----------+"
]
skull_face = [
'+-----------+',
'|    ___    |',
'|   /   \\   |',
'|  |() ()|  |',
'|   \\ ^ /   |',
'|    VVV    |',
'+-----------+'
]
question_face = [
'+-----------+',
'|           |',
'|           |',
'|     ?     |',
'|           |',
'|           |',
'+-----------+'
]
face_width = 13
face_height = 7
print('''
Lucky Stars, by Al Sweigart

A "press your luck" game where you roll dice with Stars, Skulls, and
Question Marks.

On your turn, you pull three random dice from the dice cup and roll
them. You can roll Stars, Skulls, and Question Marks. You can end your
turn and get one point per Star. If you choose to roll again, you keep
the Question Marks and pull new dice to replace the Stars and Skulls.
If you collect three Skulls, you lose all your Stars and end your turn.

When a player gets 13 points, everyone else gets one more turn before
the game ends. Whoever has the most points wins.

There are 6 Gold dice, 4 Silver dice, and 3 Bronze dice in the cup.
Gold dice have more Stars, Bronze dice have more Skulls, and Silver is even.

How many players are there?
''')
while True:
    response = input('> ')
    if response.isdecimal() and int(response) > 1:
        num_players = int(response)
        break
    print('Enter a number larger than one.')
player_names = []
player_scores = {}
for i in range(num_players):
    while True:
        print(f"What is player #{i + 1}'s name?")
        response = input('> ').capitalize()
        if response != '' and response not in player_names:
            player_names.append(response)
            player_scores[response] = 0
            break
        print('Enter a unique name.')
print()
turn = 0
end_game_with = None
while True:
    print('\nScores:', end='')
    for i, name in enumerate(player_names):
        print(f'{name} = {str(player_scores[name])}', end='')
        if i != len(player_names) - 1:
            print(', ', end='')
    print('\n')
    stars = 0
    skulls = 0
    cup = ([gold] * 6) + ([silver] * 4) + ([bronze] * 3)
    hand = []
    print(f"It's {player_names[turn]}'s turn")
    while True:
        if (3 - len(hand)) > len(cup):
            print(f"There are not enough dice left to {player_names[turn]}'s turn.")
            break
        shuffle(cup)
        while len(hand) < 3:
            hand.append(cup.pop())
        roll_results = []
        for dice in hand:
            roll = randint(1, 6)
            if dice == gold:
                if 1 <= roll <= 3:
                    roll_results.append(star_face)
                    stars += 1
                elif 4 <= roll <= 5:
                    roll_results.append(question_face)
                else:
                    roll_results.append(skull_face)
                    skulls += 1
            if dice == silver:
                if 1 <= roll <= 2:
                    roll_results.append(star_face)
                    stars += 1
                elif 3 <= roll <= 4:
                    roll_results.append(skull_face)
                    skulls += 1
                else:
                    roll_results.append(question_face)
            if dice == bronze:
                if roll == 1:
                    roll_results.append(star_face)
                    stars += 1
                elif 2 <= roll <= 4:
                    roll_results.append(skull_face)
                    skulls += 1
                else:
                    roll_results.append(question_face)
        for line_num in range(face_height):
            for dice_num in range(3):
                print(roll_results[dice_num][line_num] + ' ', end='')
            print()
        for dice_type in hand:
            print(dice_type.center(face_width) + ' ', end='')
        print(f'\nStars collected: {stars}, Skulls collected: {skulls}')
        if skulls >= 3:
            print("3 or more skulls means you've lost your stars.")
            input('Press Enter to continue...')
            break
        print(player_names[turn] + ', do you want to roll again? (Y/N)')
        while True:
            response = input('> ').upper()
            if response != '' and response[0] in ('Y', 'N'):
                break
            print('Enter Y or N')
        if response.startswith('N'):
            print(player_names[turn], 'got', stars, 'stars!')
            player_scores[player_names[turn]] += stars
            if end_game_with == None and player_scores[player_names[turn]] >= 13:
                print('\n\n' + '!' * 60)
                print(player_names[turn], 'reached 13 points!')
                print('Everyone else will get one more turn!')
                print('!' * 60, '\n\n')
                end_game_with = player_names[turn]
            input('Press Enter to continue...')
            break
        next_hand = []
        for i in range(3):
            if roll_results[i] == question_face:
                next_hand.append(hand[i])
        hand = next_hand
    turn = (turn + 1) % num_players
    if end_game_with == player_names[turn]:
        break
print('The game has ended...\n')
print('Scores:', end='')
for i, name in enumerate(player_names):
    print(f'{name} = {str(player_scores[name])}', end='')
    if i != len(player_names) - 1:
        print(', ', end='')
print('\n')
highest_score = 0
winners = []
for name, score in player_scores.items():
    if score > highest_score:
        highest_score = score
        winners = [name]
    elif score == highest_score:
        winners.append(name)
if len(winners) == 1:
    print(f'The winner is {winners[0]}!')
else:
    print(f'The winners are {", ".join(winners)}')
print('Thanks for playing!')
