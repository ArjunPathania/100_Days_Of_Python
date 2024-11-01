from tkinter import Tk, Label, Entry, Button

# Create the main window
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Conversion function
def convert_miles_to_km():
    try:
        miles = float(miles_entry.get())
        kms = round(miles * 1.60934, 2)
        km_result_label.config(text=str(kms))
    except ValueError:
        km_result_label.config(text="Invalid input")

# Miles input
miles_entry = Entry(width=10)
miles_entry.grid(column=1, row=0)

# Miles label
Label(text="Miles").grid(column=2, row=0)

# "is equal to" label
Label(text="is equal to").grid(column=0, row=1)

# Km result label
km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

# Km label
Label(text="Km").grid(column=2, row=1)

# Calculate button
Button(text="Calculate", command=convert_miles_to_km).grid(column=1, row=2)

# Run the main loop
window.mainloop()
