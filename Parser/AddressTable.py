class AddressTable():
    def __init__(self):
        self.ReturnPointers = []
        self.RAPrototype = {'LocalSpOffset':0,'Conents':''}

    def PushRA(self, Offset, Contents=None):
        RA = deepcopy({'LocalSpOffset':Offset,'Conents':Contents})
        self.ReturnPointers.append(RA)

    def PopRA(self):
        return self.ReturnPointers.pop()
