print('Multiplication table by Al Sweigart')
print('  |   1   2   3   4   5   6   7   8   9  10  11  12')
print('--+------------------------------------------------')

for num_1 in range(1, 13):
    print(str(num_1).rjust(2), end='|')
    for num_2 in range(1, 13):
        print(str(num_2 * num_1).rjust(4), end='')
    print()
