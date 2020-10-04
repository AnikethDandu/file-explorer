import tkinter
import tkinter.ttk as ttk
import file_explorer.commands as commands
import os
import pathlib


class Application(ttk.Frame):
    selected_path = 0

    def __init__(self, master=None):
        super().__init__(master)
        self.current_directories = list(path for path in os.listdir(pathlib.Path.home()))

        self.master.rowconfigure(2, weight=1)

        self.main_frame = ttk.Frame(master)
        self.main_frame.grid(column=0, row=0, sticky=tkinter.NSEW)

        self.open_button = ttk.Button(self.main_frame, text='Open')
        self.open_button.grid(column=2, row=2)

        self.cancel_button = ttk.Button(self.main_frame, text='Close')
        self.cancel_button.grid(column=3, row=2, padx=(2.5, 5))

        self.assign_commands()

    def show_path(self):
        indices = {}
        for directory in self.current_directories:
            directory_index = self.current_directories.index(directory)
            indices[directory] = directory_index
            tkinter.Radiobutton(self.main_frame, text=directory, indicatoron=0, value=indices[directory],
                                command=lambda: self.set_selected_path(indices[directory]))\
                .grid(column=1, row=directory_index, columnspan=3, sticky=tkinter.W)

    def assign_commands(self):
        self.cancel_button['command'] = commands.cancel(self=self)

    def set_selected_path(self, value):
        self.selected_path = value
        print(self.selected_path)


root = tkinter.Tk()
root.title('File Explorer')
application = Application(master=root)
application.show_path()
application.mainloop()

