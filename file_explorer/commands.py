from tkinter import *
from tkinter.ttk import *


def cancel(self):
    return lambda: self.master.destroy()


def set_selected_path(value):
    return lambda: print(value)
