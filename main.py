import random
from tkinter import *
import pandas as pd

inform = {}
try:
    data = pd.read_csv('words_to_learn.csv')
except FileNotFoundError:
    orig_data = pd.read_csv('french_words.csv')
    inform = orig_data.to_dict(orient='records')
else:
    inform = data.to_dict(orient='records')

current_card = {}


def ticked():
    inform.remove(current_card)
    #print(len(inform))
    data = pd.DataFrame(inform)
    data.to_csv('words_to_learn.csv',index=False)
    next_card()


def next_card():
    global current_card, flipt
    window.after_cancel(flipt)
    current_card = random.choice(inform)
    canvas.itemconfig(lang_name, text="French", fill='#D989B5')
    canvas.itemconfig(word_name, text=current_card['French'], fill="#975C8D")
    canvas.itemconfig(card_bg, image=card_front_img)
    flipt = window.after(3000, func=flipped)


def flipped():
    canvas.itemconfig(lang_name, text="English", fill="#C060A1")
    canvas.itemconfig(word_name, text=current_card['English'], fill="#975C8D")
    canvas.itemconfig(card_bg, image=card_back_img)


window = Tk()
window.title("Flash Card App")
window.config(pady=50, padx=50, bg='#DEBACE')
flipt = window.after(3000, func=flipped)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file='card_b.png')
card_back_img = PhotoImage(file='new_bg.png')
card_bg = canvas.create_image(400, 263, image=card_front_img)
canvas.grid(row=0, column=1, padx=5, pady=5, columnspan=2)

lang_name = canvas.create_text(400, 150, text='Title', fill="#D989B5", font=('Ariel', 35, 'italic'))

word_name = canvas.create_text(400, 263, text='Word', fill="#975C8D", font=('Ariel', 60, 'bold'))

tick_mark = PhotoImage(file="tick_l.png")
tick_button = Button(image=tick_mark, highlightthickness=0, command=ticked)
tick_button.grid(row=1, column=1, padx=7, pady=7)

cross_mark = PhotoImage(file="cross_l.png")
cross_button = Button(image=cross_mark, highlightthickness=0, command=next_card)
cross_button.grid(row=1, column=2, padx=7, pady=7)

next_card()
window.mainloop()
