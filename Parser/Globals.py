class ErrorManager(object):
    def __init__(self):
        self.Errors = []

    def AddError(self, Error):
        self.Errors.append(Error)

    def PrintErrors(self):
        for Error in self.Errors:
            print(Error)

    def WriteErrors(self, Error):
        pass

ErrManager = ErrorManager()
