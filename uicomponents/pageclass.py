
import tkinter as tk


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class loginPage(tk.Frame, window):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
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

