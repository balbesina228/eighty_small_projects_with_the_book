from random import randint, choice
from time import sleep, time

dice_width = 9
dice_height = 5
canvas_width = 79
canvas_height = 24 - 3
quiz_duration = 30
min_dice = 2
max_dice = 6
reward = 4
penalty = 1
assert max_dice <= 14

d1 = (['+-------+',
       '|       |',
       '|   O   |',
       '|       |',
       '+-------+'], 1)
d2a = (['+-------+',
        '| O     |',
        '|       |',
        '|     O |',
        '+-------+'], 2)
d2b = (['+-------+',
        '|     O |',
        '|       |',
        '| O     |',
        '+-------+'], 2)
d3a = (['+-------+',
        '| O     |',
        '|   O   |',
        '|     O |',
        '+-------+'], 3)
d3b = (['+-------+',
        '|     O |',
        '|   O   |',
        '| O     |',
        '+-------+'], 3)
d4 = (['+-------+',
       '| O   O |',
       '|       |',
       '| O   O |',
       '+-------+'], 4)
d5 = (['+-------+',
       '| O   O |',
       '|   O   |',
       '| O   O |',
       '+-------+'], 5)
d6a = (['+-------+',
        '| O   O |',
        '| O   O |',
        '| O   O |',
        '+-------+'], 6)
d6b = (['+-------+',
        '| O O O |',
        '|       |',
        '| O O O |',
        '+-------+'], 6)
all_dice = [d1, d2a, d2b, d3a, d3b, d4, d5, d6a, d6b]
print(f'''
Dice Math, by Al Sweigart.
Add up the sides of all the dice displayed on the screen. You have
{quiz_duration} seconds to answer as many as possible. You get {reward} points for each
correct answer and lose {penalty} point for each incorrect answer.
''')
input('Enter anything to begin... ')

correct_answers = 0
incorrect_answers = 0
start_time = time()

while time() < start_time + quiz_duration:
    sum_answer = 0
    dice_faces = []
    for i in range(randint(min_dice, max_dice)):
        die = choice(all_dice)
        dice_faces.append(die[0])
        sum_answer += die[1]

        top_left_dice_corners = []

        for i in range(len(dice_faces)):
            while True:
                left = randint(0, canvas_width - 1 - dice_width)
                top = randint(0, canvas_height - 1 - dice_height)

                top_left_x = left
                top_left_y = top
                bottom_left_x = left
                bottom_left_y = top + dice_height
                top_right_x = left + dice_width
                top_right_y = top
                bottom_right_x = left + dice_width
                bottom_right_y = top + dice_height

                overlaps = False
                for prev_die_left, prev_die_top in top_left_dice_corners:
                    prev_die_right = prev_die_left + dice_width
                    prev_die_bottom = prev_die_top + dice_height
                    for corner_x, corner_y in ((top_left_x, top_left_y),
                                               (top_right_x, top_right_y),
                                               (bottom_left_x, bottom_left_y),
                                               (bottom_right_x, bottom_right_y)):
                        if (prev_die_left <= corner_x < prev_die_right
                                and prev_die_top <= corner_y < prev_die_bottom):
                            overlaps = True
                if not overlaps:
                    top_left_dice_corners.append((left, top))
                    break
    canvas = {}
    for i, (die_left, die_top) in enumerate(top_left_dice_corners):
        die_face = dice_faces[i]
        for dx in range(dice_width):
            for dy in range(dice_height):
                canvas_x = die_left + dx
                canvas_y = die_top + dy
                canvas[(canvas_x, canvas_y)] = die_face[dy][dx]

    for cy in range(canvas_height):
        for cx in range(canvas_width):
            print(canvas.get((cx, cy), ''), end='')
        print()

    response = input('Enter the sum: ').strip()
    if response.isdecimal and int(response) == sum_answer:
        correct_answers += 1
    else:
        print('Incorrect, the answer is', sum_answer)
        sleep(2)
        incorrect_answers += 1

score = (correct_answers * reward) - (incorrect_answers * penalty)
print('Correct:   ', correct_answers)
print('Incorrect: ', incorrect_answers)
print('Score:     ', score)
