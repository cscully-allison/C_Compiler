from Utils import GetBytesFromIds, FunctPrettyErrorPrint, PrettyErrorPrint, FindColumn, IsNode, GetLoc, BuildArrayString, CalcConversionFactor, SafeCheckDict
from Globals import CM, ErrManager, Label, FloatRegister, IntRegister, OutPutDataType, SCSLib, TSLib, TQLib, ST_G
from copy import deepcopy


class Node(object):
    '''Abstract base class for nodes'''
    def GetChildren(self):
        '''Retrieves an ordered list of all children beneath this node.'''
        pass

    def RunSemanticAnalysis(self):
        '''Run a context sensitive semantic analysis at the current node when being built'''
        pass


    def BuildTreeOutput(self, Parent):
        ''' Default tree output function. Inherited by all nodes.
            Overwritten in defined in a specific class.
        '''
        output = '{} = Node(\'{}\'{})'

        if Parent is None:
            output = output.format(self.__class__.__name__ + str(id(self)), self.__class__.__name__ +"_"+ str(id(self))[-4:], "")
        else:
            output = output.format(self.__class__.__name__ + str(id(self)), self.__class__.__name__ +"_"+ str(id(self))[-4:], ", parent="+Parent)

        return output



#We need to make nodes for the following Items

class PassUpNode(Node):
    '''
        Children: Must be passed in as a list of nodes when constructor is called
    '''
    def __init__(self, ProductionName, Children):
        self.ProductionName = ProductionName
        self.Children = Children

    def GetChildren(self):
        return self.Children

    def BuildTreeOutput(self, Parent):
        ''' Default tree output function. Inherited by all nodes.
            Overwritten in defined in a specific class.
        '''
        output = '{} = Node(\'{}\'{})'

        if Parent is None:
            output = output.format(self.__class__.__name__ + str(id(self)), self.ProductionName+"*"+"_"+ str(id(self))[-4:], "")
        else:
            output = output.format(self.__class__.__name__ + str(id(self)), self.ProductionName+"*"+"_"+ str(id(self))[-4:], ", parent="+Parent)

        return output

class PostfixExpression(Node):
    def __init__(self, Loc=None):
        pass

    def GetChildren(self):
        Children = []
        return Children

    #we cannot increment a constant
    def RunSemanticAnalysis(self):
        pass


class FunctionPrototype(Node):
    '''A node for specifically building a function prototype'''
    def __init__(self, DirectDeclarator=None, ParameterTypeList=None, Production=None):
        self.DirectDeclarator = DirectDeclarator
        self.ParameterTypeList = ParameterTypeList
        self.Production = Production
        self.FunctionId = None
        self.FunctionArguments = []
        self.Label = None

        # fetch id first
        self.FetchFunctionId(self.DirectDeclarator)

        # update only if subtype is previously undefined
        if 'Subtype' in self.FunctionId and self.FunctionId['Subtype'] == 'Function Prototype':
            return
        elif 'Subtype' not in self.FunctionId:
            self.ManagePrototype()
        else:
            self.ManagePrototype()

        # do semantic analysis
        self.RunSemanticAnalysis()

    def GetChildren(self):
        Children = []
        if self.DirectDeclarator is not None: Children.append(self.DirectDeclarator)
        if self.ParameterTypeList is not None: Children.append(self.ParameterTypeList)
        return Children

    def ManagePrototype(self):
        self.BuildArgumentList(self.ParameterTypeList)
        # print(self.FunctionArguments)
        self.FunctionId['Arguments'] = self.FunctionArguments
        self.FunctionId['Subtype'] = "Function Prototype"
        self.FunctionId['Label'] = self.Label

    def FetchFunctionId(self, Subtree):
        if Subtree is None: return
        if not IsNode(Subtree): return
        if Subtree.GetChildren() is None: return

        if Subtree.__class__.__name__ is "Identifier":
            self.FunctionId = Subtree.STPtr
            self.Label = Subtree.Name
        #
        # for Child in Subtree.GetChildren():
        #     if Child.__class__.__name__ is "Identifier":
        #         self.FunctionId = Child.STPtr
        #         self.Label = Child.Name
        #     if Child.__class__.__name__ is "PassUpNode":
        #         if Child.ProductionName is not "ParameterTypeList":
        #             self.FetchFunctionId(Child)
        #     else:
        #         self.FetchFunctionId(Child)

    def BuildArgumentList(self, Subtree):
            '''Actually handles the building of the arg list'''
            if Subtree is None: return
            if not IsNode(Subtree): return
            if Subtree.GetChildren() is None: return


            if Subtree.__class__.__name__ is "DeclarationSpecifiers":
                self.FunctionArguments.append(self.BuildDeclSpecsDict(self.FetchDeclSpecs(Subtree)))

            else:
                for Child in Subtree.GetChildren():
                    if Child.__class__.__name__ is "DeclarationSpecifiers":
                        self.FunctionArguments.append(self.BuildDeclSpecsDict(self.FetchDeclSpecs(Child)))
                    elif Child.__class__.__name__ is "PassUpNode":
                        if Child.ProductionName is "DirectAbstractDeclarator":
                            temp = self.FunctionArguments.pop()
                            temp['Array Size Info'] = self.FetchAbstractDeclarators(Child)
                            temp['Subtype'] = 'Array Argument'
                            self.FunctionArguments.append(temp)
                        else:
                            self.BuildArgumentList(Child)
                    # one-d array case
                    elif Child.__class__.__name__ is "PrimaryExpression":
                        temp = self.FunctionArguments.pop()
                        temp['Array Size Info'] = self.FetchAbstractDeclarators(Child)
                        temp['Subtype'] = 'Array Argument'
                        self.FunctionArguments.append(temp)

                    else:
                        self.BuildArgumentList(Child)

    def CheckForConstantExpression(self, Subtree):
        if Subtree.GetChildren() == []:
            return False
        return True

    def FetchAbstractDeclarators(self, AbstractDeclarator):
        ''' Builds up a list of the declaration specifiers recursively
        '''
        # past a leaf node case
        if AbstractDeclarator is None:
            return []
        # at a node case
        else:
            AbstractDeclaratorList = []
            for Child in AbstractDeclarator.GetChildren():
                # more nodes beneath us
                if Child.__class__.__name__ == 'PassUpNode':
                    if Child.ProductionName == 'DirectAbstractDeclarator':
                        if self.CheckForConstantExpression(Child) is False:
                            AbstractDeclaratorList.append([])
                if Child.__class__.__name__ != 'Constant':
                    # we need to check if this abstract declarator has a constant expression
                    AbstractDeclaratorList.extend(self.FetchAbstractDeclarators(Child))
                # at a leaf node
                else:
                    AbstractDeclaratorList = [Child.Child]
            # return after loop
            return AbstractDeclaratorList


    def BuildDeclSpecsDict(self, DeclSpecsList):
        ''' Converts declaration spcifier list to a queryable dictionary
        '''
        Dict = {}
        for Spec in DeclSpecsList:
            if Spec in TSLib:
                if 'Type' in Dict:
                    Dict['Type'].append(Spec)
                else:
                    Dict['Type'] = [Spec]
            elif Spec in TQLib:
                if 'Type Qualifier' in Dict:
                    Dict['Type Qualifier'].append(Spec)
                else:
                    Dict['Type Qualifier'] = [Spec]
            elif Spec in SCSLib:
                if 'Storage Class Specifier' in Dict:
                    Dict['Storage Class Specifier'].append(Spec)
                else:
                    Dict['Storage Class Specifier'] = [Spec]
        return Dict

    def FetchDeclSpecs(self, DeclSpecs):
        ''' Builds up a list of the declaration specifiers recursively
        '''
        # past a leaf node case
        if DeclSpecs is None:
            return []
        # at a node case
        else:
            DeclSpecsList = []

            for Child in DeclSpecs.GetChildren():
                # more nodes beneath us
                if Child.__class__.__name__ == 'DeclarationSpecifiers':
                    DeclSpecsList.extend(self.FetchDeclSpecs(Child))
                # at a leaf node
                else:
                    DeclSpecsList = [Child]
            # return after loop
            return DeclSpecsList

    def RunSemanticAnalysis(self):
        for Argument in self.FunctionId['Arguments']:
            if 'Storage Class Specifier' in Argument:
                ErrManager.AddError(PrettyErrorPrint("Storage class specifier on function definition argument.", self.FunctionId['TokenLocation'][0], self.FunctionId['TokenLocation'][2], self.Production.lexer.lexdata))


        pass

