
from tkinter import *


class GUI:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry('500x500')

        # Labels
        first_Label = Label(self.root, text='First Label')
        second_Label = Label(self.root, text='Second Label')

        # Entries
        first_entry = Entry(self.root)
        second_entry = Entry(self.root)



        # Packing
        first_Label.grid(column=1, row=1)
        second_Label.grid(column=1, row=2)
        first_entry.grid(column=2, row=1)
        second_entry.grid(column=2, row=2)


    def start(self):
        self.root.mainloop()

appstart = GUI()
appstart.start()