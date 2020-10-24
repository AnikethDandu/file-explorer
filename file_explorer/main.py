"""
This module creates an Application instance and runs the main loop

OBJECTS:
    root
    application
"""

from file_explorer.application import Application
import tkinter

root = tkinter.Tk()
root.title('File Explorer')
application = Application(master=root)
application.mainloop()
