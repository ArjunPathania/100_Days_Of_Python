def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1,2,3,5,6,7,8,8))

def calculate(**kwargs):
    for (key,value) in kwargs.items():
        print(f"{key}:{value}")


calculate(name="arjun",age=22,sex="m")

from tkinter import *
from tkinter.ttk import Entry

window = Tk()
window.minsize(width=500,height=400)
window.title("My First GUI Program")
window.config(padx=200,pady=150)

#label
my_label = Label(text="I am a Label",font=("Arial",12,"italic"))
my_label.grid(column=1,row=1)

#buttons
def button_clicked():
    print("button was clicked")
    my_label.config(text=input_.get())
button1=Button(text="Click Me",command=button_clicked)
button1.grid(column=2,row=2)

def button_clicked():
    print("button was clicked")
    my_label.config(text=input_.get())
button2=Button(text="Click Me",command=button_clicked)
button2.grid(column=3,row=1)

#input
input_ = Entry(width=10)
input_.grid(column=4,row=3)
print(input_.get())

window.mainloop()