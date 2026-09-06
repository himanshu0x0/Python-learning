import tkinter as tk

# Function to evaluate the expression
def calculate():
    try:
        result = eval(entry.get())  # Evaluate expression
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget (for input)
entry = tk.Entry(root, font=("Arial", 16), justify="right", width=15)
entry.grid(row=0, column=0, columnspan=4)

# Buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row, col = 1, 0
for button in buttons:
    action = lambda x=button: entry.insert(tk.END, x) if x != "=" else calculate()
    if button == "C":
        action = lambda: entry.delete(0, tk.END)

    tk.Button(root, text=button, command=action, font=("Arial", 14), width=5).grid(row=row, column=col)
    
    col += 1
    if col > 3:
        col = 0
        row += 1

# Run the application
root.mainloop()