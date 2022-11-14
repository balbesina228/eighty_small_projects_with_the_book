from sys import exit, stdout
from random import choice, randint
from time import sleep

try:
    from bext import goto, fg, bg, clear, size
except ImportError:
    print('''
This program requires the bext module, which you
can install by following the instructions at
https://pypi.org/project/Bext/'
''')
    exit()

width, height = size()
width -= 1
num_kelp = 2
num_fish = 10
num_bubblers = 1
frames_per_second = 4
fish_types = [
{'right': ['><>'],          'left': ['<><']},
{'right': ['>||>'],         'left': ['<||<']},
{'right': ['>))>'],         'left': ['<[[<']},
{'right': ['>||o', '>||.'], 'left': ['o||<', '.||<']},
{'right': ['>))o', '>)).'], 'left': ['o[[<', '.[[<']},
{'right': ['>-==>'],        'left': ['<==-<']},
{'right': [r'>\\>'],        'left': ['<//<']},
{'right': ['><)))*>'],      'left': ['<*(((><']},
{'right': ['}-[[[*>'],      'left': ['<*]]]-{']},
{'right': [']-<)))b>'],     'left': ['<d(((>-[']},
{'right': ['><XXX*>'],      'left': ['<*XXX><']},
{'right': ['_.-._.-^=>', '.-._.-.^=>', '-._.-._^=>', '._.-._.^=>'],
'left': ['<=^-._.-._', '<=^.-._.-.',
'<=^_.-._.-', '<=^._.-._.']}
]

longest_fish_length = 10
left_edge = 1
right_edge = width - 1 - longest_fish_length
top_edge = 0
bottom_edge = height - 2

def get_random_color():
    return choice(('black', 'red', 'green', 'yellow',
                   'blue', 'purple', 'cyan', 'white'))

def generate_fish():
    fish_type = choice(fish_types)
    color_pattern = choice(('random', 'head-tail', 'single'))
    fish_length = len(fish_type['right'][0])
    if color_pattern == 'random':
        colors = []
        for i in range(fish_length):
            colors.append(get_random_color())
    if color_pattern == 'single' or color_pattern == 'head-tail':
        colors = [get_random_color()] * fish_length
    if color_pattern == 'head-tail':
        head_tail_color = get_random_color()
        colors[0] = head_tail_color
        colors[-1] = head_tail_color
    fish = {
'right':                fish_type['right'],
'left':                 fish_type['left'],
'colors':               colors,
'h_speed':              randint(1, 6),
'v_speed':              randint(5, 15),
'time_to_h_dir_change': randint(10, 60),
'time_to_v_dir_change': randint(2, 20),
'going_right':          choice([True, False]),
'going_down':           choice([True, False])
    }
    fish['x'] = randint(0, width - 1 - longest_fish_length)
    fish['y'] = randint(0, height - 2)
    return fish

def simulate_aquarium():
    global fishes, bubblers, bubbles, kelps, step
    for fish in fishes:
        if step % fish['h_speed']:
            if fish['going_right']:
                if fish['x'] != right_edge:
                    fish['x'] += 1
                else:
                    fish['going_right'] = False
                    fish['colors'].reverse()
            else:
                if fish['x'] != left_edge:
                    fish['x'] -= 1
                else:
                    fish['going_right'] = True
                    fish['colors'].reverse()
        fish['time_to_h_dir_change'] -= 1
        if fish['time_to_h_dir_change'] == 0:
            fish['time_to_h_dir_change'] = randint(10, 60)
            fish['going_right'] = not fish['going_right']

        if step % fish['v_speed']:
            if fish['going_down']:
                if fish['y'] != bottom_edge:
                    fish['y'] += 1
                else:
                    fish['going_down'] = False
                    fish['colors'].reverse()
            else:
                if fish['y'] != top_edge:
                    fish['y'] -= 1
                else:
                    fish['going_down'] = True
                    fish['colors'].reverse()
        fish['time_to_v_dir_change'] -= 1
        if fish['time_to_v_dir_change'] == 0:
            fish['time_to_v_dir_change'] = randint(10, 60)
            fish['going_down'] = not fish['going_down']

    for bubbler in bubblers:
        if randint(1, 5) == 1:
            bubbles.append({'x': bubbler, 'y': height - 2})
    for bubble in bubbles:
        dice_roll = randint(1, 6)
        if dice_roll == 1 and bubble['x'] != left_edge:
            bubble['x'] -= 1
        elif dice_roll == 2 and bubble['x'] != right_edge:
            bubble['x'] += 1
        bubble['y'] -= 1
    for i in range(len(bubbles) - 1, -1, -1):
        if bubbles[i]['y'] == top_edge:
            del bubbles[i]
    for kelp in kelps:
        for i, kelp_segment in enumerate(kelp['segments']):
            if randint(1, 20) == 1:
                if kelp_segment == '(':
                    kelp['segments'][i] = ')'
                elif kelp_segment == ')':
                    kelp['segments'][i] = '('

def draw_aquarium():
    global fishes, bubblers, bubbles, kelps, step
    fg('white')
    goto(0, 0)
    print('Fish Tank, by Al Sweigart. Ctrl-C to quit')
    fg('white')
    for bubble in bubbles:
        goto(bubble['x'], bubble['y'])
        print(choice(('o', 'O')), end='')
    for fish in fishes:
        goto(fish['x'], fish['y'])

        if fish['going_right']:
            fish_text = fish['right'][step % len(fish['right'])]
        else:
            fish_text = fish['left'][step % len(fish['left'])]

        for i, fish_part in enumerate(fish_text):
            fg(fish['colors'][i])
            print(fish_part, end='')
    fg('green')
    for kelp in kelps:
        for i, kelp_segment in enumerate(kelp['segments']):
            if kelp_segment == '(':
                goto(kelp['x'], bottom_edge - i)
            elif kelp_segment == ')':
                goto(kelp['x'] + 1, bottom_edge - i)
    fg('yellow')
    goto(0, height - 1)
    print(chr(9617) * (width - 1), end='')
    stdout.flush()

def clear_aquarium():
    global fishes, bubblers, bubbles, kelps
    for bubble in bubbles:
        goto(bubble['x'], bubble['y'])
        print(' ', end='')
    for fish in fishes:
        goto(fish['x'], fish['y'])
        print(' ' * len(fish['left'][0]), end='')
    for kelp in kelps:
        for i, kelp_segment in enumerate(kelp['segments']):
            goto(kelp['x'], height - 2 - i)
            print('  ', end='')
    stdout.flush()

def main():
    global fishes, bubblers, bubbles, kelps, step
    bg('black')
    clear()
    fishes = []
    for i in range(num_fish):
        fishes.append(generate_fish())
    bubblers = []
    for i in range(num_bubblers):
        bubblers.append(randint(left_edge, right_edge))
    bubbles = []
    kelps = []
    for i in range(num_kelp):
        kelp_x = randint(left_edge, right_edge)
        kelp = {'x': kelp_x, 'segments': []}
        for i in range(randint(6, height - 1)):
            kelp['segments'].append(choice(['(', ')']))
        kelps.append(kelp)
    step = 1
    while True:
        simulate_aquarium()
        draw_aquarium()
        sleep(1 / frames_per_second)
        clear_aquarium()
        step += 1

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
