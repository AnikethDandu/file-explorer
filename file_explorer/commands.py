from tkinter import *
from tkinter.ttk import *


def cancel(self):
    return lambda: self.master.destroy()
