from sys import exit

x_max = 7
try:
    while True:
        print(r'           /        \ ' * x_max)
        print( '          /          \\'* x_max)
        print(r'\________/            ' * x_max)
        print(r"/        \            " * x_max)
        print(r'          \          /' * x_max)
        print(r'           \________/ ' * x_max)
except KeyboardInterrupt:
    exit()
