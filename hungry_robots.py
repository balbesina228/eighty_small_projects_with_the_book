from random import randint
from sys import exit

width = 40
height = 20
num_robots = 10
num_teleports = 2
num_dead_robots = 2
num_walls = 100
empty_space = ' '
player = '@'
robot = 'R'
dead_robot = 'X'
wall = chr(9617)


def main():
    print(f'''
Hungry Robots, by Al Sweigart

You are trapped in a maze with hungry robots! You don't know why robots
need to eat, but you don't want to find out. The robots are badly
programmed and will move directly toward you, even if blocked by walls.
You must trick the robots into crashing into each other (or dead robots)
without being caught. You have a personal teleporter device, but it only
has enough battery for {num_teleports} trips. Keep in mind, you and robots can slip
through the corners of two diagonal walls!
    ''')
    input('Press Enter to begin...')
    board = get_new_board()
    robots = add_robots(board)
    player_position = get_random_empty_space(board, robots)
    while True:
        display_board(board, robots, player_position)
        if len(robots) == 0:
            print('All the robots have crashed into each other and you'
                  ' lived to tell the tale. Good job!')
            exit()
        player_position = ask_for_player_move(board, robots, player_position)
        robots = move_robots(board, robots, player_position)
        for x, y in robots:
            if (x, y) == player_position:
                display_board(board, robots, player_position)
                print('You have been caught by a robot!')
                exit()


def get_new_board():
    board = {'teleports': num_teleports}
    for x in range(width):
        for y in range(height):
            board[(x, y)] = empty_space
    for x in range(width):
        board[(x, 0)] = wall
        board[(x, height - 1)] = wall
    for y in range(height):
        board[(0, y)] = wall
        board[(width - 1, y)] = wall
    for _ in range(num_walls):
        x, y = get_random_empty_space(board, [])
        board[(x, y)] = wall
    for _ in range(num_dead_robots):
        x, y = get_random_empty_space(board, [])
        board[(x, y)] = dead_robot
    return board


def add_robots(board):
    robots = []
    for _ in range(num_robots):
        x, y = get_random_empty_space(board, robots)
        robots.append((x, y))
    return robots


def get_random_empty_space(board, robots):
    while True:
        random_x = randint(1, width - 2)
        random_y = randint(1, height - 2)
        if is_empty(random_x, random_y, board, robots):
            break
    return random_x, random_y


def is_empty(x, y, board, robots):
    return board[(x, y)] == empty_space and (x, y) not in robots


def display_board(board, robots, player_position):
    for y in range(height):
        for x in range(width):
            if board[(x, y)] == wall:
                print(wall, end='')
            elif board[(x, y)] == dead_robot:
                print(dead_robot, end='')
            elif (x, y) == player_position:
                print(player, end='')
            elif (x, y) in robots:
                print(robot, end='')
            else:
                print(empty_space, end='')
        print()


def ask_for_player_move(board, robots, player_position):
    player_x, player_y = player_position

    q = 'Q' if is_empty(player_x - 1, player_y - 1, board, robots) else ' '
    w = 'W' if is_empty(player_x,     player_y - 1, board, robots) else ' '
    e = 'E' if is_empty(player_x + 1, player_y - 1, board, robots) else ' '
    d = 'D' if is_empty(player_x + 1, player_y,     board, robots) else ' '
    c = 'C' if is_empty(player_x + 1, player_y + 1, board, robots) else ' '
    z = 'Z' if is_empty(player_x - 1, player_y + 1, board, robots) else ' '
    x = 'X' if is_empty(player_x,     player_y + 1, board, robots) else ' '
    a = 'A' if is_empty(player_x - 1, player_y,     board, robots) else ' '
    all_moves = (q + w + e + d + c + z + x + a + 'S')

    while True:
        print(f'(T)eleports remaining: {board["teleports"]}')
        print(f'                    ({q})({w})({e})')
        print(f'                    ({a})(S)({d})')
        print(f'Enter move or QUIT: ({z})({x})({c})')
        move = input('> ').upper()
        if move == 'QUIT':
            print('Thanks for playing!')
            exit()
        elif move == 'T' and board['teleports'] > 0:
            board['teleports'] -= 1
            return get_random_empty_space(board, robots)
        elif move != '' and move in all_moves:
            return {
                'Q': (player_x - 1, player_y - 1),
                'W': (player_x, player_y - 1),
                'E': (player_x + 1, player_y - 1),
                'D': (player_x + 1, player_y),
                'C': (player_x + 1, player_y + 1),
                'X': (player_x, player_y + 1),
                'Z': (player_x - 1, player_y + 1),
                'A': (player_x - 1, player_y),
                'S': (player_x, player_y),
            }[move]


def move_robots(board, robot_positions, player_position):
    player_x, player_y = player_position
    next_robot_positions = []
    while len(robot_positions) > 0:
        robot_x, robot_y = robot_positions[0]
        if robot_x < player_x:
            move_x = 1
        elif robot_x > player_x:
            move_x = -1
        elif robot_x == player_x:
            move_x = 0

        if robot_y < player_y:
            move_y = 1
        elif robot_y > player_y:
            move_y = -1
        elif robot_y == player_y:
            move_y = 0

        if board[(robot_x + move_x, robot_y + move_y)] == wall:
            if board[(robot_x + move_x, robot_y)] == empty_space:
                move_y = 0
            elif board[(robot_x, robot_y + move_y)] == empty_space:
                move_x = 0
            else:
                move_x, move_y = 0, 0
        new_robot_x = robot_x + move_x
        new_robot_y = robot_y + move_y

        if (board[(new_robot_x, new_robot_y)] == dead_robot or
            board[(robot_x, robot_y)] == dead_robot):
            del robot_positions[0]
            continue
        if (new_robot_x, new_robot_y) in next_robot_positions:
            board[(new_robot_x, new_robot_y)] = dead_robot
            next_robot_positions.remove((new_robot_x, new_robot_y))
        else:
            next_robot_positions.append((new_robot_x, new_robot_y))

        del robot_positions[0]
    return next_robot_positions


if __name__ == '__main__':
    main()
