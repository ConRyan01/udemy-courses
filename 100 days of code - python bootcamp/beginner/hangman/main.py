import random
import hangman_art
import hangman_words

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
lives = 6
guessed_letters = []

print(hangman_art.logo)
display = ['_'] * len(chosen_word)
print(' '.join(display))

while ''.join(display) != chosen_word and lives > 0:
    guess = input('\n\n\nGuess a letter: ').lower()

    for i in range(word_length):
        letter = chosen_word[i]
        if letter == guess:
            display[i] = letter
    
    if len(guess) > 1 or not guess.isalpha():
        print('\n!!!INVALID GUESS. TYPE A SINGLE LETTER!!!')

    elif guess in guessed_letters:
        print('You already guessed that letter.')

    elif guess not in display:
        lives -= 1

        if guess not in guessed_letters:
            guessed_letters.append(guess)

        print(f'Incorrect Guess. You have {lives} guesses left.')

    else:
        print('Correct!')
        if guess not in guessed_letters:
            guessed_letters.append(guess)

    print(hangman_art.stages[lives])
    print(' '.join(display))
    print(f'\nguessed letters: {",".join(guessed_letters)}')

if ''.join(display) == chosen_word:
    print('You Win!')
else:
    print(f'\nYou Lose... the word was {chosen_word}')
