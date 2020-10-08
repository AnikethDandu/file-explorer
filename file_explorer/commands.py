def cancel(self):
    return lambda: self.master.destroy()


def open_directory(path):
    return open(file=path, mode='r') if path[-3:] == '.txt' else print(f'Open directory: {path}')
