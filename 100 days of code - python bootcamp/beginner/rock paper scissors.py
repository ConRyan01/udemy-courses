import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images=[rock, paper, scissors]
player_choice = int(input('Type 0 for Rock, 1 for Paper, or 2 for Scissors: '))
print(game_images[int(player_choice)])
computer_choice_int = random.randint(0,2)

computer_choice = 'rock' if computer_choice_int == 0 else ('paper' if computer_choice_int == 1 else 'scissors')

if player_choice == computer_choice_int:
    print(f'The computer chose {computer_choice}, It\'s a tie!')
elif player_choice == 0 and computer_choice_int == 2:
    print(f'the computer chose {computer_choice}, You Win!')
elif player_choice == 1 and computer_choice_int == 0:
    print(f'the computer chose {computer_choice}, You Win!')
elif player_choice == 2 and computer_choice_int == 1:
    print(f'the computer chose {computer_choice}, You Win!')
else:
    print(f'the computer chose {computer_choice}, You Lose!')

print(game_images[computer_choice_int])
