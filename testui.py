
import tkinter as tk
from ui_funcs import _from_rgb, button_push

class window(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)
        
        # window.grid_rowconfigure(0, weight=1)
        # window.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = StartPage(container, self)

        self.frames[StartPage] = frame

        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)
    
    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self,parent)
        label1 = tk.Label(text="Enter Your Name Below")
        label1.place(relx=0.5, rely=0.40, anchor=tk.CENTER)
        
        e = tk.Entry()
        e.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        s = e.get()

        button1 = tk.Button(text="Enter", command=button_push)
        button1.place(relx=0.5, rely=0.60, anchor=tk.CENTER)

class Chat(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self,parent)
        label1 = tk.Label("Online")
        label1.place(relx=0.3)


app = window()

# test starts
ws = app.winfo_screenwidth()
hs = app.winfo_screenheight()

# Assigning window dimensions
w = 1024
h = 720
# calculate x and y coordinates for the Window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# setting the dimensions of the screen and where it is placed
app.geometry('%dx%d+%d+%d' % (w, h, x, y))



app.mainloop()

#window = tk.Tk()

# ws = window.winfo_screenwidth()
# hs = window.winfo_screenheight()

# Assigning window dimensions
# w = 1024
# h = 720
# calculate x and y coordinates for the Window
# x = (ws/2) - (w/2)
# y = (hs/2) - (h/2)

# setting the dimensions of the screen and where it is placed
# window.geometry('%dx%d+%d+%d' % (w, h, x, y))

# window customization
# window.configure(background=_from_rgb((65, 244, 166)))

# bgColor = _from_rgb((65, 244, 166))

# title
# window.title("Welcome to Scholarly")
# lbl = tk.Label(window, text="Welcome to Scholarly", font=("Times New Roman", 50), bg=bgColor)
# lbl.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
# tk.Label(window, text="Login to continue", font=("Times New Roman", 24), bg=bgColor).place(relx=0.5, rely=0.3, anchor=tk.CENTER)
# wlcmUsrLbl = tk.Label(window, text="An interesting name goes below", font=("Times New Roman", 16), bg=bgColor)
# wlcmUsrLbl.place(relx=0.5, rely=0.4, anchor=tk.CENTER)
'''
# getting user input
userName = tk.Entry(window, width = 30)
userName.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

# submit button
submitButton = tk.Button(window, text="Introduce me to cool people")
submitButton.place(relx=0.5, rely=0.55, anchor=tk.CENTER)

# exit button
tk.Button(window, text="Exit").place(relx=0.9, rely=0.9, anchor=tk.CENTER)

window.mainloop()
'''