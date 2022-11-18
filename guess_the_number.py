from random import randint

def ask_for_guess():
    while True:
        guess = input('> ')
        if guess.isdecimal():
            return int(guess)
        print('Enter a number between 1 and 100.')


print('Guess the Number, by Al Sweigart.\n')
secret_number = randint(1, 100)
print('I am thinking of a number between 1 and 100.')
for i in range(10):
    print(f'You have {10 - i} guesses left. Take a guess.')
    guess = ask_for_guess()
    if guess == secret_number:
        break
    if guess < secret_number:
        print('Your guess is too low.')
    if guess > secret_number:
        print('Your guess is too high.')
if guess == secret_number:
    print('Yay! You have guessed my number!')
else:
    print('Game over. The number I was thinking of was', secret_number)
