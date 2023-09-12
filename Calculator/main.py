import tkinter as tk
from tkinter import font

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, tk.END)

def calculate():
    current = entry.get()
    try:
        result = eval(current)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# main window
window = tk.Tk()
window.title("Calculator")
window.geometry("400x400")
window.configure(bg='#f2f2f2')


button_font = font.Font(family="Helvetica", size=16, weight="bold")

# Entry field
entry = tk.Entry(window, width=25, borderwidth=5, font=("Helvetica", 20))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

# button colors and styles
button_bg_color = "#4CAF50"
button_fg_color = "white"
button_width = 10
button_height = 2

# Create and position buttons

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row, col = 1, 0
for button_text in buttons:
    if button_text == '=':
        tk.Button(
            window,
            text=button_text,
            padx=button_width,
            pady=button_height,
            command=calculate,
            bg=button_bg_color,
            fg=button_fg_color,
            font=button_font,
        ).grid(row=row, column=col, padx=10, pady=10)
    elif button_text == 'C':
        tk.Button(
            window,
            text=button_text,
            padx=button_width,
            pady=button_height,
            command=clear,
            bg='#ff5722',
            fg=button_fg_color,
            font=button_font,
        ).grid(row=row, column=col, padx=10, pady=10)
    else:
        tk.Button(
            window,
            text=button_text,
            padx=button_width,
            pady=button_height,
            command=lambda text=button_text: button_click(text),
            bg=button_bg_color,
            fg=button_fg_color,
            font=button_font,
        ).grid(row=row, column=col, padx=10, pady=10)
    col += 1
    if col > 3:
        col = 0
        row += 1

window.mainloop()
