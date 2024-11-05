from tkinter import *
import random as rand
from tkinter import messagebox
import string
import pyperclip

# ---------------------------- CONSTANTS ------------------------------- #
FONT_NAME = "Courier"

# ---------------------------- VALIDATE PASSWORD ------------------------------- #
def validation(password):
    symbols = "!@#$%^&*()"
    numbers = string.digits
    symbol_no, no_no = 0, 0

    if len(password) < 8:
        messagebox.showerror(title="Weak Password", message="Password is too short. It must be at least 8 characters.")
        return False
    for i in password:
        if i in symbols:
            symbol_no += 1
        if i in numbers:
            no_no += 1
    if no_no < 2 or symbol_no < 2:
        messagebox.showerror(title="Weak Password", message="Password must include at least 2 symbols and 2 numbers.")
        return False

    return True

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    nr_letters = rand.randint(8, 12)
    nr_symbols = rand.randint(2, 4)
    nr_numbers = rand.randint(2, 4)

    letters = string.ascii_letters
    symbols = "!@#$%^&*()"
    numbers = string.digits

    password_list = (
        [rand.choice(letters) for _ in range(nr_letters)] +
        [rand.choice(symbols) for _ in range(nr_symbols)] +
        [rand.choice(numbers) for _ in range(nr_numbers)]
    )

    rand.shuffle(password_list)
    password = ''.join(password_list)

    password_entry.delete(0, 'end')
    password_entry.insert(END, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_name = website_entry.get()
    username = user_name_entry.get()
    password = password_entry.get()

    if len(website_name) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(title="Warning", message="Please make sure you haven't left any fields empty.")
        return

    if not validation(password):
        return

    # Check for existing entries
    try:
        with open("saved_passwords.txt", mode="r") as password_file:
            existing_entries = password_file.readlines()
            if f"{website_name} | {username} | {password}\n" in existing_entries:
                messagebox.showerror(title="Warning", message="This entry already exists.")
                return
    except FileNotFoundError:
        # If the file doesn't exist, it's safe to proceed with saving
        pass

    user_action = messagebox.askokcancel(title=website_name, message=f"Website: {website_name}\nEmail/Username: {username}\nPassword: {password}\nDo you want to save or cancel?")
    if user_action:
        try:
            with open("saved_passwords.txt", mode="a") as password_file:
                password_file.write(f"{website_name} | {username} | {password}\n")
                messagebox.showinfo(title="Success", message="Password saved successfully!")
        except Exception as e:
            messagebox.showerror(title="Error", message=f"Failed to save password: {e}")


# ---------------------------- HIDE PASSWORD ------------------------------- #
def toggle_password_visibility():
    if password_entry.cget('show') == '':
        password_entry.config(show='*')
        toggle_btn.config(text='Show Password')
    else:
        password_entry.config(show='')
        toggle_btn.config(text='Hide Password')

# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title("Password Manager")
root.config(padx=20, pady=20)

canvas = Canvas(width=200, height=220, highlightthickness=0)
password_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 110, image=password_logo)
canvas.grid(column=2, row=0)

Label(text="Website:", font=(FONT_NAME, 12)).grid(column=1, row=1)
website_entry = Entry(width=46)
website_entry.grid(column=2, row=1, columnspan=2)

Label(text="Email/Username:", font=(FONT_NAME, 12)).grid(column=1, row=2)
user_name_entry = Entry(width=46)
user_name_entry.grid(column=2, row=2, columnspan=2)
user_name_entry.insert(END, "@gmail.com")

Label(text="Password:", font=(FONT_NAME, 12)).grid(column=1, row=3,rowspan=2)
password_entry = Entry(width=28)
password_entry.grid(column=2, row=3 ,rowspan=2, columnspan=1)

# Generate Password Button
generatePassword_btn = Button(text="Generate Password", command=password_generator)
generatePassword_btn.config(width=14)
generatePassword_btn.grid(column=3, row=3)

# Show Password Button
toggle_btn = Button(text="Show Password", command=toggle_password_visibility)
toggle_btn.grid(column=3, row=4)

# Add Button
add_btn = Button(text="Add", bg="lightblue", width=46, command=save_password)
add_btn.grid(column=2, row=5, columnspan=2)

root.mainloop()
