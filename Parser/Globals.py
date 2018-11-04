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


class TicketCounter(object):
    def __init__(self, Type):
        self.Type = Type
        self.Counter = 0

    def DispenseTicket(self):
        self.Counter += 1
        print("DispensedTicket:", self.Type+str(self.Counter))
        return self.Type+str(self.Counter)

Label = TicketCounter("L")
FloatRegister = TicketCounter("FR")
IntRegister = TicketCounter("IR")
