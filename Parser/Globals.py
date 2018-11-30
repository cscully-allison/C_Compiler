from SymbolTable import SymbolTable
from ConfigManager import ConfigManager

CM = ConfigManager("TargetMachine.config")
ST_G = SymbolTable(None)


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
        return self.Type+str(self.Counter)

Label = TicketCounter("L")
FloatRegister = TicketCounter("FR")
IntRegister = TicketCounter("IR")

def OutPutDataType(Arr):
    TypeString = ''
    for DT in Arr:
        TypeString += DT + ' '

    return TypeString

TSLib = ['void', 'char', 'int', 'float', 'long', 'double', 'short', 'signed', 'unsigned', 'struct', 'union']
TQLib = ['const', 'volatile']
SCSLib = ['auto', 'register', 'static', 'extern', 'typedef']
