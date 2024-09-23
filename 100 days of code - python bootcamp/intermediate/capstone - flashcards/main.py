from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ('Ariel', 40, 'italic')
WORD_FONT = ('Ariel', 60, 'bold')
random_word = None

def chose_correctly():
    try:
        words.remove(random_word)
    except:
        canvas.itemconfig(word_text, text='You Are Done!')
        correct_btn.destroy()
        wrong_btn.destroy()

    choose_word()

def choose_word():
    global random_word, flip_timer

    window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_image, image=card_front_img)
    random_word = random.choice(words)
    canvas.itemconfig(language_text, fill='black', text=list(random_word.keys())[0])
    canvas.itemconfig(word_text, fill='black', text=random_word['French'])
    flip_timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(language_text, fill='white', text=list(random_word.keys())[1])
    canvas.itemconfig(word_text, fill='white', text=random_word['English'])

try:
    df = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    df = pandas.read_csv('data/french_words.csv')

words = df.to_dict(orient='records')

window = Tk()
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)

card_front_img = PhotoImage(file='images/card_front.png')
card_back_img = PhotoImage(file='images/card_back.png')
right_img = PhotoImage(file='images/right.png')
wrong_img = PhotoImage(file='images/wrong.png')

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=0, padx=50, pady=50, columnspan=2)

correct_btn = Button(image=right_img, highlightthickness=0, command=chose_correctly)
correct_btn.grid(row=1, column=1)
wrong_btn = Button(image=wrong_img, highlightthickness=0, command=choose_word)
wrong_btn.grid(row=1, column=0)

language_text = canvas.create_text(400, 150, font=LANGUAGE_FONT)
word_text = canvas.create_text(400, 300, font=WORD_FONT)

flip_timer = window.after(3000, flip_card)
choose_word()

window.mainloop()

df = pandas.DataFrame(words)
df.to_csv('data/words_to_learn.csv', index=False)
