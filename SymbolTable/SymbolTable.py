from bintrees import FastRBTree
from copy import deepcopy

class SymbolTable():
    #constructor
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
        #perform deepcopy on passed in dictionary
        self.TopScope.insert(SymbolKey_str, deepcopy(Content_dict) )
        return

    #Function: FindSymbolInTable
    #Desc: Search all scopes of the symbol table to find a specific symbol
    #Return: [{Level_int: Content_dict}, False] (list of keys for possibility of many shadowed vars)
    def FindSymbolInTable(self, SymbolKey_str):
        T_list = []
        Level_int = 0

        T_list.append(FindSymbolInCurrentScope(SymbolKey_str))
        Level_int += 1

        for Tree in Table:
            if Tree.__contains__(SymbolKey_str):
                T_list.append( {Level_int: Tree.get(SymbolKey_str)} )
            Level_int += 1

        if len(T_list) > 0:
            return T_list

        #nothing found case
        return False

    #Function: FindSymbolInCurrentScope
    #Desc: Search only the top level of the symbol table for key
    def FindSymbolInCurrentScope(self, SymbolKey_str):
        return self.TopScope.get(SymbolKey_str, False)

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
