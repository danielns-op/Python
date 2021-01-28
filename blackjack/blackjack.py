import logo
from random import choice
from time import sleep

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def presentation():
    will_play = True
    while will_play:
        print('-=' * 32)
        print(logo.logo)
        print('-=' * 32)
        print('{:^64}'.format("*** Let's Play one BlackJack! ***\n"))
        print(f'{"[ 1 ] - START":^64}')
        print(f'{"[ 2 ] - Exit":^63}')

        try:
            start = int(input('Option: '))
            if start < 1 or start > 2:
                print('[ERROR] - Option 1 or 2 only.')
                sleep(1.5)
                continue
            elif start == 2:
                will_play = False
                return will_play
            else:
                return will_play
        except ValueError:
            print('[ERROR] - Choose only:\n1 - to play\nor\n2 - to leave.')
            sleep(2)


def choose_card():
    card = choice(cards)
    return card


def sum_cards(var):
    sum_is = sum(var)
    return sum_is


def calculate_balance(num1, num2):
    c_balance = num1[0] - num2
    return c_balance


def get_another_card(var):
    card = choose_card()
    var.append(card)


def play():
    playing = presentation()
    balance = [1000]
    if playing:
        print('-=' * 32)
        while True:
            try:
                bet_player = int(input('->How much you want to bet: $'))
                if bet_player < 1 or bet_player > balance[0]:
                    print(f'Attention, enter value between 1 and {balance[0]}.')
                    sleep(2)
                else:
                    break
            except ValueError:
                print('[ERROR] - Integer values only.')
                sleep(2)
        print('-=' * 32)
        player_cards = [choose_card(), choose_card()]
        balance_player = calculate_balance(balance, bet_player)
        player_score = sum_cards(player_cards)
        print(f'>Your cards: {player_cards}')
        print(f'>Current score: {player_score}')
        print(f'>Bet: ${bet_player}  --  Balance: ${balance_player}')

        print('-=' * 16)

        bot_cards = [choose_card(), choose_card()]
        bot_score = sum_cards(bot_cards)
        print(f'{f">Bot first card: {bot_cards[0]}":>50}')
        print('')

        while True:
            get_card = str(input('Take another card? [Y / n]: ')).strip().lower()
            if get_card == 'y':
                get_another_card(player_cards)
                player_score = sum_cards(player_cards)
                if player_score > 20:
                    break
                else:
                    player_score = sum_cards(player_cards)
                    print('-=' * 32)
                    print(f'>Your cards: {player_cards}')
                    print(f'>Current score: {player_score}')
                    print(f'>Bet: ${bet_player}  --  Balance: ${balance_player}')
            else:
                player_score = sum_cards(player_cards)
                print('-=' * 32)
                print(f'>Your final cards: {player_cards}')
                print(f'>Your final score: {player_score}')
                print(f'>Bet: ${bet_player}  --  Balance: ${balance_player}')

                while bot_score < 21:
                    get_another_card(bot_cards)
                    bot_score = sum_cards(bot_cards)
                print('-=' * 16)
                print(f'{f">Bot final hand: {bot_cards}":>58}')
                print(f'{f">Bot final score: {bot_score}":>50}')
                print('')
    else:
        print(f'{"Leaving the game.":^64}')
        sleep(1.5)


play()
