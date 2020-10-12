"""
This module creates and populates a TkInter frame with the necessary GUI widgets

CLASSES:
    Application

OBJECTS:
    root
    application
"""

import pathlib
import tkinter
import tkinter.ttk as ttk
import file_explorer.commands as commands


class Application(ttk.Frame):
    """
    Creates a Canvas widget and populates it with navigation buttons and a list of directories based on current path

    METHODS:
        show_path
        assign_commands
        destroy_directory_widgets

    INSTANCE ATTRIBUTES:
        :ivar selected_path: index of selected directory RadioButton
        :type selected_path: tkinter.IntVar()
        :ivar current_directory_widgets: list of all RadioButton widgets corresponding to each directory at current path
        :type current_directory_widgets: list of tkinter.RadioButton
        :ivar starting_path: root path
        :type starting_path: pathlib.Path
        :ivar current_directories: list of all current directories available at current path
        :type current_directories: list of str
        :ivar main_canvas: Canvas that is master widget for all other widgets
        :type main_canvas: tkinter.Canvas
        :ivar open_button: button to open directory or file
        :type open_button: ttk.Button
        :ivar close_button: button to close application
        :type close_button: ttk.Button
    """

    def __init__(self, master=None):
        """
        Creates an application class inheriting from the tkinter.Tk class, master frame widget, and navigation buttons

        :param master: root class to inherit from
        :type master: tkinter.Tk
        """

        super().__init__(master)
        self.selected_path = tkinter.IntVar()
        self.current_directory_widgets = []
        self.starting_path = pathlib.Path.home()
        self.current_directories = commands.return_directories(self.starting_path)

        self.master.rowconfigure(2, weight=1)

        self.main_canvas = tkinter.Canvas(master, width=500, height=500)
        self.main_canvas.grid(column=0, row=0, sticky=tkinter.NSEW)

        self.open_button = ttk.Button(self.main_canvas, text='Open')
        self.open_button.grid(column=3, row=3)

        self.close_button = ttk.Button(self.main_canvas, text='Close')
        self.close_button.grid(column=3, row=2, padx=(2.5, 5))

        self.assign_commands()

    def show_path(self) -> None:
        """
        Displays every directory at current path as RadioButton

        :return: None
        :rtype: None
        """
        count = 0
        for directory in self.current_directories:
            if directory[0:1] != '.':
                count += 1
                directory_index = self.current_directories.index(directory)
                directory_button = tkinter.Radiobutton(self.main_canvas, text=directory, indicatoron=0,
                                                       value=directory_index, variable=self.selected_path)
                directory_button.grid(column=1, row=count, columnspan=3, sticky=tkinter.W)
                self.current_directory_widgets.append(directory_button)

    def assign_commands(self) -> None:
        """
        Sets commands for navigation buttons

        :return:None
        :rtype: None
        """
        self.close_button['command'] = commands.cancel(application=self)
        self.open_button['command'] = lambda: commands.open_directory(self.current_directories[self.selected_path.get()]
                                                                      , self)

    def destroy_directory_widgets(self) -> None:
        """
        Destroys all directory RadioButton widgets

        :return: None
        :rtype: None
        """
        [button.destroy() for button in self.current_directory_widgets]


root = tkinter.Tk()
root.title('File Explorer')
application = Application(master=root)
application.show_path()
application.mainloop()