class FunctionDefintion(Node):
    ''' Declaration List is a Subtree
        Statement is a Subtree
        Decl List can be null
    '''
    def __init__(self, ReturnDeclarator = None, Declarator = None, DeclarationList = None, Statement = None, Loc=None, Production=None):
        self.ReturnDeclarator = ReturnDeclarator
        self.Declarator = Declarator
        self.Statement = Statement
        self.DeclarationList = DeclarationList
        self.Production = Production
        self.Loc = GetLoc(Production)
        #label and idptr come from FetchFunctionId function
        self.IDPtr = None
        self.ReturnType = None
        self.FunctionArguments = []


        #do things
        self.ManageFunctionDeclaration()
        self.RunSemanticAnalysis()



        pass

    def GetChildren(self):
        Children = []
        if self.DeclarationList is not None: Children.append(self.DeclarationList)
        if self.ReturnDeclarator is not None: Children.append(self.ReturnDeclarator)
        if self.Declarator is not None: Children.append(self.Declarator)
        if self.Statement is not None: Children.append(self.Statement)
        return Children

    def ManageFunctionDeclaration(self):
        self.FetchFunctionId(self.Declarator)
        self.ReturnType = self.BuildDeclSpecsDict(self.FetchDeclSpecs(self.ReturnDeclarator))
        self.BuildArgumentList(self.Declarator)


    def FetchFunctionId(self, Subtree):
        if Subtree is None: return
        if not IsNode(Subtree): return
        if Subtree.GetChildren() is None: return

        if Subtree.__class__.__name__ is "Identifier":
            self.IDPtr = Subtree.STPtr
            self.Label = Subtree.Name
            return

        else:
            for Child in Subtree.GetChildren():
                if Child.__class__.__name__ is "Identifier":
                    self.IDPtr = Child.STPtr
                    self.Label = Child.Name
                    break


    def BuildArgumentList(self, Subtree):
            '''Actually handles the building of the arg list'''
            if Subtree is None: return
            if not IsNode(Subtree): return
            if Subtree.GetChildren() is None: return

            DeclSpecs = None
            for Child in Subtree.GetChildren():
                if Child.__class__.__name__ == 'Identifier' and Child.Name is not self.Label:
                    self.FunctionArguments.append(Child.STPtr)
                if Child.__class__.__name__ is "DeclarationSpecifiers":
                    DeclSpecs = self.BuildDeclSpecsDict(self.FetchDeclSpecs(Child))
                else:
                    self.BuildArgumentList(Child)



    def FetchId(self, Subtree):
        if Subtree is None: return
        if not IsNode(Subtree): return
        if Subtree.GetChildren() is None: return

        for Child in Subtree.GetChildren():
            if Child.__class__.__name__ == 'Identifier':
                return (Child.Name, Child.STPtr)
            else:
                return(self.FetchId(Child))

    def BuildDeclSpecsDict(self, DeclSpecsList):
        ''' Converts declaration spcifier list to a queryable dictionary
        '''
        Dict = {}
        for Spec in DeclSpecsList:
            if Spec in TSLib:
                if 'Type' in Dict:
                    Dict['Type'].append(Spec)
                else:
                    Dict['Type'] = [Spec]
            elif Spec in TQLib:
                if 'Type Qualifier' in Dict:
                    Dict['Type Qualifier'].append(Spec)
                else:
                    Dict['Type Qualifier'] = [Spec]
            elif Spec in SCSLib:
                if 'Storage Class Specifier' in Dict:
                    Dict['Storage Class Specifier'].append(Spec)
                else:
                    Dict['Storage Class Specifier'] = [Spec]
        return Dict


    def FetchDeclSpecs(self, DeclSpecs):
        ''' Builds up a list of the declaration specifiers recursively
        '''
        # past a leaf node case
        if DeclSpecs is None:
            return []
        # at a node case
        else:
            DeclSpecsList = []
            for Child in DeclSpecs.GetChildren():
                # more nodes beneath us
                if Child.__class__.__name__ == 'DeclarationSpecifiers':
                    DeclSpecsList.extend(self.FetchDeclSpecs(Child))
                # at a leaf node
                else:
                    DeclSpecsList = [Child]
            # return after loop
            return DeclSpecsList


    def MismachedTypes(self, Prototype):
        returns = []
        if 'Return Type' in Prototype:
            if Prototype['Return Type'] != self.ReturnType['Type']:
                returns.append('Return')
        if 'Arguments' in Prototype:
            if len(Prototype['Arguments']) != len(self.FunctionArguments):
                returns.append('Number')
            else:
                for i, Arg in enumerate(Prototype['Arguments']):
                    if Arg['Type'] != self.FunctionArguments[i]['Type']:
                        returns.append('Argument')

        else:
            returns = []

        return returns

    def CheckArray(self, Prototype):
        if 'Arguments' in Prototype:
            for i, Arg in enumerate(Prototype['Arguments']):
                if 'Subtype' in Arg and Arg['Subtype'] == 'Array Argument':
                    if 'Subtype' not in self.FunctionArguments[i] or self.FunctionArguments[i]['Subtype'] != 'Array':
                            ErrManager.AddError(FunctPrettyErrorPrint("Error: Line:{} Column:{} ".format(self.Loc[0], self.Loc[2]) + "Argument data types in function definition do not match prototype. Array was expected from prototype.", self.IDPtr['TokenLocation'][0], self.IDPtr['TokenLocation'][2], self.Production.lexer.lexdata))
                    elif 'Subtype' in self.FunctionArguments[i] and self.FunctionArguments[i]['Subtype'] == 'Array':
                        if len(self.FunctionArguments[i]['Array Size']) != len(Arg['Array Size Info']):
                            ErrManager.AddError(FunctPrettyErrorPrint("Error: Line:{} Column:{} ".format(self.Loc[0], self.Loc[2]) + "Array dimensions do not match between prototype and function declaration. Prototype can be found here.", self.IDPtr['TokenLocation'][0], self.IDPtr['TokenLocation'][2], self.Production.lexer.lexdata))
                        else:
                            for i, Size in enumerate(self.FunctionArguments[i]['Array Size']):
                                if Arg['Array Size Info'][i] != Size:
                                    ErrManager.AddError(FunctPrettyErrorPrint("Error: Line:{} Column:{} ".format(self.Loc[0], self.Loc[2]) + "Array sizes do not match between prototype and function declaration. Prototype can be found here.", self.IDPtr['TokenLocation'][0], self.IDPtr['TokenLocation'][2], self.Production.lexer.lexdata))





    #we cannot increment a constant
    def RunSemanticAnalysis(self):
        #check type match with prototype (if prototype is deifned)
        if 'Subtype' in self.IDPtr and self.IDPtr['Subtype'] == 'Function Prototype':
            if 'Argument' in self.MismachedTypes(self.IDPtr):
                ErrManager.AddError(FunctPrettyErrorPrint("Error: Line:{} Column:{} ".format(self.Loc[0], self.Loc[2]) + "Argument data types in function definition do not match prototype. Prototype declaration here.", self.IDPtr['TokenLocation'][0], self.IDPtr['TokenLocation'][2], self.Production.lexer.lexdata))
            if 'Return' in self.MismachedTypes(self.IDPtr):
                ErrManager.AddError(FunctPrettyErrorPrint("Error: Line:{} Column:{} ".format(self.Loc[0], self.Loc[2]) + "Return data type in function definition does not match prototype. Prototype declaration here.", self.IDPtr['TokenLocation'][0], self.IDPtr['TokenLocation'][2], self.Production.lexer.lexdata))
            if 'Number' in self.MismachedTypes(self.IDPtr):
                ErrManager.AddError(FunctPrettyErrorPrint("Error: Line:{} Column:{} ".format(self.Loc[0], self.Loc[2]) + "Number of arguments in function definition does not match prototype. Expected {} but only found {}. Prototype declaration here.".format(len(self.IDPtr['Arguments']), len(self.FunctionArguments)), self.IDPtr['TokenLocation'][0], self.IDPtr['TokenLocation'][2], self.Production.lexer.lexdata))

        self.CheckArray(self.IDPtr)


        if 'Return Type' not in self.IDPtr and self.ReturnType == None:
            self.IDPtr['Return Type'] = ['int']
            print("Warning: Line: {} Col: {} No return type defined for function '{}', default to int.".format(self.IDPtr['TokenLocation'][0], self.IDPtr['TokenLocation'][2], self.Label))



