from tkinter import *
from tkinter.ttk import *


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.cancel_button = Button(text='Cancel').pack()


root = Tk()
application = Application(master=root)
application.mainloop()
