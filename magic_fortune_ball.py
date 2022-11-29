from time import sleep
from random import choice, randint


def slow_space_print(text, interval=0.1):
    for char in text:
        if char.upper == 'I':
            print('i ', end='', flush=True)
        else:
            print(char.upper(), ' ', end='', flush=True)
        sleep(interval)
    print('\n')


slow_space_print('magic fortune ball by al sweigart')
sleep(0.5)
slow_space_print('ask me your yes/no question')
input('> ')
replies = [
    'let me think on this...',
    'an interesting question...',
    'hmmm... are you sure want to know..?',
    'do you think some things are best left unknown..?',
    'i might tell you but you may not like the answer...',
    'yes... no... maybe... i will think on it...',
    'and what you will do when you know the answer..? we shall see...',
    'i shall consult my visions...',
    'you may want to sit down for this...'
]
slow_space_print(choice(replies))
slow_space_print('.' * randint(4, 12), 0.7)
slow_space_print('i have an answer...', 0.2)
sleep(1)
answers = [
    'yes, for sure',
    'my answer is no',
    'ask me later',
    'i am programmed to say yes',
    'the stars say yes, but i say no',
    'i dunno maybe',
    'focus and ask once more',
    'doubtful, very doubtful',
    'affirmative',
    'yes, though you may not like it',
    'no but you may wish it was so'
]
slow_space_print(choice(answers), 0.5)
