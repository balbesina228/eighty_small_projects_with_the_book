from sev_seg import get_sev_seg_str
from sys import exit
from time import localtime, sleep

try:
    while True:
        print('\n' * 60)
        current_time = localtime()
        hours = str(current_time.tm_hour % 24)
        minutes = str(current_time.tm_min)
        seconds = str(current_time.tm_sec)

        h_digits = get_sev_seg_str(hours, 2)
        h_top_row, h_middle_row, h_bottom_row = h_digits.splitlines()

        m_digits = get_sev_seg_str(minutes, 2)
        m_top_row, m_middle_row, m_bottom_row = m_digits.splitlines()

        s_digits = get_sev_seg_str(seconds, 2)
        s_top_row, s_middle_row, s_bottom_row = s_digits.splitlines()

        print(h_top_row    + '   ' + m_top_row +    '   ' + s_top_row)
        print(h_middle_row + ' * ' + m_middle_row + ' * ' + s_middle_row)
        print(h_bottom_row + ' * ' + m_bottom_row + ' * ' + s_bottom_row)
        print('\nPress Ctrl-C to quit.')

        while True:
            sleep(0.01)
            if localtime().tm_sec != current_time.tm_sec:
                break

except KeyboardInterrupt:
    print('Digital clock, by Al Sweigart.')
    exit()
    input()
