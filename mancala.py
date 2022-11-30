from sys import exit

player_1_pits = ('A', 'B', 'C', 'D', 'E', 'F')
player_2_pits = ('G', 'H', 'I', 'J', 'K', 'L')
opposite_pit = {'A': 'G', 'B': 'H', 'C': 'I', 'D': 'J', 'E': 'K', 'F': 'L',
                'G': 'A', 'H': 'B', 'I': 'C', 'J': 'D', 'K': 'E', 'L': 'F'}
next_pit = {'A': 'B', 'B': 'C', 'C': 'D', 'D': 'E', 'E': 'F', 'F': '1', '1': 'L',
            'L': 'K', 'K': 'J', 'J': 'I', 'I': 'H', 'H': 'G', 'G': '2', '2': 'A'}
pit_labels = 'ABCDEF1LKJIHG2'
starting_num_of_seeds = 4


def main():
    print('''
Mancala, by Al Sweigart al@inventwithpython.com

The ancient two-player seed-sowing game. Grab the seeds from a pit on
your side and place one in each following pit, going counterclockwise
and skipping your opponent's store. If your last seed lands in an empty
pit of yours, move the opposite pit's seeds into that pit. The
goal is to get the most seeds in your store on the side of the board.
If the last placed seed is in your store, you get a free turn.

The game ends when all of one player's pits are empty. The other player
claims the remaining seeds for their store, and the winner is the one
with the most seeds.

More info at https://en.wikipedia.org/wiki/Mancala
''')
    input('Press Enter to begin...')
    game_board = get_new_board()
    player_turn = '1'
    while True:
        print('\n' * 60)
        display_board(game_board)
        player_move = ask_for_player_move(player_turn, game_board)
        player_turn = make_move(game_board, player_turn, player_move)
        winner = check_for_winner(game_board)
        if winner == '1' or winner == '2':
            display_board(game_board)
            print('Player', winner, 'has won!')
            exit()
        elif winner == 'tie':
            display_board(game_board)
            print('There is a tie!')
            exit()


def get_new_board():
    s = starting_num_of_seeds
    board = {k: 4 for k in next_pit}
    board['1'], board['2'] = 0, 0
    return board


def display_board(board):
    seed_amounts = []
    for pit in 'GHIJKL21ABCDEF':
        num_seeds_in_this_pit = str(board[pit]).rjust(2)
        seed_amounts.append(num_seeds_in_this_pit)
    print('''
+------+------+--<<<<<-Player 2----+------+------+------+
2      |G     |H     |I     |J     |K     |L     |      1
       |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |
S      |      |      |      |      |      |      |      S
T  {}  +------+------+------+------+------+------+  {}  T
O      |A     |B     |C     |D     |E     |F     |      O
R      |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |      R
E      |      |      |      |      |      |      |      E
+------+------+------+-Player 1->>>>>-----+------+------+
'''.format(*seed_amounts))


def ask_for_player_move(player_turn, board):
    while True:
        if player_turn == '1':
            print('Player one, choose move: A-F (or QUIT)')
        elif player_turn == '2':
            print('Player two, choose move: G-L (or QUIT)')
        response = input('> ').upper().strip()
        if response == 'QUIT':
            print('Thanks for playing!')
            exit()
        if (player_turn == '1' and response not in player_1_pits) or \
            (player_turn == '2' and response not in player_2_pits):
            print('Pick a letter on your side of the board.')
            continue
        if board.get(response) == 0:
            print('Pick a non-empty pit.')
            continue
        return response


def make_move(board, player_turn, pit):
    seeds_to_sow = board[pit]
    board[pit] = 0
    while seeds_to_sow > 0:
        pit = next_pit[pit]
        if (player_turn == '1' and next_pit == '2') or \
                (player_turn == '2' and next_pit == '1'):
            continue
        board[pit] += 1
        seeds_to_sow -= 1
    if (pit == '1' == player_turn) or (pit == '2' == player_turn):
        return player_turn
    if player_turn == '1' and pit in player_1_pits and board[pit] == 1:
        op_pit = opposite_pit[pit]
        board['1'] += board[op_pit]
        board[op_pit] = 0
    elif player_turn == '2' and pit in player_2_pits and board[pit] == 1:
        op_pit = opposite_pit[pit]
        board['2'] += board[op_pit]
        board[op_pit] = 0
    if player_turn == '1':
        return '2'
    elif player_turn == '2':
        return '1'


def check_for_winner(board):
    player_1_total = board['A'] + board['B'] + board['C']
    player_1_total += board['D'] + board['E'] + board['F']
    player_2_total = board['G'] + board['H'] + board['I']
    player_2_total += board['J'] + board['K'] + board['L']
    if player_1_total == 0:
        board['2'] += player_2_total
        for pit in player_2_pits:
            board[pit] = 0
    elif player_2_total == 0:
        board['1'] += player_1_total
        for pit in player_1_pits:
            board[pit] = 0
    else:
        return 'no winner'
    if board['1'] > board['2']:
        return '1'
    elif board['2'] > board['1']:
        return '2'
    else:
        return 'tie'



if __name__ == '__main__':
    main()
