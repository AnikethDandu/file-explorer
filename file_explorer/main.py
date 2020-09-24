from tkinter import *
from tkinter.ttk import *


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()


root = Tk()
application = Application(master=root)
application.mainloop()
