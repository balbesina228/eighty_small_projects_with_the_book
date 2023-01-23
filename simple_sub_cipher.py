from random import shuffle

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    print('''
Simple Substitution Cipher, by Al Sweigart
A simple substitution cipher has a one-to-one translation for each
symbol in the plaintext and each symbol in the ciphertext.
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
        print('Please specify key to use.')
        if mode == 'encrypt':
            print('Or enter RANDOM to have one generated for you.')
        response = input('> ').upper()
        if response == 'RANDOM':
            key = generate_random_key()
            print(f'The key is {key}. KEEP THIS IN SECRET!')
            break
        else:
            if check_key(response):
                key = response
                break
    print(f'Enter the message to {mode}.')
    message = input('> ')
    if mode == 'encrypt':
        translated = encrypt_message(message, key)
    elif mode == 'decrypt':
        translated = decrypt_message(message, key)
    print('The %sed message is:' % mode)
    print(translated)


def generate_random_key():
    key = list(LETTERS)
    shuffle(key)
    return ''.join(key)


def check_key(key):
    key_list = list(key)
    letters_list = list(LETTERS)
    key_list.sort()
    letters_list.sort()
    if key_list != letters_list:
        print('There is an error in the key or symbol set.')
        return False
    return True


def encrypt_message(message, key):
    return translate_message(message, key, 'encrypt')


def decrypt_message(message, key):
    return translate_message(message, key, 'decrypt')


def translate_message(message, key, mode):
    translated = ''
    chars_a = LETTERS
    chars_b = key
    if mode == 'decrypt':
        chars_a, chars_b = chars_b, chars_a
    for symbol in message:
        if symbol.upper() in chars_a:
            sym_index = chars_a.find(symbol.upper())
            if symbol.isupper():
                translated += chars_b[sym_index].upper()
            else:
                translated += chars_b[sym_index].lower()
        else:
            translated += symbol
    return translated


if __name__ == '__main__':
    main()
