from sys import exit
from random import randint, choice, sample

garbage_chars = '~!@#$%^&*()_+-={}[]|;:,.<>?/'
with open('words.txt') as file:
    words = file.readlines()
for i in range(len(words)):
    words[i] = words[i].strip().upper()


def main():
    print('''
Hacking Minigame, by Al Sweigart.
Find the password in the computer's memory. You are given clues after
each guess. For example, if the secret password is MONITOR but the
player guessed CONTAIN, they are given the hint that 2 out of 7 letters
were correct, because both MONITOR and CONTAIN have the letter O and N
as their 2nd and 3rd letter. You get four guesses.\n
''')
    input('Press Enter to begin...')
    game_words = get_words()
    computer_memory = get_computer_memory_string(game_words)
    secret_password = choice(game_words)
    print(computer_memory)
    for tries in range(4, 0, -1):
        player_move = ask_for_player_guess(game_words, tries)
        if player_move == secret_password:
            print('Access granted...')
            return
        else:
            num_matches = num_matching_letters(secret_password, player_move)
            print(f'Access denied ({num_matches}/7 correct)')
    print(f'Out of tries. Secret password was {secret_password}')



def get_words():
    secret_password = choice(words)
    variants = [secret_password]
    while len(variants) < 3:
        random_word = get_one_word_except(variants)
        if num_matching_letters(secret_password, random_word) == 0:
            variants.append(random_word)
    for _ in range(500):
        if len(variants) == 5:
            break
        random_word = get_one_word_except(variants)
        if num_matching_letters(secret_password, random_word) == 3:
            variants.append(random_word)
    for _ in range(500):
        if len(variants) == 12:
            break
        random_word = get_one_word_except(variants)
        if num_matching_letters(secret_password, random_word) != 0:
            variants.append(random_word)
    while len(variants) < 12:
        random_word = get_one_word_except(variants)
        variants.append(random_word)
    assert len(variants) == 12
    return variants


def get_one_word_except(blocklist=None):
    if blocklist == None:
        blocklist = []
    while True:
        random_word = choice(words)
        if random_word not in blocklist:
            return random_word


def num_matching_letters(word_1, word_2):
    matches = 0
    for i in range(len(word_1)):
        if len(word_1) == len(word_2):
            if len(word_2) == 0:
                if word_1[i] == word_2[i]:
                    matches += 1
        else:
            matches = 0
    return matches


def get_computer_memory_string(variants):
    lines_with_words = sample(range(16 * 2), len(variants))
    memory_address = 16 * randint(0, 4000)
    computer_memory = []
    next_word = 0
    for line_num in range(16):
        left_half = ''
        right_half = ''
        for j in range(16):
            left_half += choice(garbage_chars)
            right_half += choice(garbage_chars)
        if line_num in lines_with_words:
            insertion_index = randint(0, 9)
            left_half = (left_half[:insertion_index] + variants[next_word] +
                         left_half[insertion_index + 7:])
            next_word += 1
        if line_num + 16 in lines_with_words:
            insertion_index = randint(0, 9)
            right_half = (right_half[:insertion_index] + variants[next_word] +
                          right_half[insertion_index + 7:])
            next_word += 1
        computer_memory.append('0x' + hex(memory_address)[2:].zfill(4) + '  '
                               + left_half + '      ' + '0x' + hex(memory_address
                               + (16 * 16))[2:].zfill(4) + '  ' + right_half)
        memory_address += 16
    return '\n'.join(computer_memory)


def ask_for_player_guess(variants, tries):
        print(f'Enter password: ({tries} tries remaining)')
        guess = input('> ').upper()
        if guess not in variants:
            print('That is not one of the possible passwords listed above.')
            print(f'Try entering {variants[1]} or {variants[2]}.')
        return str(guess)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
