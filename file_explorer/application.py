"""
This module stores the class that inherits from the TkInter Frame and adds GUI widgets

CLASSES:
    Application
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
        :ivar button_frame: Frame for navigation buttons
        :type button_frame: tkinter.Frame
        :ivar open_button: button to open directory or file
        :type open_button: ttk.Button
        :ivar close_button: button to close application
        :type close_button: ttk.Button
        :ivar scroll_bar: Scroll bar for directories in Canvas widget
        :type scroll_bar: tkinter.Scrollbar
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

        self.master = tkinter.Frame(master)
        self.master.grid()
        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=1)

        self.scroll_bar = tkinter.Scrollbar(master, orient=tkinter.VERTICAL)
        self.scroll_bar.grid(row=0, column=1, sticky=tkinter.NSEW)

        self.master.bind("<Configure>",
                         lambda x: self.main_canvas.configure(scrollregion=self.main_canvas.bbox(tkinter.ALL)))

        self.main_canvas = tkinter.Canvas(self.master, yscrollcommand=self.scroll_bar.set)
        self.main_canvas.grid(column=0, row=0, sticky=tkinter.NSEW)
        self.main_canvas.rowconfigure(0, weight=1)

        self.scroll_bar.configure(command=self.main_canvas.yview)

        self.button_frame = tkinter.Frame(self.master)
        self.button_frame.grid(column=0, row=1, sticky=tkinter.NSEW)

        self.open_button = ttk.Button(self.button_frame, text='Open')
        self.open_button.grid(column=0, row=1, sticky=tkinter.EW)

        self.close_button = ttk.Button(self.button_frame, text='Close')
        self.close_button.grid(column=0, row=0, sticky=tkinter.EW)

        self.assign_commands()

        self.show_path()

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
                self.main_canvas.create_window(50, count*25, window=directory_button)
                self.current_directory_widgets.append(directory_button)

    def assign_commands(self) -> None:
        """
        Sets commands for navigation buttons

        :return:None
        :rtype: None
        """
        self.close_button['command'] = commands.cancel(application=self.master)
        self.open_button['command'] = lambda: commands.open_directory(self.current_directories[self.selected_path.get()]
                                                                      , self)

    def destroy_directory_widgets(self) -> None:
        """
        Destroys all directory RadioButton widgets

        :return: None
        :rtype: None
        """
        [button.destroy() for button in self.current_directory_widgets]
