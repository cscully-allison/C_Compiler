class ErrorManager(object):
    def __init__(self):
        self.Errors = []

    def HasErrors(self):
        if len(self.Errors) > 0:
            return True
        return False

    def AddError(self, Error):
        self.Errors.append(Error)

    def PrintErrors(self):
        for Error in self.Errors:
            print(Error)

    def WriteErrors(self, Error):
        pass

ErrManager = ErrorManager()
