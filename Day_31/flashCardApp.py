#---------------------------------------------------------PACKAGES AND DEPENDENCIES---------------------------------------------------------------#
from tkinter import *
import pandas as pd

#----------------------------------------------------------------CONSTANTS------------------------------------------------------------------------#
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

#-----------------------------------------------------------------READ FILE DATA-------------------------------------------------------------------------#

def flasher():
    df = pd.read_csv("Data/fr_to_en_data/translated_fr_to_en_dict.csv")
    print(f"Error: The source file  does not exist.")
    lang_dict = df.to_dict(orient="records")
    print(lang_dict)


#----------------------------------------------------------------SET UP UI-------------------------------------------------------------------------#

#set up tk window widget
root = Tk()
root.title("Flashly")
root.config(bg=BACKGROUND_COLOR,padx=50,pady=50)

#add graphics using Canvas
canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card_front_img=PhotoImage(file="Images/card_front.png")
card_back_img = PhotoImage(file="Images/card_back.png")
canvas.create_image(410,268,image = card_front_img)
canvas.grid(row=1,column=1,columnspan=2)
#adding text to card
language = canvas.create_text(400, 150, text="Language", fill="black", font=(FONT_NAME, 40, "italic"))
word = canvas.create_text(400, 253, text="Word", fill="black", font=(FONT_NAME, 60, "bold"))

#adding buttons
#wrong btn
wrng_btn_img = PhotoImage(file="Images/wrong.png")
wrng_btn = Button(image=wrng_btn_img,highlightthickness=0,command=flasher)
wrng_btn.grid(row=2,column=1)

#right btn
rt_btn_img = PhotoImage(file="Images/right.png")
rt_btn = Button(image=rt_btn_img,highlightthickness=0,command=flasher)
rt_btn.grid(row=2,column=2)


#-------------------------------------------------------------LOOP UI----------------------------------------------------------------------------#
root.mainloop()