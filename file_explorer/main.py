from tkinter import *
from tkinter.ttk import *
import file_explorer.commands as commands


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        self.widgets = []

        self.cancel_button = Button(self, text='Cancel')
        self.widgets.append(self.cancel_button)

        self.pack_widgets()
        self.assign_commands()

    def assign_commands(self):
        self.cancel_button['command'] = commands.cancel(self=self)

    def pack_widgets(self):
        for widget in self.widgets:
            widget.pack()


root = Tk()
application = Application(master=root)
application.mainloop()
