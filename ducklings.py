from sys import exit, stdout
from random import random, choice
from shutil import get_terminal_size
from time import sleep

pause = 0.2
density = 0.1
left = 'left'
right = 'right'
up = 'up'
down = 'down'
out = 'out'
happy = 'happy'
aloof = 'aloof'
beady = 'beady'
wide = 'wide'
chubby = 'chubby'
very_chubby = 'very chubby'
opened = 'opened'
closed = 'closed'
head = 'head'
body = 'body'
feet = 'feet'
duckling_width = 5
width = get_terminal_size()[0] - 1


class Duckling:
    def __init__(self):
        self.direction = choice([left, right])
        self.body = choice([chubby, very_chubby])
        self.mouth = choice([opened, closed])
        self.wing = choice([out, up, down])

        if self.body == chubby:
            self.eyes = beady
        else:
            self.eyes = choice([beady, happy, aloof, wide])
        self.part_to_display_next = head

    def get_eyes(self):
        if self.eyes == beady and self.body == chubby:
            return '"'
        elif self.eyes == beady and self.body == very_chubby:
            if self.direction == left:
                return '" '
            else:
                return ' "'
        elif self.eyes == happy:
            return '^^'
        elif self.eyes == wide:
            return "''"
        elif self.eyes == aloof:
            return '``'

    def get_mouth(self):
        if self.mouth == opened:
            if self.direction == left:
                return '>'
            else:
                return '<'
        elif self.mouth == closed:
            return '='

    def get_wing(self):
        if self.wing == out:
            if self.direction == left:
                return '>'
            else:
                return '<'
        elif self.wing == up:
            return '^'
        elif self.wing == down:
            return 'v'

    def get_head(self):
        head_str = ''
        if self.direction == left:
            head_str += self.get_mouth()
            head_str += self.get_eyes() + ') '

        elif self.direction == right:
            head_str += ' (' + self.get_eyes()
            head_str += self.get_mouth()

        if self.body == chubby:
            head_str += ' '
        return head_str

    def get_body(self):
        body_str = '('
        if self.direction == left:
            if self.body == chubby:
                body_str += ' '
            elif self.body == very_chubby:
                body_str += '  '
            body_str += self.get_wing()

        elif self.direction == right:
            body_str += self.get_wing()

            if self.body == chubby:
                body_str += ' '
            elif self.body == very_chubby:
                body_str += '  '
        body_str += ')'
        if self.body == chubby:
            body_str += ' '
        return body_str

    def get_feet(self):
        if self.body == chubby:
            return ' ^^  '
        elif self.body == very_chubby:
            return ' ^ ^ '

    def get_next_body_part(self):
        if self.part_to_display_next == head:
            self.part_to_display_next = body
            return self.get_head()
        elif self.part_to_display_next == body:
            self.part_to_display_next = feet
            return self.get_body()
        elif self.part_to_display_next == feet:
            self.part_to_display_next = None
            return self.get_feet()


def main():
    print('Duckling screensaver by Al Sweigart\nPress Ctrl-C to quit')
    sleep(2)
    duckling_lanes = [None] * (width // duckling_width)

    while True:
        for lane_num, duckling_obj in enumerate(duckling_lanes):
            if duckling_obj == None and random() <= density:
                duckling_obj = Duckling()
                duckling_lanes[lane_num] = duckling_obj
            if duckling_obj != None:
                print(duckling_obj.get_next_body_part(), end='')
                if duckling_obj.part_to_display_next == None:
                    duckling_lanes[lane_num] = None
            else:
                print(' ' * duckling_width, end='')
        print()
        stdout.flush()
        sleep(pause)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
