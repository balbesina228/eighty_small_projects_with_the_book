print('Gullible, by Al Sweigart.')

while True:
    print('Do you want to know how to keep a gullible person '
          'busy for hours? Y/N')
    response = input('> ').upper()
    if response.startswith('Y'):
        continue
    elif response.startswith('N'):
        break
    else:
        print(f'{response} is not a valid yes/no response.')
print('Thank you! Have a nice day!')
