import tkinter as tk
from ui_funcs import _from_rgb
from clientSocketConnection import *
from threading import Thread

# Global variables
USERIP = ''
USERPORT = 8981
USERNAME = ''

# UI instance
class window(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)
        
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Chat):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)
    
    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self,parent)

        #Enter your name
        label1 = tk.Label(self, text="Enter Your Name Below")
        #label1.pack()
        label1.place(relx=0.5, rely=0.40, anchor=tk.CENTER)
       
        
        #Text box for username entry
        self.userInput = tk.Entry(self, text="UserName")
        self.userInput.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        

        #Enter button
        button1 = tk.Button(self, text="Enter", command=lambda: self.onButtonPress(controller))
        button1.place(relx=0.5, rely=0.60, anchor=tk.CENTER)

    def onButtonPress(self, controller):
        global USERNAME
        USERNAME = self.userInput.get()
        getUsername(USERNAME)
        return controller.show_frame(Chat)

class Chat(tk.Frame):

    def __init__(self, parent, controller):
        #Online label
        tk.Frame.__init__(self,parent)
        # TODO: DO the USERNAME implementation  
        global USERNAME
        print(USERNAME)
        label1 = tk.Label(self, text=  " - Online")
        label1.place(relx=0.05, rely=0.05, anchor=tk.CENTER)
        #label1.place(x=1, y=1)

        #listbox of online members
        listbox = tk.Listbox(self)
        listbox.place(relx=0.19, rely= 0.25, anchor=tk.CENTER)
        #listbox.place(x=2,y=5)

        #listbox of chat messages
        listbox2 = tk.Listbox(self)
        listbox2.place(relx=0.67, rely=0.3777, anchor=tk.CENTER, width=275, height=300)

        #Return to login screen (log out)
        button1 = tk.Button(self, text="Log Out", command=lambda: controller.show_frame(StartPage))
        button1.place(relx=0.9, rely=0.05, anchor=tk.CENTER)

        #Send button
        button2 = tk.Button(self, text="Send", command=sendMessage)
        button2.place(relx=0.9, rely=0.72, anchor=tk.CENTER)

        # Message field
        e = tk.Entry(self)
        e.place(relx=0.6, rely= 0.72, anchor=tk.CENTER, width=260)
        
        
        makeSocketConnection(USERIP, USERPORT)
    
    def getUsername(self):
        global USERNAME
        
        print(USERNAME) # USER NAME IS NOT GETTING HERE< IT IS BLANK


# UI ends here


app = window()
app.title("Welcome to Scholarly App")
app.geometry("600x600")





app.mainloop()
