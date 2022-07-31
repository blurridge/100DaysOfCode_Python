# Main

from tkinter import *

window = Tk()
window.title("Mile to Km Converter by blurridge")
window.minsize(width=300, height=100)

# Function
def miles_to_km():
    km = float(user_input.get()) * 1.609
    converted_label.config(text=km)

# Entry
user_input = Entry()
user_input.insert(END, "0")
user_input.focus()
user_input.grid(column=1, row=0)

# Entry Label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# Is Equal To Label
is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

# Converted Label
converted_label = Label(text="0")
converted_label.grid(column=1, row=1)

# Km Label
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Calculate Button
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()