print('Enter the encrypted Ceasar cipher message to hack:')
message = input('> ')

symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(symbols)):
    translated = ''
    for symbol in message:
        if symbol in symbols:
            num = symbols.find(symbol)
            num -= key
            if num < 0:
                num += len(symbols)
            translated += symbols[num]
        else:
            translated += symbol

    print(f'Key #{key}: {translated}')
