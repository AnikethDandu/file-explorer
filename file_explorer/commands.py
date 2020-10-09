import os


def cancel(self):
    return lambda: self.master.destroy()


def return_directories(path):
    return list(directory for directory in os.listdir(path))


def open_directory(directory, master):
    master.starting_path = master.starting_path.joinpath(directory)
    return open(file=directory, mode='r') \
        if directory[-3:] == '.txt' else set_list(master, return_directories(path=master.starting_path))


def set_list(master, value,):
    master.destroy_directory_widgets()
    master.current_directories = value
    master.show_path()
