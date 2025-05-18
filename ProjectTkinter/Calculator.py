import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget for display
entry = tk.Entry(root, width=40, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button click event
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

# Clear entry
def button_clear():
    entry.delete(0, tk.END)

# Calculate result
def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Button layout
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
]

# Add buttons to window
for (text, row, col) in buttons:
    if text == '=':
        tk.Button(root, text=text, padx=30, pady=20, command=button_equal).grid(row=row, column=col)
    else:
        tk.Button(root, text=text, padx=30, pady=20, command=lambda t=text: button_click(t)).grid(row=row, column=col)

# Clear button
tk.Button(root, text="Clear", padx=115, pady=20, command=button_clear).grid(row=5, column=0, columnspan=4)

# Run the app
root.mainloop()
