import tkinter as tk

root = tk.Tk()
root.title("My First GUI")
root.geometry("300x200")

label = tk.Label(root, font="Arial", text="HEllo, Python")
label.pack(pady=200)

root.mainloop()