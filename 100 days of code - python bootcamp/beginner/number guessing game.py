import random

should_continue = True

while should_continue:
    print('\nWelcome to the number guessing game!\nI\'m thinking of a number between 1 and 100.')
    number = random.randint(1,100)
    difficulty = input('Choose a difficulty. type "easy" or "hard": ')

    if difficulty == 'hard':
        lives = 5
    elif difficulty == 'easy':
        lives = 10

    while lives > 0:
        print(f'You have {lives} attempts remaining to guess the number')
        guess = int(input('Make a guess: '))

        if guess == number:
            print('You got it!')
            break
        elif guess < number:
            print('Too low.')
            lives -= 1
        else:
            print('Too high.')
            lives -= 1
        
        if lives == 0:
            print(f'You Lose. The number was {number}')
            break
    
    should_continue = False if input('Would you like to play again? "y" or "n": ') == 'n' else True

print('Game Over. Goodbye.')
