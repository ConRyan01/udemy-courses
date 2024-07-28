from random import choice

questions = ['why is the sky blue?: ','why is the grass green?: ','Where are all the dinosaurs?: ']

acceptable_answers = ['just because', 'just cause', 'because i said so']

answer = input(choice(questions)).lower().strip()
while answer not in acceptable_answers:
    answer = input('but why?: ')

print('Oh, okay!')