class FunctionCall(Node):
    '''Node for a function call.
    '''
    def __init__(self, IdentifierSubtree = None, ArgumentList = None, Production = None, ST = None):
        self.IdentifierSubtree = IdentifierSubtree
        self.ArgumentList = ArgumentList
        ST_G = ST
        self.Loc = GetLoc(Production)
        self.Production = Production

        self.Label = Label.DispenseTicket()

        self.Arguments = []
        self.IdLabel = None
        self.Id = None
        self.IdPtr = None
        self.FunctionPrototypeArgs = None


        self.SetUpFunctionCall()
        self.RunSemanticAnalysis()



    def SetUpFunctionCall(self):
        self.IdLabel = self.FetchId(self.IdentifierSubtree)
        self.IdPtr = ST_G.RecoverMostRecentID(self.IdLabel)
        self.Arguments = self.FetchArguments(self.ArgumentList)
        if self.IdPtr is not False:
            self.IdPtr = self.IdPtr
            if 'Arguments' in self.IdPtr:
                self.FunctionPrototypeArgs = self.IdPtr['Arguments']
            else:
                self.FunctionPrototypeArgs = []
        else:
            return
        pass

    def FetchId(self, Subtree):
        if Subtree is None: return
        if not IsNode(Subtree): return
        if Subtree.GetChildren() is None: return

        for Child in Subtree.GetChildren():
            if Child.__class__.__name__ == 'Identifier':
                return Child.Name
            else:
                return(self.FetchId(Child))

    def FetchArguments(self, Args):
        ''' Builds up a list of the declaration specifiers recursively
        '''
        # past a leaf node case
        if not IsNode(Args): return []
        if Args is None:
            return []
        # at a node case
        else:
            ArgsList = []
            for Child in Args.GetChildren():
                # more nodes beneath us
                if Child.__class__.__name__ == 'Constant':
                    Arg = {'Type':[Child.DataType] ,'Value':Child.Child, 'Type Qualifier':['const']}
                    ArgsList = [Arg]
                elif Child.__class__.__name__ == 'Identifier':
                    ArgsList = [deepcopy(Child.STPtr)]
                # at a leaf node
                else:
                    ArgsList.extend(self.FetchArguments(Child))

            # return after loop
            return ArgsList

    def GetChildren(self):
        Children = []
        if self.IdentifierSubtree is not None: Children.append(self.IdentifierSubtree)
        if self.ArgumentList is not None: Children.append(self.ArgumentList)
        return Children

    def RunSemanticAnalysis(self):
        if self.IdPtr is False:
            ErrManager.AddError(PrettyErrorPrint("Function '{}' undefined.".format(self.IdLabel), self.Loc[0], self.Loc[2], self.Production.lexer.lexdata))
            return

        # check for mismatched number of arguments
        if len(self.Arguments) != len(self.FunctionPrototypeArgs):
            ErrManager.AddError(FunctPrettyErrorPrint("Error: Line:{} Column:{} ".format(self.Loc[0], self.Loc[2]) + "Number of arguments in function call does not match prototype. Expected {} but only found {}. Prototype declaration here.".format(len(self.FunctionPrototypeArgs), len(self.Arguments)), self.IdPtr['TokenLocation'][0], self.IdPtr['TokenLocation'][2], self.Production.lexer.lexdata))

        # check for incorrect argument types
        else:
            for i, arg in enumerate(self.Arguments):
                if 'Subtype' in arg and arg['Subtype'] == 'Array':
                    if 'Subtype' not in self.FunctionPrototypeArgs[i] or self.FunctionPrototypeArgs[i]['Subtype'] != 'Array Argument':
                        ErrManager.AddError(FunctPrettyErrorPrint("Error: Line:{} Column:{} ".format(self.Loc[0], self.Loc[2]) +
                            "Argument types in function call does not match prototype. Expected '{}' but found '{}'. Prototype declaration here.".format(BuildArrayString(self.FunctionPrototypeArgs[i]['Type'], []), BuildArrayString(arg['Type'], arg['Array Size'])), self.IdPtr['TokenLocation'][0], self.IdPtr['TokenLocation'][2], self.Production.lexer.lexdata))
                if 'Subtype' in self.FunctionPrototypeArgs[i] and self.FunctionPrototypeArgs[i]['Subtype'] == 'Array Argument':
                    if 'Subtype' not in arg or arg['Subtype'] != 'Array':
                        ErrManager.AddError(FunctPrettyErrorPrint("Error: Line:{} Column:{} ".format(self.Loc[0], self.Loc[2]) +
                            "Argument types in function call does not match prototype. Expected '{}' but found '{}'. Prototype declaration here.".format(BuildArrayString(self.FunctionPrototypeArgs[i]['Type'], self.FunctionPrototypeArgs[i]['Array Size Info']), BuildArrayString(arg['Type'], [])), self.IdPtr['TokenLocation'][0], self.IdPtr['TokenLocation'][2], self.Production.lexer.lexdata))
                if 'Subtype' in self.FunctionPrototypeArgs[i] and self.FunctionPrototypeArgs[i]['Subtype'] == 'Array Argument' and 'Subtype' in arg and arg['Subtype'] == 'Array':
                    if len(self.FunctionPrototypeArgs[i]['Array Size Info']) != len(arg['Array Size']):
                        ErrManager.AddError(FunctPrettyErrorPrint("Error: Line:{} Column:{} ".format(self.Loc[0], self.Loc[2]) +
                            "Array dimensions in function call does not match prototype. Expected '{}' but found '{}'. Prototype declaration here.".format(BuildArrayString(self.FunctionPrototypeArgs[i]['Type'], self.FunctionPrototypeArgs[i]['Array Size Info']), BuildArrayString(arg['Type'],  arg['Array Size'])), self.IdPtr['TokenLocation'][0], self.IdPtr['TokenLocation'][2], self.Production.lexer.lexdata))
                if 'Subtype' in self.FunctionPrototypeArgs[i] and self.FunctionPrototypeArgs[i]['Subtype'] == 'Array Argument' and 'Subtype' in arg and arg['Subtype'] == 'Array' or 'Subtype' not in arg and 'Subtype' not in self.FunctionPrototypeArgs[i]:
                    if self.FunctionPrototypeArgs[i]['Type'] != arg['Type']:
                        arg['Coerced Type'] = self.FunctionPrototypeArgs[i]['Type']
                        print("Warning: Line: {} Col: {} Implicit cast of argument {} in function call \"{}\" from {}to {}".format(self.Loc[0], self.Loc[2], i+1, self.IdLabel, OutPutDataType(arg['Type']), OutPutDataType(self.FunctionPrototypeArgs[i]['Type'])))


