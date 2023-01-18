upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_letters = 'abcdefghijklmnopqrstuvwxyz'
print('ROT13 Cipher by Al Sweigart\n')

while True:
    print('Enter a message to encrypt/decrypt (or QUIT):')
    message = input('> ')
    if message.upper() == 'QUIT':
        break
    translated = ''
    for character in message:
        if character.isupper():
            trans_char_index = (upper_letters.find(character) + 13) % 26
            translated += upper_letters[trans_char_index]
        elif character.islower():
            trans_char_index = (lower_letters.find(character) + 13) % 26
            translated += lower_letters[trans_char_index]
        else:
            translated += character
    print('The translated message is:')
    print(translated + '\n')
