from sys import exit
from shutil import get_terminal_size

up_down_char =         chr(9474)  # │
left_right_char =      chr(9472)  # ─
down_right_char =      chr(9484)  # ┌
down_left_char =       chr(9488)  # ┐
up_right_char =        chr(9492)  # └
up_left_char =         chr(9496)  # ┘
up_down_right_char =   chr(9500)  # ├
up_down_left_char =    chr(9508)  # ┤
down_left_right_char = chr(9516)  # ┬
up_left_right_char =   chr(9524)  # ┴
cross_char =           chr(9532)  # ┼

canvas_width, canvas_height = get_terminal_size()
canvas_width -= 1
canvas_height -= 5
canvas = {}
cursor_x = 0
cursor_y = 0

def get_canvas_string(canvas_data, cx, cy):
    canvas_str = ''
    for row_number in range(canvas_height):
        for column_number in range(canvas_width):
            if column_number == cx and row_number == cy:
                canvas_str += '#'
                continue
            cell = canvas_data.get((column_number, row_number))
            if cell in (set(['W', 'S']), set(['W']), set(['S'])):
                canvas_str += up_down_char
            elif cell in (set(['A', 'D']), set(['A']), set(['D'])):
                canvas_str += left_right_char
            elif cell == set(['S', 'D']):
                canvas_str += down_right_char
            elif cell == set(['S', 'A']):
                canvas_str += down_left_char
            elif cell == set(['W', 'D']):
                canvas_str += up_right_char
            elif cell == set(['W', 'A']):
                canvas_str += up_left_char
            elif cell == set(['W', 'S', 'D']):
                canvas_str += up_down_right_char
            elif cell == set(['W', 'S', 'A']):
                canvas_str += up_down_left_char
            elif cell == set(['A', 'S', 'D']):
                canvas_str += down_left_right_char
            elif cell == set(['W', 'A', 'D']):
                canvas_str += up_left_right_char
            elif cell == set(['W', 'A', 'S', 'D']):
                canvas_str += cross_char
            elif cell == None:
                canvas_str += ' '
        canvas_str += '\n'
    return canvas_str
moves = []
while True:
    print(get_canvas_string(canvas, cursor_x, cursor_y))
    print('''
WASD keys to move, H for help, C to clear,
F to save, or QUIT.
''')
    response = input('> ').upper()
    if response == 'QUIT':
        print('Thanks for playing!')
        exit()
    elif response == 'H':
        print('''
Enter W, A, S, and D characters to move the cursor and
draw a line behind it as it moves. For example, ddd
draws a line going right and sssdddwwwaaa draws a box.
You can save your drawing to a text file by entering F.
''')
        input('Press Enter to return to the program...')
        continue
    elif response == 'C':
        canvas = {}
        moves.append('C')
    elif response == 'F':
        try:
            print('Enter filename to save to:')
            filename = input('> ')
            if not filename.endswith('.txt'):
                filename += '.txt'
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(''.join(moves) + '\n')
                file.write(get_canvas_string(canvas, None, None))
        except:
            print('ERROR. Could not save the file.')
    for command in response:
        if command not in ('W', 'A', 'S', 'D'):
            continue
        moves.append(command)
        if canvas == {}:
            if command in ('W', 'S'):
                canvas[(cursor_x, cursor_y)] = set(['W', 'S'])
            elif command in ('A', 'D'):
                canvas[(cursor_x, cursor_y)] = set(['A', 'D'])
        if command == 'W' and cursor_y > 0:
            canvas[(cursor_x, cursor_y)].add(command)
            cursor_y -= 1
        elif command == 'S' and cursor_y < canvas_height - 1:
            canvas[(cursor_x, cursor_y)].add(command)
            cursor_y += 1
        elif command == 'A' and cursor_x > 0:
            canvas[(cursor_x, cursor_y)].add(command)
            cursor_x -= 1
        elif command == 'D' and cursor_x < canvas_width - 1:
            canvas[(cursor_x, cursor_y)].add(command)
            cursor_x += 1
        else:
            continue
        if (cursor_x, cursor_y) not in canvas:
            canvas[(cursor_x, cursor_y)] = set()

        if command == 'W':
            canvas[(cursor_x, cursor_y)].add('S')
        if command == 'S':
            canvas[(cursor_x, cursor_y)].add('W')
        if command == 'A':
            canvas[(cursor_x, cursor_y)].add('D')
        if command == 'D':
            canvas[(cursor_x, cursor_y)].add('A')