class DeclList(Node):
    '''Self refrencing production like init decl list.
    '''
    def __init__(self, DeclList=None, Decl=None, Loc=None):
        self.DeclList = DeclList
        self.Decl = Decl

    def GetChildren(self):
        Children = []
        if self.DeclList is not None: Children.append(self.DeclList)
        if self.Decl is not None: Children.append(self.Decl)
        return Children

    #we cannot increment a constant
    def RunSemanticAnalysis(self):
        pass


class DeclarationSpecifiers(Node):
    ''' This class represents the static const int etc part of
        a variable declaration. Needs to store the type_specifier
        and be able to walk down the storage class specifiers
    '''
    def __init__(self, SCSpec=None, TSpec=None, TQual=None, DeclSpec=None,  Loc=None):
        self.SCSpec = SCSpec
        self.TSpec = TSpec
        self.TQual = TQual
        self.DeclSpec = DeclSpec

    def GetChildren(self):
        Children = []
        if self.SCSpec is not None: Children.append(self.SCSpec)
        if self.TSpec is not None: Children.append(self.TSpec)
        if self.TQual is not None: Children.append(self.TQual)
        if self.DeclSpec is not None: Children.append(self.DeclSpec)
        return Children


    #we cannot increment a constant
    def RunSemanticAnalysis(self):
        pass


