from tkinter import *
import random as rand
from tkinter import messagebox
import string
import pyperclip
# ---------------------------- CONSTANTS ------------------------------- #

FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    nr_letters = rand.randint(8, 12)
    nr_symbols = rand.randint(2, 4)
    nr_numbers = rand.randint(2, 4)

    # Define characters
    letters = string.ascii_letters
    symbols = "!@#$%^&*()"
    numbers = string.digits

    # Use list comprehensions to build the password list
    password_list = (
        [rand.choice(letters) for _ in range(nr_letters)] +
        [rand.choice(symbols) for _ in range(nr_symbols)] +
        [rand.choice(numbers) for _ in range(nr_numbers)]
    )

    # Shuffle the list to randomize the order
    rand.shuffle(password_list)

    # Join the list into a string to form the final password
    password = ''.join(password_list)

    # Insert the password into the entry field
    password_entry.delete(0, 'end')  # Clear the existing content
    password_entry.insert(END, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    validation_check = True
    website_name = website_entry.get()
    username = user_name_entry.get()
    password = password_entry.get()
    if len(website_name) ==0 or len(username)==0 or len(password)==0:
        validation_check =False
    if not validation_check:
        messagebox.showerror(title="Warning",message="Please make sure you haven't left any fields empty.")
    else:
        user_action = messagebox.askokcancel(title=website_name,message=f"Website: {website_name}\nEmail/Username:{username}\nPassword:{password}\nDo you want to save or cancel?")
        if user_action and validation_check:
            with open("saved_passwords.txt", mode="a") as password_file:
                password_file.write(f"{website_name} | {username} | {password}\n")

# ---------------------------- UI SETUP ------------------------------- #

#Main Window
root = Tk()
root.title("Password Manager")
root.config(padx=20,pady=20)


#add logo
canvas = Canvas(width=200,height=220,highlightthickness=0)
password_logo = PhotoImage(file="logo.png")
canvas.create_image(100,110,image=password_logo)
canvas.grid(column=2,row=0)

#Website label
Label(text="Website:",font=(FONT_NAME,12)).grid(column=1,row=1)

# Website Entry
website_entry = Entry(width=46)
website_entry.grid(column=2,row=1,columnspan=2)

#Email/Username label
Label(text="Email/Username:",font=(FONT_NAME,12)).grid(column=1,row=2)

#Email/Username entry
user_name_entry = Entry(width=46)
user_name_entry.grid(column=2,row=2,columnspan=2)
user_name_entry.insert(END, string="@gmail.com")

#Password Label
Label(text="Password:",font=(FONT_NAME,12)).grid(column=1,row=3)

#Password Entry
password_entry = Entry(width=28)
password_entry.grid(column=2,row=3,columnspan=1)

#Generate Password Button
generatePassword_btn = Button(text="Generate Password",command=password_generator)
generatePassword_btn.config(width=14)
generatePassword_btn.grid(column=3,row=3,)

#Add Button
add_btn = Button(text="Add",bg="lightblue",width=46,command=save_password)
add_btn.grid(column=2,row=4,columnspan=2)

root.mainloop()