from sys import exit
from random import shuffle

hearts = chr(9829) # ♥
diamonds = chr(9830) # ♦
spades = chr(9824) # ♠
clubs = chr(9827) # ♣

backside = 'backside'

def main():
    print('''
Blackjack, by Al Sweigart al@inventwithpython.com

Rules:
Try to get as close to 21 without going over.
Kings, Queens, and Jacks are worth 10 points.
Aces are worth 1 or 11 points.
Cards 2 through 10 are worth their face value.
(H)it to take another card.
(S)tand to stop taking cards.
On your first play, you can (D)ouble down to increase your bet
but must hit exactly one more time before standing.
In case of a tie, the bet is returned to the player.
The dealer stops hitting at 17.
''')

    money = 5000
    while True:
        if money <= 0:
            print('You are broke!')
            exit()

        print(f'Money: {money}')
        bet = get_bet(money)

        deck = get_deck()
        dealer_hand = [deck.pop(), deck.pop()]
        player_hand = [deck.pop(), deck.pop()]

        print(f'Bet: {bet}')
        while True:
            display_hands(player_hand, dealer_hand, False)
            print()

            move = get_move(player_hand, money-bet)

            if move == 'D':
                additional_bet = get_bet(min(bet, money-bet))
                bet += additional_bet
                print(f'Bet increased to {bet}')
                print(f'Bet: {bet}')


            if move in ('H', 'D'):
                new_card = deck.pop()
                rank, suit = new_card
                print(f'You drew a {rank} of {suit}.')
                player_hand.append(new_card)
                continue

            if move in ('S', 'D'):
                break

        if get_hand_value(player_hand) <= 21:
            while get_hand_value(dealer_hand) < 17:
                print('Dealer hits...')
                dealer_hand.append(deck.pop())
                display_hands(player_hand, dealer_hand, False)

                if get_hand_value(dealer_hand) > 21:
                    break
                input('Press Enter to continue...')
                print('\n\n')

        display_hands(player_hand, dealer_hand, True)

        player_value = get_hand_value(player_hand)
        dealer_value = get_hand_value(dealer_hand)

        if dealer_value > 21:
            print(f'Dealer busts! You win ${bet}')
            money += bet
        elif (player_value > 21) or (player_value < dealer_value):
            print('You lost!')
            money -= bet
        elif player_value > dealer_value:
            print('You win!')
            money += bet
        elif player_value == dealer_value:
            print('It is a tie. Your bet returned to you.')

        input('Press Enter to continue...')
        print('\n\n')

def get_bet(max_bet):
    while True:
        print(f'How much do you bet? 1-{max_bet} or QUIT')
        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            print('Thanks for playing!')
            exit()
        if not bet.isdecimal():
            continue
        bet = int(bet)
        if 1 <= bet <= max_bet:
            return bet

def get_deck():
    deck = []
    for suit in (hearts, diamonds, spades, clubs):
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        for rank in ('J', 'K', 'Q', 'A'):
            deck.append((rank, suit))
    shuffle(deck)
    return deck

def display_hands(player_hand, dealer_hand, show_dealer_hand):
    print()
    if show_dealer_hand:
        print('DEALER:', get_hand_value(dealer_hand))
        display_cards(dealer_hand)
    else:
        print('DEALER: ???')
        display_cards([backside] * len(dealer_hand))
    print('PLAYER:', get_hand_value(player_hand))
    display_cards(player_hand)

def get_hand_value(cards):
    value = 0
    number_of_aces = 0

    for card in cards:
        rank = card[0]
        if rank == 'A':
            number_of_aces += 1
        elif rank in ('K', 'Q', 'J'):
            value += 10
        else:
            value += int(rank)
    value += number_of_aces
    for i in range(number_of_aces):
        if value + 10 <= 21:
            value += 10
    return value

def display_cards(cards):
    rows = ['', '', '', '', '']
    for i, card in enumerate(cards):
        rows[0] += ' ___  '
        if card == backside:
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            rank, suit = card
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))
    for row in rows:
        print(row)

def get_move(player_hand, money):
    while True:
        moves = ['(H)it', '(S)tand']
        if len(player_hand) == 2 and money > 0:
            moves.append('(D)ouble down')

        move_prompt = ', '.join(moves) + '> '
        move = input(move_prompt).upper()
        if move in ('H', 'S'):
            return move
        if move == 'D' and '(D)ouble down' in moves:
            return move

if __name__ == '__main__':
    main()