class InitDeclList(Node):
    ''' Decl is the declarator at this point in our tree
        DeclList is the subtree where we got our Decls from
    '''
    def __init__(self, DeclList=None, Decl=None, Loc=None):
        self.DeclList = DeclList
        self.Decl = Decl


    def GetChildren(self):
        Children = []
        if self.DeclList is not None: Children.append(self.DeclList)
        if self.Decl is not None: Children.append(self.Decl)
        return Children

    #we cannot increment a constant
    def RunSemanticAnalysis(self):
        pass



class Declaration(Node):
    '''Left: Declaration Specificers
       Right: Declarator List
       This node has the side affect of updating the symbol table
       with type, type qualifier and storage class specifier information.
    '''
    def __init__(self, Left=None, Right=None, Loc=None):
        self.Left = Left
        self.Right = Right
        self.Loc = Loc
        self.ID = []
        self.DeclLabel = []
        self.IDCtr = 0;
        self.Bytes = 1;

        #gets and formats the declaration specifiers
        self.DeclSpecs = self.BuildDeclSpecsDict( self.FetchDeclSpecs(self.Left) )

        #updates the symbol table
        self.UpdateSymbolTable(Right)

        # for list declarations gets the required number of bytes for each var
        self.Bytes = self.CalcBytes(self.DeclSpecs);

    def CalcBytes(self, DeclSpecs):
        Bytes = 0
        DTCBytes = 0
        Type = DeclSpecs['Type']
        DTCBytes = CM.TypeToBytes(Type)


        # caluclates a conditional for arrays and normal data types space allocaton
        Bytes = GetBytesFromIds(self.ID, DTCBytes)


        return Bytes

    def GetChildren(self):
        Children = []
        if self.Left is not None: Children.append(self.Left)
        if self.Right is not None: Children.append(self.Right)
        return Children

    def BuildDeclSpecsDict(self, DeclSpecsList):
        ''' Converts declaration spcifier list to a queryable dictionary
        '''
        Dict = {}
        for Spec in DeclSpecsList:
            if Spec in TSLib:
                if 'Type' in Dict:
                    Dict['Type'].append(Spec)
                else:
                    Dict['Type'] = [Spec]
            elif Spec in TQLib:
                if 'Type Qualifier' in Dict:
                    Dict['Type Qualifier'].append(Spec)
                else:
                    Dict['Type Qualifier'] = [Spec]
            elif Spec in SCSLib:
                if 'Storage Class Specifier' in Dict:
                    Dict['Storage Class Specifier'].append(Spec)
                else:
                    Dict['Storage Class Specifier'] = [Spec]
        return Dict


    def FetchDeclSpecs(self, DeclSpecs):
        ''' Builds up a list of the declaration specifiers recursively
        '''
        # past a leaf node case
        if DeclSpecs is None:
            return []
        # at a node case
        else:
            DeclSpecsList = []
            for Child in DeclSpecs.GetChildren():
                # more nodes beneath us
                if Child.__class__.__name__ == 'DeclarationSpecifiers':
                    DeclSpecsList.extend(self.FetchDeclSpecs(Child))
                # at a leaf node
                else:
                    DeclSpecsList = [Child]
            # return after loop
            return DeclSpecsList


    def UpdateSymbolTable(self, DeclList):
        if DeclList.__class__.__name__ == 'Identifier':
                self.ID.append(DeclList.STPtr)
                self.DeclLabel.append(DeclList.Name)
                self.IDCtr += 1;
                # inserting for function prototypes
                if 'Subtype' in DeclList.STPtr and DeclList.STPtr['Subtype'] == 'Function Prototype':
                    DeclList.STPtr['Return Type'] = self.DeclSpecs['Type']
                else:
                    DeclList.STPtr['Type'] = self.DeclSpecs['Type']

                if 'Type Qualifier' in self.DeclSpecs:
                    DeclList.STPtr['Type Qualifier'] = self.DeclSpecs['Type Qualifier']
                if 'Storage Class Specifier' in self.DeclSpecs:
                    DeclList.STPtr['Storage Class Specifier'] = self.DeclSpecs['Storage Class Specifier'][0]


        elif DeclList is not None and IsNode(DeclList):
            for Child in DeclList.GetChildren():
                if Child.__class__.__name__ == 'Identifier':
                    self.ID.append(Child.STPtr)
                    self.DeclLabel.append(Child.Name)
                    self.IDCtr += 1;
                    # inserting for function prototypes
                    if 'Subtype' in Child.STPtr and Child.STPtr['Subtype'] == 'Function Prototype':
                        Child.STPtr['Return Type'] = self.DeclSpecs['Type']
                    else:
                        Child.STPtr['Type'] = self.DeclSpecs['Type']

                    if 'Type Qualifier' in self.DeclSpecs:
                        Child.STPtr['Type Qualifier'] = self.DeclSpecs['Type Qualifier']
                    if 'Storage Class Specifier' in self.DeclSpecs:
                        Child.STPtr['Storage Class Specifier'] = self.DeclSpecs['Storage Class Specifier'][0]
                else:
                    self.UpdateSymbolTable(Child)
        else:
            return

    def RunSemanticAnalysis(self):
        # check that only one meaningful Type exists
        # check that only one Storage Class Specifier Exists
        pass


