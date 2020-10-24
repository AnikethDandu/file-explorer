"""
This module has methods for widget commands in the Application class located in main.py

METHODS:
    cancel
        Calls inherited destroy method
    return_directories
        Returns all directories at specified path
    open_directory
        Returns lambda that opens text file or re-initializes current path
    set_list
        Re-initializes list of directories at path
"""

import os
import pathlib
from typing import Any


def cancel(application):
    """
    Calls the inherited destroy method from the parent class of parameter class

    :param application: class that calls method
    :type application: Application

    :return: lambda object that contains destroy method
    :rtype: lambda
    """

    return lambda: application.master.destroy()


def return_directories(path: pathlib.Path) -> list:
    """
    Returns a list of directories at a given path

    :param path: path to list directories at
    :type path: pathlib.Path

    :return: list of directories
    :rtype: list of str
    """

    return list(directory for directory in os.listdir(path))


def open_directory(directory: str, application) -> Any:
    """
    Returns lambda object that opens text file or re-initializes current path and returns directories at new path

    :param directory: name of directory that was opened
    :type directory: str
    :param application: class whose widget called open_directory
    :type application: Application

    :return: lambda object to open text file or directory
    :rtype: lambda
    """

    application.starting_path = application.starting_path.joinpath(directory)
    return open(file=application.starting_path, mode='r') \
        if directory[-4:] == '.txt' else set_list(application, return_directories(path=application.starting_path))


def set_list(application, directories: list) -> None:
    """
    Clears Frame of widgets, re-initializes list of directories. and repopulates Frame with new widgets

    :param application: class whose widget called set_list
    :type application: Application
    :param directories: list of directories to re-initialize current_directories to
    :type directories: list of str

    :return: None
    :rtype: None
    """

    application.destroy_directory_widgets()
    application.current_directories = directories
    application.show_path()
