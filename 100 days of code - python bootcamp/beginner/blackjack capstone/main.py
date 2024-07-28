from art import logo
from replit import clear
import random
print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

should_continue = True if input('Would you like to play a game of blackjack? type "y" or "n": ') == 'y' else False

def deal():
    return random.choice(cards)

def calculate(hand:list):
    total = sum(hand)
    if total == 21:
        return 0
    else:
        return total

def display(p_hand:list, c_hand:list):
    return print(f'\nYour cards: {p_hand}, current score: {calculate(p_hand)}\nComputer\'s first card: {c_hand[0]}')

def player_turn(p_hand:list, d_hand:list):
    while True:
        get_card = input('Type "y" to get another card, type "n" to pass: ')
        if get_card == 'y':
            p_hand.append(deal())
            if calculate(p_hand) > 21:
                if calculate(p_hand) > 21 and 11 in p_hand:
                    p_hand[p_hand.index(11)] = 1
                else:
                    break
        elif get_card == 'n':
            break

        display(p_hand, d_hand)

def dealer_turn(d_hand:list):
    while calculate(d_hand) < 17:
        d_hand.append(deal())
        if calculate(d_hand) > 21 and 11 in d_hand:
            d_hand[d_hand.index(11)] = 1

def compare(p_hand:list, d_hand:list):
    print(f'You\'re final hand: {p_hand}, final score: {calculate(p_hand)}')
    print(f'Computer\'s final hand: {d_hand}, final score: {calculate(d_hand)}')
    
    if sum(d_hand) == 21:
        print('Computer got blackjack. You Lose...')
    elif sum(p_hand) == 21:
        print('Win with a blackjack!')
    elif calculate(d_hand) > 21:
        print('opponent went over. You Win!')
    elif calculate(p_hand) > calculate(d_hand):
        print('You Win!')
    elif calculate(p_hand) < calculate(d_hand):
        print('You Lose.')
    elif calculate(p_hand) == calculate(d_hand):
        print('Draw.')


while should_continue:
    print('\n')
    player_hand = []
    dealer_hand = []  

    for i in range(0,2):
        dealer_hand.append(deal())
        player_hand.append(deal())
    if sum(player_hand) > 21 and 11 in player_hand:
            player_hand[player_hand.index(11)] = 1
    elif sum(dealer_hand) > 21 and 11 in dealer_hand:
            dealer_hand[dealer_hand.index(11)] = 1

    display(player_hand, dealer_hand)

    if sum(dealer_hand) == 21:
        print(f'Computer\'s final hand: {dealer_hand}, final score: {0}')
        print('Dealer got blackjack! You Lose...')
    elif sum(player_hand) == 21:
        print('You got blackjack! You Win!')
    else:
        player_turn(player_hand, dealer_hand)

    if calculate(player_hand) > 21:
        display(player_hand, dealer_hand)
        print('Break! You Lose!')
    elif calculate(player_hand) != 0 and calculate(dealer_hand) != 0:
        dealer_turn(dealer_hand)
        compare(player_hand, dealer_hand)

    if input('Would you like to play a game of blackjack? type "y" or "n": ') == 'n':
        should_continue = False

    clear()
    
print('Game Over! Goodbye.')

