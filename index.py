# creating a simple couculator app useing tkinter

import tkinter as tk

def clickbutton(value):
    current = entry_field.get()
    entry_field.delete(0, tk.END)
    entry_field.insert(tk.END, current + value)


def clear():
    entry_field.delete(0, tk.END)


def calculator():
    try:
        result = eval(entry_field.get())
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, str(result))
    except:
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, "Error")


# we are creating the main window

root = tk.Tk()
root.title("The Problem Solver")

# we are creating the entry feild to accept values

entry_field = tk.Entry(root)
entry_field.grid(row = 0, column = 0, columnspan = 4)

# we are creating the button number
buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','=','+'

]
# creating buttons using loops
row_val = 1
col_val = 0
for button in buttons:
    if button == "=":
        btn = tk.Button(root, text=button, width=10, height=3, font=('Arial', 18), command=calculator)
    elif button == "C":
        btn = tk.Button(root, text=button, width=10, height=3, font=('Arial', 18), command=clear)
    else:
        btn = tk.Button(root, text=button, width=10, height=3, font=('Arial', 18), command=lambda b=button: clickbutton(b))

    btn.grid(row=row_val, column=col_val)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Clear button
clear_button = tk.Button(root, text="C", width=10, height=3, font=('Arial', 18), command=clear)
clear_button.grid(row=5, column=0, columnspan=4)

# Start the main event loop
root.mainloop()
