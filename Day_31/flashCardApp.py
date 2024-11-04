#---------------------------------------------------------PACKAGES AND DEPENDENCIES---------------------------------------------------------------#
from tkinter import *
import pandas as pd
import random

#----------------------------------------------------------------CONSTANTS------------------------------------------------------------------------#
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"


df = pd.read_csv("Data/fr_to_en_data/translated_fr_to_en_dict.csv")
to_learn = df.to_dict(orient="records")
current_car = {}
#-----------------------------------------------------------------FLASHING MECHANISM-------------------------------------------------------------------------#

def next_card():
    wrng_btn.config(state="disabled")
    rt_btn.config(state="disabled")
    canvas.itemconfig(card_side, image=card_front_img)
    if len(to_learn)!=0:
        current_card = random.choice(to_learn)
        global current_car
        current_car = current_card
        current_word = current_card["French"]
        canvas.itemconfig(language,text="French")
        canvas.itemconfig(word,text = current_word)
    else:
        canvas.itemconfig(language, text="You have learned all the words.")
        canvas.itemconfig(word, text="Congratulations")
    root.after(3000,flash_card)


def flash_card():
    wrng_btn.config(state="normal")
    rt_btn.config(state="normal")
    global current_car
    current_card = current_car
    canvas.itemconfig(card_side, image=card_back_img)
    current_word = current_card["English"]
    canvas.itemconfig(language, text="English")
    canvas.itemconfig(word, text=current_word)

def is_known():
    to_learn.remove(current_car)
    print(len(to_learn))
    words_to_learn = pd.DataFrame(to_learn)
    words_to_learn.to_csv("Data/fr_to_en_data/words_to_learn.csv")
    next_card()



#----------------------------------------------------------------SET UP UI-------------------------------------------------------------------------#

#set up tk window widget
root = Tk()
root.title("Flashly")
root.config(bg=BACKGROUND_COLOR,padx=50,pady=50)

root.after(3000,flash_card)

#add graphics using Canvas
canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card_front_img=PhotoImage(file="Images/card_front.png")
card_back_img = PhotoImage(file="Images/card_back.png")
card_side = canvas.create_image(410,268,image = card_front_img)
canvas.grid(row=1,column=1,columnspan=2)
#adding text to card
language = canvas.create_text(400, 150, text="Language", fill="black", font=(FONT_NAME, 40, "italic"))
word = canvas.create_text(400, 253, text="Word", fill="black", font=(FONT_NAME, 60, "bold"))

#adding buttons
#wrong btn
wrng_btn_img = PhotoImage(file="Images/wrong.png")
wrng_btn = Button(image=wrng_btn_img,highlightthickness=0,command=next_card)
wrng_btn.grid(row=2,column=1)

#right btn
rt_btn_img = PhotoImage(file="Images/right.png")
rt_btn = Button(image=rt_btn_img,highlightthickness=0,command=is_known)
rt_btn.grid(row=2,column=2)

next_card()

#-------------------------------------------------------------LOOP UI----------------------------------------------------------------------------#
root.mainloop()