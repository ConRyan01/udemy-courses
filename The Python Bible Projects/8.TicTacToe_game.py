
board = [' ' for i in range(9)]

def print_board():
    row1 = f"| {board[0]} | {board[1]} | {board[2]} |"
    row2 = f"| {board[3]} | {board[4]} | {board[5]} |"
    row3 = f"| {board[6]} | {board[7]} | {board[8]} |"

    print(f'\n {row1} \n {row2} \n {row3} \n')

def player_move(icon):
    while True:
        if icon == 'X':
            number = 1
        elif icon == 'O':
            number = 2

        print(f'It is your turn, player {number}')
        choice = int(input('Enter your move (1-9): ').strip())
        if board[choice-1] == ' ':
            board[choice-1] = icon
            break
        else:
            print('That space is taken. Choose a different space.')

def is_victory(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
        (board[3] == icon and board[4] == icon and board[5] == icon) or \
        (board[6] == icon and board[7] == icon and board[8] == icon) or \
        (board[0] == icon and board[3] == icon and board[6] == icon) or \
        (board[1] == icon and board[4] == icon and board[7] == icon) or \
        (board[2] == icon and board[5] == icon and board[8] == icon) or \
        (board[0] == icon and board[4] == icon and board[8] == icon) or \
        (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False

def is_draw():
    if ' ' not in board:
        return True
    else:
        return False

while True:
    print_board()
    player_move('X')
    print_board()
    if is_victory('X'):
        print('--------------- X wins! ---------------')
        break
    elif is_draw():
        print('No one wins!')
        break
    player_move('O')
    print_board()
    if is_victory('O'):
        print('O wins!')
        break
    elif is_draw():
        print('--------------- No one wins! ---------------')
        break