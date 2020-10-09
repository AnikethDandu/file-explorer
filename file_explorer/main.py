import pathlib
import tkinter
import tkinter.ttk as ttk
import file_explorer.commands as commands


class Application(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.selected_path = tkinter.IntVar()
        self.current_directory_widgets = []
        self.starting_path = pathlib.Path.home()
        self.current_directories = commands.return_directories(self.starting_path)

        self.master.rowconfigure(2, weight=1)

        self.main_frame = ttk.Frame(master)
        self.main_frame.grid(column=0, row=0, sticky=tkinter.NSEW)

        self.open_button = ttk.Button(self.main_frame, text='Open')
        self.open_button.grid(column=3, row=3)

        self.cancel_button = ttk.Button(self.main_frame, text='Close')
        self.cancel_button.grid(column=3, row=2, padx=(2.5, 5))

        self.assign_commands()

    def show_path(self) -> None:
        count = 0
        for directory in self.current_directories:
            if directory[0:1] != '.':
                count += 1
                directory_index = self.current_directories.index(directory)
                directory_button = tkinter.Radiobutton(self.main_frame, text=directory, indicatoron=0,
                                                       value=directory_index, variable=self.selected_path)
                directory_button.grid(column=1, row=count, columnspan=3, sticky=tkinter.W)
                self.current_directory_widgets.append(directory_button)

    def assign_commands(self) -> None:
        self.cancel_button['command'] = commands.cancel(self=self)
        self.open_button['command'] = lambda: commands.open_directory(self.current_directories[self.selected_path.get()]
                                                                      , self)

    def destroy_directory_widgets(self) -> None:
        [button.destroy() for button in self.current_directory_widgets]


root = tkinter.Tk()
root.title('File Explorer')
application = Application(master=root)
application.show_path()
application.mainloop()
