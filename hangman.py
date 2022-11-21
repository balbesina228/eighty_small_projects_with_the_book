from sys import exit
from random import choice

hangman_pics = [
r'''
 +--+
 |  |
    |
    |
    |
    |
=====
''',
r'''
 +--+
 |  | 
 O  |
    |
    |
    |
=====
''',
r'''
 +--+
 |  |
 O  |
 |  |
    |
    |
=====
''',
r'''
 +--+
 |  |
 O  |
/|  |
    |
    |
=====
''',
r'''
 +--+
 |  |
 O  |
/|\ |
    |
    |
=====
''',
r'''
 +--+
 |  |
 O  |
/|\ |
/   |
    |
=====
''',
r'''
 +--+
 |  |
 O  |
/|\ |
/ \ |
    |
=====
'''
]

category = 'animals'
words = 'ANT BABOON BADGER BAT BEAR BEAVER CAMEL CAT CLAM COBRA COUGAR' \
        'COYOTE CROW DEER DOG DONKEY DUCK EAGLE FERRET FOX FROG GOAT GOOSE HAWK' \
        'LION LIZARD LLAMA MOLE MONKEY MOOSE MOUSE MULE NEWT OTTER OWL PANDA PARROT' \
        'PIGEON PYTHON RABBIT RAM RAT RAVEN RHINO SALMON SEAL SHARK SHEEP SKUNK' \
        'SLOTH SNAKE SPIDER STORK SWAN TIGER TOAD TROUT TURKEY TURTLE WEASEL WHALE' \
        'WOLF WOMBAT ZEBRA'.split()


def main():
    print('Hangman by Al Sweigart.')
    missed_letters = []
    correct_letters = []
    secret_word = choice(words)
    while True:
        draw_hangman(missed_letters, correct_letters, secret_word)
        guess = get_player_guess(missed_letters + correct_letters)
        if guess in secret_word:
            correct_letters.append(guess)
            found_all_letters = True
            for secret_word_letter in secret_word:
                if secret_word_letter not in correct_letters:
                    found_all_letters = False
                    break
            if found_all_letters:
                print('Yes! The secret word is:', secret_word)
                print('You have won!')
                break
        else:
            missed_letters.append(guess)
            if len(missed_letters) == len(hangman_pics) - 1:
                draw_hangman(missed_letters, correct_letters, secret_word)
                print('You have run out of guesses!')
                print(f'The word was {secret_word}.')
                break


def draw_hangman(missed_letters, correct_letters, secret_word):
    print(hangman_pics[len(missed_letters)])
    print('The category is:', category, '\n')
    print('Missed letters: ', end='')
    if len(missed_letters) == 0:
        print('No missed letters yet.\n')
    blanks = ['_'] * len(secret_word)
    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks[i] = secret_word[i]
    print(' '.join(blanks))


def get_player_guess(already_guessed):
    print('Guess a letter:')
    guess = input('> ').upper()
    if len(guess) > 1:
        print('You\'ve entered more than one letter!')
    elif guess in already_guessed:
        print('You have already guessed that letter!')
    elif not guess.isalpha():
        print('You\'ve entered not a letter!')
    return guess


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
