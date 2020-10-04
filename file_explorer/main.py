import tkinter
import tkinter.ttk as ttk
import file_explorer.commands as commands
import os
import pathlib


class Application(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.main_frame = ttk.Frame(master, padding="2.5 0 10 10")
        self.main_frame.grid(column=0, row=0)

        self.cancel_button = ttk.Button(self.main_frame, text='Close')
        self.cancel_button.grid(column=2, row=2)

        self.assign_commands()

    def assign_commands(self):
        self.cancel_button['command'] = commands.cancel(self=self)


root = tkinter.Tk()
root.title('File Explorer')
application = Application(master=root)
application.mainloop()
