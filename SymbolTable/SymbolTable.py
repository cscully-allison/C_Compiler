from bintrees import FastRBTree

class SymbolTable():
    def __init__(self):
        self.Table = [] #declare table as a stack (list) containing an empty tree
        self.TopScope = FastRBTree() # a place where the current top scope is held
        self.ReadMode = True #Read or lookup mode

    #Function: InsertSymbol
    #Desc: Insert a symbol into the current top of the symbol table
    #Content_dict: At present this will contain
    #                       {DataType: (the token adjacent to the SymbolKey i.e. >int< <SymbolKey>),
    #                       ContainedValue: (char/float/int) literal,
    #                       TokenLocation: tuple(line, char) }
    def InsertSymbol(self, SymbolKey_str, Content_dict):
        self.TopScope.insert(SymbolKey_str, Content_dict)
        return

    #Function: FindSymbolInTable
    #Desc: Search all scopes of the symbol table to find a specific symbol
    def FindSymbolInTable(self, SymbolKey_str):
        return False

    #Function: FindSymbolInCurrentScope
    #Desc: Search only the top level of the symbol table for key
    def FindSymbolInCurrentScope(self, SymbolKey_str):
        return False

    #Function:PushNewScope
    #Desc: Create a new scope and push it onto the table
    def PushNewScope(self):
        self.PushScope(FastRBTree())
        return

    #Function: PushScope
    #Desc: Insert symbol tree (RBTree) onto our table
    def PushScope(self, SymbolTree):
        self.Table.append(self.TopScope)
        self.TopScope = SymbolTree
        return

    #Function: PopScope
    #Desc: Remove and return scope (RBtree) from the symbol table
    def PopScope(self):
        TScope = self.TopScope
        self.TopScope = self.Table.pop()
        return TScope

    #Function: WriteSymbolTableToFile
    #Desc: Write the current contents of the symbol table to file
    def WriteSymbolTableToFile(self, FileName_str):
        return

    def ToggleReadMode(self):
        self.ReadMode = not self.ReadMode
        return