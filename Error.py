class Error(Exception):
    pass

class FileNameError(Error):
    def __init__(self, pathFile):
        self.pathFile = pathFile
