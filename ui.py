
import tkinter as tk

window = tk.Tk()

ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()

# Assigning window dimensions
w = 1024
h = 720
# calculate x and y coordinates for the Window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# setting the dimensions of the screen and where it is placed
window.geometry('%dx%d+%d+%d' % (w, h, x, y))

# title
window.title("Welcome to Scholarly")
lbl = tk.Label(window, text="Welcome to Scholarly", font=("Times New Roman", 50))
lbl.grid(column=0, row=0)


window.mainloop()
