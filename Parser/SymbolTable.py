from bintrees import FastRBTree
from copy import deepcopy

class SymbolTable():
    #constructor
    def __init__(self, SourceFile):
        self.Table = [] #declare table as a stack (list) containing an empty tree
        self.TopScope = FastRBTree()    # a place where the current top scope is held
        self.ReadMode = False           #Read or lookup mode
        self.DebugMode = False
        self.SourceFile = SourceFile
        self.LastPushedInScope = None

    #Function: InsertSymbol
    #Desc: Insert a symbol into the current top of the symbol table
    # The symbol key string is a lexeme
    #Content_dict: At present this will contain
    #                       {Type: (the token adjacent to the SymbolKey i.e. >int< <SymbolKey>),
    #                       Type Qualifier: qualifies the type specificer 'const', 'volatile' can be a list
    #                       Storage Class Specifier: defines how the symbol is stored
    #                       TokenLocation: tuple(line, char_in_file, char_in_line) }
    def InsertSymbol(self, SymbolKey_str, Content_dict):
        try:

            if self.DebugMode == True:
                print("Insert symbol is called: ", "In Read Mode?", self.ReadMode, SymbolKey_str ,Content_dict)

            if self.ReadMode == False:
                found = self.FindSymbolInCurrentScope(SymbolKey_str)
                if not found:
                    found = self.FindSymbolInTable(SymbolKey_str)
                    if found:
                        for item in found:
                            for key in list(item.keys()):
                                self.PrettyErrorPrint("Warning: {0} on line {3} is a shadowded variable. Previous declaration in scope level {1} at line {2}.".format(SymbolKey_str, abs(key-len(self.Table)), item[key]["TokenLocation"][0], Content_dict['TokenLocation'][0]), item[key]["TokenLocation"][0], item[key]["TokenLocation"][2] )
                    #perform deepcopy on passed in dictionary
                    self.TopScope.insert(SymbolKey_str, deepcopy(Content_dict) )
                    self.LastPushedInScope = Content_dict
                elif 'Subtype' in found and found['Subtype'] == 'Function Prototype':
                    pass
                else:
                    self.PrettyErrorPrint('''Error: Redeclaration of existing variable.\nPrior declaration is here at line {0}: \n'''.format(found["TokenLocation"][0]), found["TokenLocation"][0], found["TokenLocation"][2] )
                    raise Exception('Redeclaration of exisitng variable in current scope.')
            else:
                # do nothing
                pass
        except Exception as e:
            raise e

        # can return false causing problems with Children
        # need to handle this in the context of functions
        return self.RecoverMostRecentID(SymbolKey_str)



    #Function: FindSymbolInTable
    #Desc: Search all scopes of the symbol table to find a specific symbol
    #Return: [{Level_int: Content_dict}, False] (list of keys for possibility of many shadowed vars)
    def FindSymbolInTable(self, SymbolKey_str):
        T_list = []
        Level_int = 0

        #search the top of our stack
        if self.FindSymbolInCurrentScope(SymbolKey_str):
            T_list.append( {abs(Level_int-len(self.Table)): self.FindSymbolInCurrentScope(SymbolKey_str)} )
        Level_int += 1

        #iterate over all trees
        #add found isntances of symbols to list if present
        for Tree in reversed(self.Table): #reversed so appended items are at the front
            if Tree is not None and Tree.__contains__(SymbolKey_str):
                T_list.append( {abs(Level_int-len(self.Table)): Tree.get(SymbolKey_str)} )
            Level_int += 1

        if len(T_list) > 0:
            return T_list

        #nothing found case
        return False

    #Function: FindSymbolInCurrentScope
    #Desc: Search only the top level of the symbol table for key
    def FindSymbolInCurrentScope(self, SymbolKey_str):
        return self.TopScope.get(SymbolKey_str, False)


    def RecoverMostRecentID(self, SymbolKey_str):
        SymbolList = self.FindSymbolInTable(SymbolKey_str)
        if SymbolList is not False:
            for Key in SymbolList[0]:
                return SymbolList[0][Key]
        else:
            return False

    def CalcLocalOffset(self):
        if self.LastPushedInScope is None:
            return 0;
        else:
            return self.LastPushedInScope['Local Offset'] + self.LastPushedInScope['Size In Bytes']


    #Function:PushNewScope
    #Desc: Create a new scope and push it onto the table
    def PushNewScope(self):
        self.PushScope(FastRBTree())
        self.LastPushedInScope = None
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

        # try:
        with open(FileName_str, "w") as File:
            File.write("\n**** Outputting Contents of Symbol Table **** \n\n")

            while not self.TableIsEmpty():
                File.write( "Items in Tree at Level {}: \n".format(i) )
                self.PrettyPrintScope(self.TopScope, FilePtr=File)
                T_Stack.append( self.PopScope() )
                i += 1

        while len(T_Stack) > 0:
            self.PushScope(T_Stack.pop())

        # except Exception as e:
        #     raise

    def PrettyPrintScope(self, Scope, FilePtr=None):
        for Key in Scope.keys():
            if FilePtr is not None:
                FilePtr.write( "\tKey: \"{}\" | Content: {}\n".format(Key, Scope.get(Key)) )
            else:
                print( "\tKey: \"{}\" | Content: {}\n".format(Key, Scope.get(Key)) )
        return

    def ToggleDebugMode(self):
        self.DebugMode = not self.DebugMode
        return

    def ReadModeOn(self):
        self.ReadMode = True
        # print("Insert Mode Toggled Off")
        return

    def InsertMode(self):
        self.ReadMode = False
        # print("Insert Mode Toggled On")
        return

    def ToggleReadMode(self):
        self.ReadMode = not self.ReadMode

        if self.ReadMode == False:
            print("Insert Mode Toggled On")
        elif self.ReadMode == True:
            print("Insert Mode Toggled Off")

        return

    def TableIsEmpty(self):
        if self.TopScope is None:
            return True
        return False

    def ClearSymbolTable(self):
        while not self.TableIsEmpty():
            self.PopScope()
        return

    def IsGlobalScope(self):
        if len(self.Table) is 1 and self.TopScope is not None:
            return True
        return False

    def PrettyErrorPrint(self, Message, Lineno, Column):
        arrow = ""

        print(Message)

        #print line
        with open(self.SourceFile) as file:
            for i in range(0,Lineno):
                source = file.readline()
        print(source)

        #build arrow
        for i in range(0,Column-1):
            arrow += " "
        arrow += "^\n"

        print(arrow)
