try:
    import pyperclip
except ImportError:
    pass

symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('''
Caesar Cipher, by Al Sweigart al@inventwithpython.com
The Caesar cipher encrypts letters by shifting them over by a
key number. For example, a key of 2 means the letter A is
encrypted into C, the letter B encrypted into D, and so on.\n
''')

while True:
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('Please enter the letter E or D.')

while True:
    max_key = len(symbols) - 1
    print(f'Please enter the key from 0 to {max_key} to use.')
    response = input('> ')
    if not response.isdecimal():
        continue
    if 0 <= int(response) <= len(symbols):
        key = int(response)
        break

print(f'Enter the message to {mode}.')
message = input('> ').upper()

translated = ''

for symbol in message:
    if symbol in symbols:
        num = symbols.find(symbol)
        if mode == 'encrypt':
            num += key
        elif mode == 'decrypt':
            num -= key
        if num >= len(symbols):
            num -= len(symbols)
        elif num < 0:
            num += len(symbols)
        translated += symbols[num]
    else:
        translated += symbol

print(translated)

try:
    pyperclip.copy(translated)
    print(f'Full {mode}ed text copied to clipboard.')
except:
    pass