class ArrayDeclaration(Node):
    '''This class will handle the special case of array declarations'''
    def __init__(self, Declarator, SizeExpr, Production):
        self.Declarator = Declarator
        self.SizeExpr = SizeExpr
        self.Production = Production
        self.Id = self.FetchId(Declarator)[0]
        self.Label = self.FetchId(Declarator)[1]

        # update the symbol table with size and subtype information
        if SizeExpr is not None: self.GetSize(SizeExpr)
        self.Id['Subtype'] = 'Array'

        self.RunSemanticAnalysis()

    def GetChildren(self):
        Children = []
        if self.Declarator is not None: Children.append(self.Declarator)
        if self.SizeExpr is not None: Children.append(self.SizeExpr)
        return Children

    def GetSize(self, Subtree):
        '''Updates ID ptr with the size denoted by the constant expression'''
        if Subtree is None: return []
        elif not IsNode(Subtree): return []

        else:
            for Child in Subtree.GetChildren():
                if Child.__class__.__name__ == 'Constant':
                    if Child.DataType is not 'int':
                        ErrManager.AddError(PrettyErrorPrint("Size of array declaration \"{}\" has non-integer type.".format(self.Label), self.Id['TokenLocation'][0], self.Id['TokenLocation'][2], self.Production.lexer.lexdata))

                    if 'Array Size' not in self.Id:
                        self.Id['Array Size'] = [Child.Child]
                    else:
                        self.Id['Array Size'] += [Child.Child]
                else:
                    self.GetSize(Child)

    def FetchId(self, Subtree):
        if Subtree is None: return
        if not IsNode(Subtree): return
        if Subtree.GetChildren() is None: return

        if Subtree.__class__.__name__ == 'Identifier':
            return (Subtree.STPtr, Subtree.Name)

        for Child in Subtree.GetChildren():
            if Child.__class__.__name__ == 'Identifier':
                return (Child.STPtr, Child.Name)
            else:
                return(self.FetchId(Child))


    #we cannot increment a constant
    def RunSemanticAnalysis(self):


        pass


class Identifier(Node):
    def __init__(self, Name, STPtr, Loc, ST, P):
        self.Name = Name
        if STPtr is not False:
            self.STPtr = STPtr
        else:
            self.STPtr = None
        self.Loc = Loc
        self.Production = P

        self.RunSemanticAnalysis(ST)

    def GetChildren(self):
        Children = []
        if self.Name is not None: Children.append(self.Name)
        if self.STPtr is not None: Children.append(self.STPtr)
        return Children

    def RunSemanticAnalysis(self, ST):
        #check for access before declaration
        if not ST.FindSymbolInTable(self.Name) and ST.ReadMode:
            #need a pretty error printing class
            # ErrManager.AddError("Row:{1} Col:{2} Variable \"{3}\" accessed before declaration.".format('{0}', self.Loc[0], self.Loc[2], self.Name))
            ErrManager.AddError(PrettyErrorPrint("Variable \"{0}\" accessed before declaration.".format(self.Name), self.Loc[0], self.Loc[2], self.Production.lexer.lexdata ))


class Constant(Node):
    def __init__(self, DataType, Child, Loc=None):
        self.DataType = DataType
        self.Child = Child
        pass

    def GetChildren(self):
        Children = []
        Children.append(self.Child)
        return Children

    #we cannot increment a constant
    def RunSemanticAnalysis(self):
        pass


class PrimaryExpression(Node):
    def __init__(self, Type, Child, Loc=None):
        self.Type = Type
        self.Child = Child
        self.Loc = Loc

    def GetChildren(self):
        Children = []
        Children.append(self.Child)
        return Children

    def RunSemanticAnalysis(self):
        pass


class UnaryExpression(Node):
    def __init__(self, Op, Child, Loc=None):
        self.Loc = Loc
        self.Op = Op
        self.Child = Child

        self.RunSemanticAnalysis()

    def GetChildren(self):
        Children = []
        Children.append(self.Child)
        return Children

    def RunSemanticAnalysis(self):
        if (self.Child.Type == 'constant' or
        self.Child.Type == 'string') and (self.Op == "++" or
        self.Op == "--" ):
                ErrManager.AddError("Row:{1} Col:{2} Attempted increment of constant.".format('{0}', self.Loc[0], self.Loc[1]))
        pass

class CompoundStatement(Node):
    def __init__(self, DecList = None, StmtList = None, Loc=None):
        self.DecList = DecList
        self.StmtList = StmtList
        self.Loc = Loc

    def GetChildren(self):
        Children = []
        if self.DecList is not None: Children.append(self.DecList)
        if self.StmtList is not None: Children.append(self.StmtList)
        return Children

    #we cannot increment a constant
    def RunSemanticAnalysis(self):
        pass

