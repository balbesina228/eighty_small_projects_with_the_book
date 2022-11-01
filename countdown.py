from sys import exit
from time import sleep
from sev_seg import get_sev_seg_str

seconds_left = 30  # Try to change amount of time!

try:
    while True:
        print('\n' * 60)
        hours = str(seconds_left // 3600)
        minutes = str(seconds_left % 3600 // 60)
        seconds = str(seconds_left % 60)
        h_digits = get_sev_seg_str(hours, 2)
        m_digits = get_sev_seg_str(minutes, 2)
        s_digits = get_sev_seg_str(seconds, 2)

        h_top_row, h_middle_row, h_bottom_row = h_digits.splitlines()
        m_top_row, m_middle_row, m_bottom_row = m_digits.splitlines()
        s_top_row, s_middle_row, s_bottom_row = s_digits.splitlines()

        print(h_top_row + '   ' + m_top_row + '   ' + s_top_row)
        print(h_middle_row + ' * ' + m_middle_row + ' * ' + s_middle_row)
        print(h_bottom_row + ' * ' + m_bottom_row + ' * ' + s_bottom_row)

        if seconds_left == 0:
            print()
            print('  * * * * BOOM * * * *')
            break
        sleep(1)
        seconds_left -= 1

except KeyboardInterrupt:
    print('Countdown by Al Sweigart.')
    exit()
