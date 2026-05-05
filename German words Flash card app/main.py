import pandas as pd
from tkinter import *
import random
import time

from streamlit import button

BACKGROUND_COLOR = "#B1DDC6"
german_word = ""
english_word = ""
german_dict_length = 100

try:
    df = pd.read_csv("./Words_to_learn.csv")
    word_dict = df.to_dict()
    # german_dict_length = df.shape[0]
    german_dict_length = len(word_dict["German"])
except FileNotFoundError:
    df = pd.read_csv("german_to_english.csv")
    word_dict = df.to_dict()
    # german_dict_length = df.shape[0]
    german_dict_length = len(word_dict["German"])
# word_dict = df.to_dict(orient = "record") -> That organizes the dic to a better format

# ----------------------------- FUNCTIONS --------------------------------- #

def new_word_generator(extra_func = False): #Parameter decides if the button calls an extra function or not
    global german_word, english_word, word_text, count, flip_timer, num_word

    # Select randomly a word in german and its translation
    num_word = random.randint(0, german_dict_length)
    german_word = word_dict["German"][num_word]
    english_word = word_dict["English"][num_word]
    canvas.itemconfig(word_text, text=german_word)

    if count >= 1:
        window.after_cancel(flip_timer)
        canvas.itemconfig(card, image=card_img_front)
        canvas.itemconfig(title_text, text="German", fill="black")
        canvas.itemconfig(word_text, text=german_word, fill="black")
        flip_timer = window.after(3000, flip_card)
        # print(count)

    if extra_func == True:
        words_to_learn()


def flip_card():
    # print("Flip Card")
    canvas.itemconfig(card, image=card_img_back)
    canvas.itemconfig(title_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=english_word, fill="white")



def words_to_learn():
    global english_word, german_word, num_word, german_dict_length

    del word_dict["German"][num_word]
    del word_dict["English"][num_word]

    new_df = pd.DataFrame(word_dict)
    new_df.to_csv("Words_to_learn.csv", index=False)
    german_dict_length = len(word_dict["German"]) #reset then length of search for the random words
    print(german_dict_length)


# ----------------------------- GUI --------------------------------------- #
window = Tk()
window.title("German flash cards app")
window.configure(background=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
card_img_front = PhotoImage(file="./images/card_front.png")
card_img_back = PhotoImage(file="./images/card_back.png")
card = canvas.create_image(0, 0, image=card_img_front, anchor="nw")
title_text = canvas.create_text(400, 150, text="German", font=("ariel",40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

button_x_image = PhotoImage(file="./images/wrong.png")
button_x = Button(image=button_x_image, bd=0, highlightthickness=0, command=new_word_generator)
button_x.grid(row=1, column=0)

button_c_image = PhotoImage(file="./images/right.png")
button_c = Button(image=button_c_image, bd=0, highlightthickness=0, command=lambda:new_word_generator(extra_func=True))
button_c.grid(row=1, column=1)

flip_timer = window.after(3000, flip_card)

count = 0
new_word_generator()
count +=1

words_to_learn()


window.mainloop()



#TODO Correct the error when a word is deleted from the list, but its number keeps being called
#TODO Format the translations in order to stick to only maximum 3 words

# ----------------------------- WORDS ------------------------------------- #

# df = pd.read_csv("german_to_english.csv")
#
# # Select randomly a word in german and its translation
# num_word = random.randint(0,99)
# word_dict=df.to_dict()
# german_word = word_dict["German"][num_word]
# english_word = word_dict["English"][num_word]

# Bring the column:
# col_german = df["German"]       # Series
# col_english = df["English"]     # Series
#
# print(col_german)
# print(col_english

# Bring the line:
# linha = df[df["German"] == "ich"]
# print(linha)

# Bring only the translation:
# trad_en = df.loc[df["German"] == "sie", "English"].iloc[0]
# print(trad_en)