class AssignmentExpression(Node):
    def __init__(self, Op, Left, Right, ST, Loc=None, Production=None):
        self.Op = Op
        self.Loc = GetLoc(Production)
        self.Left = Left
        self.Right = Right
        self.Production = Production

        self.ManageExprDataTypes()
        self.RunSemanticAnalysis(ST)

    def GetChildren(self):
        Children = []
        if self.Left is not None: Children.append(self.Left)
        if self.Right is not None: Children.append(self.Right)
        return Children

    #we cannot increment a constant
    def RunSemanticAnalysis(self, ST):
        LHSId = self.FetchId(self.Left)
        LHS = ST.FindSymbolInTable(LHSId)

        if LHS is False:
            return
        for ID in LHS:
            if "Type Qualifier" in ID:
                for qualifier in LHS[0]["Type Qualifier"]:
                    if qualifier == 'const':
                        ErrManager.AddError(PrettyErrorPrint("Attempted Access of Const Variable \"{}\".".format(LHSId),
                                self.Production.lexer.lineno,
                                    FindColumn(self.Production.lexer.lexdata,
                                        self.Production.lexer
                                    ),
                                self.Production.lexer.lexdata )
                            )


    def FetchId(self, Subtree):
        if Subtree is None: return
        if not IsNode(Subtree): return
        if Subtree.GetChildren() is None: return


        for Child in Subtree.GetChildren():
            if Child.__class__.__name__ == 'Identifier':
                return Child.Name
            else:
                return(self.FetchId(Child))

    def ManageExprDataTypes(self):
        LDT = self.GetBinOpDataType(self.Left)
        RDT = self.GetBinOpDataType(self.Right)



        #set the overall type of the expression
        DominantType = self.EvalDataType(LDT, RDT)
        if DominantType is 'Equal':
            self.ExprDataType = LDT
        else:
            self.ExprDataType = LDT
            temp = self.Right
            self.Right = CastNode(RDT, LDT, temp)
            print("Warning: Line: {} Col: {} Implicit cast in assignment from {}to {}".format(self.Loc[0], self.Loc[2], OutPutDataType(RDT), OutPutDataType(LDT)))


        if 'float' in self.ExprDataType:
            self.Register = FloatRegister.DispenseTicket()
        else:
            self.Register = IntRegister.DispenseTicket()



    def GetBinOpDataType(self, Subtree):
        if Subtree is None: return
        if not IsNode(Subtree): return
        if Subtree.GetChildren() is None: return

        if Subtree.__class__.__name__ == "BinOp":
            return Subtree.ExprDataType

        else:
            for Child in Subtree.GetChildren():
                if Child.__class__.__name__ == 'Constant':
                    return [Child.DataType]
                if Child.__class__.__name__ == 'Identifier':
                    return Child.STPtr["Type"]
                if Child.__class__.__name__ == "BinOp":
                    LDT = self.GetBinOpDataType(Child.Left)
                    RDT = self.GetBinOpDataType(Child.Right)

                    if LDT == RDT:
                        return LDT
                else:
                    return self.GetBinOpDataType(Child)


    def EvalDataType(self, LHS, RHS):
        '''Returns the data type which should be coreced to'''
        if CalcConversionFactor(LHS) < CalcConversionFactor(RHS):
            return LHS
        elif CalcConversionFactor(LHS) > CalcConversionFactor(RHS):
            return RHS
        elif CalcConversionFactor(LHS) == CalcConversionFactor(RHS):
            return 'Equal'


class BinOp(Node):
    def __init__(self, Op, Left, Right, Production, Loc = None):
        self.Left = Left
        self.Right = Right
        self.Op = Op
        self.Loc = GetLoc(Production)
        self.ExprDataType = None
        self.Register = None


        self.ManageExprDataTypes()
        self.RunSemanticAnalysis(None)

    def GetChildren(self):
        Children = []

        if self.Left is not None:
            Children.append(self.Left)
        if self.Op is not None:
            Children.append(self.Op)
        if self.Right is not None:
            Children.append(self.Right)
        if self.ExprDataType is not None:
            Children.append(self.ExprDataType)
        if self.Register is not None:
            Children.append(self.Register)

        return Children

    def ManageExprDataTypes(self):
        LDT = self.GetBinOpDataType(self.Left)
        RDT = self.GetBinOpDataType(self.Right)

        #set the overall type of the expression
        DominantType = self.EvalDataType(LDT, RDT)
        if DominantType is 'Equal':
            self.ExprDataType = LDT
        else:
            self.ExprDataType = DominantType
            # Adding cast nodes
            if DominantType == LDT:
                #add node on self.Right
                temp = self.Right
                self.Right = CastNode(RDT, LDT, temp)
                print("Warning: Line: {} Col: {} Implicit cast from {}to {}".format(self.Loc[0], self.Loc[2], OutPutDataType(RDT), OutPutDataType(LDT)))
            else:
                # add node on self.Left
                temp = self.Left
                self.Left = CastNode(RDT, LDT, temp)
                print("Warning: Line: {} Col: {} Implicit cast from {}to {}".format(self.Loc[0], self.Loc[2], OutPutDataType(LDT), OutPutDataType(RDT)))

        if 'float' in self.ExprDataType:
            self.Register = FloatRegister.DispenseTicket()
        else:
            self.Register = IntRegister.DispenseTicket()



    def GetBinOpDataType(self, Subtree):
        if Subtree is None: return
        if not IsNode(Subtree): return
        if Subtree.GetChildren() is None: return

        for Child in Subtree.GetChildren():
            # if Child.__class__.__name__ == "BinOp":
            #     # if Child.ExprDataType is not None:
            #     #     return Child.ExprDataType
            if Child.__class__.__name__ == 'Constant':
                return [Child.DataType]
            if Child.__class__.__name__ == 'Identifier':
                if SafeCheckDict(Child.STPtr, 'Type'):
                    return Child.STPtr['Type']
                else:
                    raise ValueError("Fatal error, see logs below.")
            if Child.__class__.__name__ == "BinOp":
                # print(Child.Left, Child.Right)
                LDT = self.GetBinOpDataType(Child.Left)
                RDT = self.GetBinOpDataType(Child.Right)
                if LDT == RDT:
                    return LDT
                else:
                    if Child.ExprDataType is not None:
                         return Child.ExprDataType
            else:
                return self.GetBinOpDataType(Child)


    def EvalDataType(self, LHS, RHS):
        '''Returns the data type which should be coreced to'''
        if CalcConversionFactor(LHS) < CalcConversionFactor(RHS):
            return LHS
        elif CalcConversionFactor(LHS) > CalcConversionFactor(RHS):
            return RHS
        elif CalcConversionFactor(LHS) == CalcConversionFactor(RHS):
            return 'Equal'




    def RunSemanticAnalysis(self, ST):
            pass


class SelectionStatement(Node):
    def __init__(self, IfExpression=None, ThenBlock=None, ElseBlock = None, Loc=None):
        self.IfExpression = IfExpression
        self.ThenBlock = ThenBlock
        self.ElseBlock = ElseBlock
        self.Loc = Loc

        if self.ThenBlock is not None: self.ElseLabel = Label.DispenseTicket()

        self.End = Label.DispenseTicket()

    def GetChildren(self):
        Children = []
        if self.IfExpression is not None: Children.append(self.IfExpression)
        if self.ThenBlock is not None: Children.append(self.ThenBlock)
        if self.ElseBlock is not None: Children.append(self.ElseBlock)
        return Children

    #we cannot increment a constant
    def RunSemanticAnalysis(self):
        pass


