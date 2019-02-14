
import tkinter as tk
from ui_funcs import _from_rgb

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

# window customization
window.configure(background=_from_rgb((65, 244, 166)))

# title
window.title("Welcome to Scholarly")
lbl = tk.Label(window, text="Welcome to Scholarly", font=("Times New Roman", 50), bg=_from_rgb((65, 244, 166)))
lbl.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
tk.Label(window, text="Login to continue", font=("Times New Roman", 24), bg=_from_rgb((65, 244, 166))).place(relx=0.5, rely=0.3, anchor=tk.CENTER)
wlcmUsrLbl = tk.Label(window, text="An interesting name goes below", font=("Times New Roman", 16), bg=_from_rgb((65, 244, 166)))
wlcmUsrLbl.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

# getting user input
userName = tk.Entry(window, width = 30)
userName.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

# submit button
submitButton = tk.Button(window, text="Introduce me to cool people")
submitButton.place(relx=0.5, rely=0.55, anchor=tk.CENTER)

# defining exit function
def close_window():
    window.destroy()
    exit()
# exit button
tk.Button(window, text="Exit", command=close_window).place(relx=0.9, rely=0.9, anchor=tk.CENTER)



window.mainloop()
