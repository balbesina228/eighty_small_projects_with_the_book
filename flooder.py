from sys import exit
from random import randint, choice

try:
    from bext import fg, bg, clear
except ImportError:
    print('''
    This program requires the bext module, which you
can install by following the instructions at
https://pypi.org/project/Bext/
''')
    exit()
board_width = 16
board_height = 14
moves_per_game = 20
heart =      chr(9829)  # ♥
diamond =    chr(9830)  # ♦
spade =      chr(9824)  # ♠
club =       chr(9827)  # ♣
ball =       chr(9679)  # •
triangle =   chr(9650)  # ▲
block =      chr(9608)  # █
left_right = chr(9472)  # ─
up_down =    chr(9474)  # │
down_right = chr(9484)  # ┌
down_left =  chr(9488)  # ┐
up_right =   chr(9492)  # └
up_left =    chr(9496)  # ┘
tile_types = (0, 1, 2, 3, 4, 5)
colors_map = {0: 'red', 1: 'green', 2: 'blue',
              3: 'yellow', 4: 'cyan', 5: 'purple'}
color_mode = 'color mode'
shapes_map =  {0: heart, 1: triangle, 2: diamond,
               3: ball, 4: club, 5: spade}
shape_mode = 'shape mode'

def get_new_board():
    board = {}
    for x in range(board_width):
        for y in range(board_height):
            board[(x, y)] = choice(tile_types)
    for i in range(board_width * board_height):
        x = randint(0, board_width - 2)
        y = randint(0, board_height - 1)
        board[(x + 1, y)] = board[(x, y)]
    return board

def display_board(board, display_mode):
    fg('white')
    print(down_right + (left_right * board_width) + down_left)
    for y in range(board_height):
        fg('white')
        if y == 0:
            print('>', end='')
        else:
            print(up_down, end='')
        for x in range(board_width):
            fg(colors_map[board[(x, y)]])
            if display_mode == color_mode:
                print(block, end='')
            elif display_mode == shape_mode:
                print(shapes_map[board[(x, y)]], end='')
        fg('white')
        print(up_down)
    print(up_right + (left_right * board_width) + up_left)

def ask_for_player_move(display_mode):
    while True:
        fg('white')
        print('Choose one of', end=' ')
        if display_mode == color_mode:
            fg('red')
            print('(R)ed', end=' ')
            fg('green')
            print('(G)reen', end=' ')
            fg('blue')
            print('(B)lue', end=' ')
            fg('yellow')
            print('(Y)ellow', end=' ')
            fg('cyan')
            print('(C)yan', end=' ')
            fg('purple')
            print('(P)urple', end=' ')
        elif display_mode == shape_mode:
            fg('red')
            print('(H)eart,', end=' ')
            fg('green')
            print('(T)riangle,', end=' ')
            fg('blue')
            print('(D)iamond,', end=' ')
            fg('yellow')
            print('(B)all,', end=' ')
            fg('cyan')
            print('(C)lub,', end=' ')
            fg('purple')
            print('(S)pade,', end=' ')
        fg('white')
        print('or QUIT:')
        response = input('> ').upper()
        if response == 'QUIT':
            print('Thanks for playing!')
            exit()
        if display_mode == color_mode and response in tuple('RGBYCP'):
            return {'R': 0, 'G': 1, 'B': 2,
                    'Y': 3, 'C': 4, 'P': 5}[response]
        if display_mode == shape_mode and response in tuple('HTDBCS'):
            return {'H': 0, 'T': 1, 'D': 2,
                    'B': 3, 'C': 4, 'S': 5}[response]

def change_tile(tile_type, board, x, y, char_to_change=None):
    if x == 0 and y == 0:
        char_to_change = board[(x, y)]
        if tile_type == char_to_change:
            return
    board[(x, y)] = tile_type
    if x > 0 and board[(x - 1, y)] == char_to_change:
        change_tile(tile_type, board, x - 1, y, char_to_change)
    if y > 0 and board[(x, y - 1)] == char_to_change:
        change_tile(tile_type, board, x, y - 1, char_to_change)
    if x < board_width - 1 and board[(x + 1, y)] == char_to_change:
        change_tile(tile_type, board, x + 1, y, char_to_change)
    if y < board_height - 1 and board[(x, y + 1)] == char_to_change:
        change_tile(tile_type, board, x, y + 1, char_to_change)

def has_won(board):
    tile = board[(0, 0)]
    for x in range(board_width):
        for y in range(board_height):
            if board[(x, y)] != tile:
                return False
    return True

def main():
    bg('black')
    fg('white')
    clear()
    print('''
Flooder, by Al Sweigart.
Set the upper left color/shape, which fills in all the
adjacent squares of that color/shape. Try to make the
entire board the same color/shape.
''')
    print('Do you want to play in colorblind mode? Y/N')
    response = input('> ').upper()
    if response.startswith('Y'):
        display_mode = shape_mode
    else:
        display_mode = color_mode
    game_board = get_new_board()
    moves_left = moves_per_game
    while True:
        display_board(game_board, display_mode)
        print('Moves left:', moves_left)
        player_move = ask_for_player_move(display_mode)
        change_tile(player_move, game_board, 0, 0)
        moves_left -= 1
        if has_won(game_board):
            display_board(game_board, display_mode)
            print('You have won!')
            break
        elif moves_left == 0:
            display_board(game_board, display_mode)
            print('You have run out of moves!')
            break

if __name__ == '__main__':
    main()
