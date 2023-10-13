import tkinter as tk

def on_button_click(value):
    if value == '=':
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(0, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    elif value == 'C':
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, value)

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")

# Entry field for input and result
entry = tk.Entry(window, width=20)
entry.grid(row=0, column=0, columnspan=4)
entry.configure(bg='yellow')

# Buttons
button_texts = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row, col = 1, 0
for text in button_texts:
    button_color = 'pink' if text in ['+', '-', '*', '/'] else 'orange'
    tk.Button(window, text=text, command=lambda t=text: on_button_click(t), bg=button_color).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Start the GUI application
window.mainloop()
# thankyou codsoft for this oppurtunity
