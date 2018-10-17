from bintrees import FastRBTree
from copy import deepcopy

class SymbolTable():
    #constructor
    def __init__(self):
        self.Table = [] #declare table as a stack (list) containing an empty tree
        self.TopScope = FastRBTree() # a place where the current top scope is held
        self.ReadMode = True #Read or lookup mode
        self.DebugMode = False

    #Function: InsertSymbol
    #Desc: Insert a symbol into the current top of the symbol table
    # The symbol key string is a lexeme
    #Content_dict: At present this will contain
    #                       {Type: (the token adjacent to the SymbolKey i.e. >int< <SymbolKey>),
    #                       Attribute: some modifier on the symbol 'static' 'const' etc.,
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

        #search the top of our stack
        if self.FindSymbolInCurrentScope(SymbolKey_str):
            T_list.append( self.FindSymbolInCurrentScope(SymbolKey_str) )
        Level_int += 1

        #iterate over all trees
        #add found isntances of symbols to list if present
        for Tree in reversed(self.Table): #reversed so appended items are at the front
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
        if len(self.Table) > 0:
            self.TopScope = self.Table.pop()
        else:
            self.TopScope = None
        return TScope

    #Function: WriteSymbolTableToFile
    #Desc: Write the current contents of the symbol table to file
    def WriteSymbolTableToFile(self, FileName_str):
        T_Stack = []
        i = 0

        try:
            if self.DebugMode == True:

                with open(FileName_str, "w") as File:

                    File.write("\n**** Outputting Contents of Symbol Table **** \n\n")

                    while not self.TableIsEmpty():
                        File.write( "Items in Tree at Level {}: \n".format(i) )
                        self.PrettyPrintScope(self.TopScope, FilePtr=File)
                        T_Stack.append( self.PopScope() )
                        i += 1

                while len(T_Stack) > 0:
                    self.PushScope(T_Stack.pop())
            pass

        except Exception as e:
            raise

    def PrettyPrintScope(self, Scope, FilePtr=None):
        for Key in Scope.keys():
            if FilePtr is not None:
                FilePtr.write( "\tKey: \"{}\" | Content: {}\n".format(Key, Scope.get(Key)) )
            else:
                print( "\tKey: \"{}\" | Content: {}\n".format(Key, Scope.get(Key)) )
        return

    def ToggleReadMode(self):
        self.ReadMode = not self.ReadMode
        return

    def TableIsEmpty(self):
        if self.TopScope is None:
            return True
        return False