class IterationStatement(Node):
    def __init__(self, AssignmentExpression = None, ConditionalExpression = None, IterativeExpression = None, Statement = None, Production = None):
        self.AssignmentExpression = AssignmentExpression
        self.ConditionalExpression = ConditionalExpression
        self.IterativeExpression = IterativeExpression
        self.Statement = Statement
        self.Production = Production

        if self.ConditionalExpression is not None: self.StartLabel = Label.DispenseTicket()
        if self.Statement is not None: self.EndLabel = Label.DispenseTicket()

    def GetChildren(self):
        Children = []
        if self.AssignmentExpression is not None: Children.append(self.AssignmentExpression)
        if self.ConditionalExpression is not None: Children.append(self.ConditionalExpression)
        if self.IterativeExpression is not None: Children.append(self.IterativeExpression)
        if self.Statement is not None: Children.append(self.Statement)
        #if self.Production is not None: Children.append(self.Production)
        return Children

    #we cannot increment a constant
    def RunSemanticAnalysis(self):
        pass


class ArrayAccess(Node):
    def __init__(self, ArrayName = None, ArrayOffset = None, ST = None, Production = None):
        self.Loc = GetLoc(Production)
        self.Production = Production
        self.ArrayName = ArrayName
        self.ArrayOffset = ArrayOffset
        self.ArrayType = None
        self.CurrentOffset = []
        self.SymbolLocation = None
        self.Label = self.FetchId(ArrayName)


        #appends offset from inner level
        for child in ArrayName.GetChildren():
            if child.__class__.__name__ == 'list':
                    if len(child) < 2:
                        self.CurrentOffset += child

       
        if self.Label is not False:
            self.SymbolLocation = ST.RecoverMostRecentID(self.Label)

        self.CurrentOffset += self.GetIndex(ArrayName) + self.GetIndex(ArrayOffset)

        if self.SymbolLocation is not None:
            self.ArrayType = self.SymbolLocation["Type"]

        self.RunSemanticAnalysis()

   # def DigForChecks(self, Subtree, ArrayLevel):
    #    if Subtree is not False:

     #       if (len(self.TempSizes) == 0):
      #          self.TempSizes = Subtree.TempSizes
       #     if self.CurrentOffset > self.TempSizes[ArrayLevel]:
        #        return False
         #   else:
        #        return True
        #if Subtree is False:

         #   for Child in self.GetChildren():
          #      if Child.__class__.__name__ == 'ArrayAccess':
           #         self.DigForChecks(Child, ArrayLevel+1)


    def GetIndex(self, Subtree):
        if Subtree is None: return []
        if not IsNode(Subtree): return []
        if Subtree.GetChildren() is None: return []

        RunnningTotal = []

        for Child in Subtree.GetChildren():
            if Child.__class__.__name__ == 'ArrayAccess':
                RunnningTotal += Child.CurrentOffset
            elif Child.__class__.__name__ == 'Constant':
                if Child.DataType is not 'int':
                    ErrManager.AddError(PrettyErrorPrint("Access of array \"{}\" has non-integer type.".format(self.Label), self.Loc[0], self.Loc[2], self.Production.lexer.lexdata))
                    pass
                RunnningTotal += Child.Child
            elif Child.__class__.__name__ == 'Identifier' and not SafeCheckDict(Child.STPtr, 'Subtype', 'Array'):
                RunnningTotal += Child.Name
            else:
                RunnningTotal += self.GetIndex(Child)

        return RunnningTotal


    def GetChildren(self):
        Children = []
        if self.ArrayOffset is not None: Children.append(self.ArrayOffset)
        if self.ArrayName is not None: Children.append(self.ArrayName)
        # if self.TempSizes is not None: Children.append(self.TempSizes)
        # if self.CurrentOffset is not None: Children.append(self.CurrentOffset)
        return Children

    def FetchId(self, Subtree):
        if Subtree is None: return False
        if not IsNode(Subtree): return False
        if Subtree.GetChildren() is None: return False

        if Subtree.__class__.__name__ == 'Identifier' and SafeCheckDict(Subtree.STPtr, 'Subtype', 'Array'):
            return Subtree.Name
        elif Subtree.__class__.__name__ == 'ArrayAccess':
            return Subtree.Label
        else:
            for Child in Subtree.GetChildren():
                if Child.__class__.__name__ == 'Identifier' and SafeCheckDict(Child.STPtr, 'Subtype', 'Array'):
                    return Child.Name
                elif Child.__class__.__name__ == 'ArrayAccess':
                    return Subtree.Label
                else:
                    return(self.FetchId(Child))

    def CheckCorrectArgNumber(self, Depth):
        return True


    def RunSemanticAnalysis(self):
        #if self.DigForChecks(self.SymbolLocation, 0) == False:
            #ErrManager.AddError("Row:{} Col:{} Array Acces out of bounds of allocated array memory")

        pass


class ReturnNode(Node):
    def __init__(self, ReturnExpression=None, Loc = None, Production=None):
        self.ReturnExpression = ReturnExpression
        self.Loc = Loc
        self.Production = Production

    def GetChildren(self):
        Children = []
        if self.ReturnExpression is not None: Children.append(self.ReturnExpression)
        return Children

    def RunSemanticAnalysis(self):
        pass


class CastNode(Node):
    def __init__(self, CastFrom, CastTo, SubExpression, Loc = None):
        self.CastFrom = CastFrom
        self.CastTo = CastTo
        self.SubExpression = SubExpression
        self.Loc = Loc

    def GetChildren(self):
        Children = []
        if self.CastFrom is not None: Children.append(self.CastFrom)
        if self.CastTo is not None: Children.append(self.CastTo)
        if self.SubExpression is not None: Children.append(self.SubExpression)
        return Children

    def RunSemanticAnalysis(self):
        pass
