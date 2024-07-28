from replit import clear
from art import logo

print(logo)
bidders = {}
more_bids = True
highest = 0

def make_bid():
    name = input('What is your name? ')
    bid = input('What is your bid amount? $')
    bidders[name] = bid

while more_bids:
    make_bid()
    ask_more = input('Are there more bids? yes or no: ').lower()
    if ask_more == 'no':
        more_bids = False
        clear()
    elif ask_more == 'yes':
        clear()

for key in bidders:
    bid_amount = int(bidders[key])
    if bid_amount > highest:
        highest = bid_amount
        winner = key

print(f'The Winner is {winner} with a bid of ${highest}')