from sys import exit

empty_space = '.'
player_x = 'x'
player_o = 'o'
board_width = 7
board_height = 6
column_labels = ('1', '2', '3', '4', '5', '6', '7')
assert len(column_labels) == board_width


def main():
    print('''
Four in a Row, by Al Sweigart.

Two players take turns dropping tiles into one of seven columns, trying
to make four in a row horizontally, vertically, or diagonally.
''')
    game_board = get_new_board()
    player_turn = player_x
    while True:
        display_board(game_board)
        player_move = ask_for_player_move(player_turn, game_board)
        game_board[player_move] = player_turn
        if is_winner(player_turn, game_board):
            display_board(game_board)
            print('Player', player_turn, 'has won!')
            exit()
        elif is_full(game_board):
            display_board(game_board)
            print('There is a tie!')
            exit()
        if player_turn == player_x:
            player_turn = player_o
        elif player_turn == player_o:
            player_turn = player_x


def get_new_board():
    board = {}
    for column_index in range(board_width):
        for row_index in range(board_height):
            board[(column_index, row_index)] = empty_space
    return board


def display_board(board):
    tile_chars = []
    for row_index in range(board_height):
        for column_index in range(board_width):
            tile_chars.append(board[(column_index, row_index)])
    print('''
    +-------+
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    |{}{}{}{}{}{}{}|
    +-------+
    '''.format(*tile_chars))


def ask_for_player_move(player_tile, board):
    while True:
        print(f'Player {player_tile}, enter a column or QUIT:')
        response = input('> ').upper().strip()
        if response == 'QUIT':
            print('Thanks for playing!')
            exit()
        if response not in column_labels:
            print(f'Enter a number from 1 to {board_width}.')
            continue
        column_index = int(response) - 1
        if board[(column_index, 0)] != empty_space:
            print('That column is full, select another one.')
        for row_index in range(board_height - 1, -1, -1):
            if board[(column_index, row_index)] == empty_space:
                return (column_index, row_index)


def is_full(board):
    for row_index in range(board_height):
        for column_index in range(board_width):
            if board[(column_index, row_index)] == empty_space:
                return False
    return True


def is_winner(player_tile, board):
    for column_index in range(board_width - 3):
        for row_index in range(board_height):
            tile_1 = board[(column_index, row_index)]
            tile_2 = board[(column_index + 1, row_index)]
            tile_3 = board[(column_index + 2, row_index)]
            tile_4 = board[(column_index + 3, row_index)]
            if tile_1 == tile_2 == tile_3 == tile_4 == player_tile:
                return True
    for column_index in range(board_width):
        for row_index in range(board_height - 3):
            tile_1 = board[(column_index, row_index)]
            tile_2 = board[(column_index, row_index + 1)]
            tile_3 = board[(column_index, row_index + 2)]
            tile_4 = board[(column_index, row_index + 3)]
            if tile_1 == tile_2 == tile_3 == tile_4 == player_tile:
                return True
    for column_index in range(board_width - 3):
        for row_index in range(board_height - 3):
            tile_1 = board[(column_index, row_index)]
            tile_2 = board[(column_index + 1, row_index + 1)]
            tile_3 = board[(column_index + 2, row_index + 2)]
            tile_4 = board[(column_index + 3, row_index + 3)]
            if tile_1 == tile_2 == tile_3 == tile_4 == player_tile:
                return True
            tile_1 = board[(column_index + 3, row_index)]
            tile_2 = board[(column_index + 2, row_index + 1)]
            tile_3 = board[(column_index + 1, row_index + 2)]
            tile_4 = board[(column_index, row_index + 3)]
            if tile_1 == tile_2 == tile_3 == tile_4 == player_tile:
                return True
    return False


if __name__ == '__main__':
    main()
