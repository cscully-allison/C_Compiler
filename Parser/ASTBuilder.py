from Utils import PrettyErrorPrint, FindColumn, IsNode
from Globals import ErrManager, Label, FloatRegister, IntRegister



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
            output = output.format(self.__class__.__name__ + str(id(self)), self.ProductionName+"_"+ str(id(self))[-4:], "")
        else:
            output = output.format(self.__class__.__name__ + str(id(self)), self.ProductionName+"_"+ str(id(self))[-4:], ", parent="+Parent)

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



class FunctionDefintion(Node):
    ''' Declaration List is a Subtree
        Statement is a Subtree
        Decl List can be null
    '''
    def __init__(self, ReturnDeclarator = None, Declarator = None, DeclarationList = None, Statement = None, Loc=None):
        self.ReturnDeclarator = ReturnDeclarator
        self.Declarator = Declarator
        self.Statement = Statement
        self.DeclarationList = DeclarationList
        #there will likely be other fancy thins here
        self.Label = Label.DispenseTicket() # This should go into the symbol table
        pass

    def GetChildren(self):
        Children = []
        if self.DeclarationList is not None: Children.append(self.DeclarationList)
        Children.append(self.ReturnDeclarator)
        Children.append(self.Declarator)
        Children.append(self.Statement)
        return Children

    #we cannot increment a constant
    def RunSemanticAnalysis(self):
        # if return type None then default to int
        # and throw warning, not error
        pass

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

        #needed for checking the specific subtype of the returned declaration specifier
        self.TSLib = ['void', 'char', 'int', 'float', 'long', 'double', 'short', 'signed', 'unsigned', 'struct', 'union']
        self.TQLib = ['const', 'volatile']
        self.SCSLib = ['auto', 'register', 'static', 'extern', 'typedef']

        #gets and formats the declaration specifiers
        self.DeclSpecs = self.BuildDeclSpecsDict( self.FetchDeclSpecs(self.Left) )

        #updates the symbol table
        self.UpdateSymbolTable(Right)

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
            if Spec in self.TSLib:
                if 'Type' in Dict:
                    Dict['Type'].append(Spec)
                else:
                    Dict['Type'] = [Spec]
            elif Spec in self.TQLib:
                if 'Type Qualifier' in Dict:
                    Dict['Type Qualifier'].append(Spec)
                else:
                    Dict['Type Qualifier'] = [Spec]
            elif Spec in self.SCSLib:
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
        if DeclList is not None and IsNode(DeclList):
            for Child in DeclList.GetChildren():
                if Child.__class__.__name__ == 'Identifier':
                    Child.STPtr['Type'] = self.DeclSpecs['Type'][0]
                    if 'Type Qualifier' in self.DeclSpecs: Child.STPtr['Type Qualifier'] = self.DeclSpecs['Type Qualifier']
                    if 'Storage Class Specifier' in self.DeclSpecs: Child.STPtr['Storage Class Specifier'] = self.DeclSpecs['Storage Class Specifier'][0]

                else:
                    self.UpdateSymbolTable(Child)
        else:
            return

    def RunSemanticAnalysis(self):
        # check that only one Type exists
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
        '''Updates ID pte with the size denoted by the constant expression'''
        if Subtree is None: return []
        elif not IsNode(Subtree): return []

        else:
            for Child in Subtree.GetChildren():
                if Child.__class__.__name__ == 'Constant':
                    if Child.DataType is not 'int':
                        ErrManager.AddError(PrettyErrorPrint("Size of array \"{}\" has non-integer type.".format(self.Label), self.Id['TokenLocation'][0], self.Id['TokenLocation'][2], self.Production.lexer.lexdata))

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
        print(self.Op, self.Child.Type)
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
        self.Loc = Loc
        self.Left = Left
        self.Right = Right
        self.Production = Production

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

    def AddImplicitCast(self):
        pass


class BinOp(Node):
    def __init__(self, Op, Left, Right, Loc = None):
        self.Left = Left
        self.Right = Right
        self.Op = Op
        self.Loc = Loc
        # self.Register =

        self.RunSemanticAnalysis(None)

    def GetChildren(self):
        Children = []

        if self.Left is not None:
            Children.append(self.Left)
        if self.Op is not None:
            Children.append(self.Op)
        if self.Right is not None:
            Children.append(self.Right)

        return Children

    def RunSemanticAnalysis(self, ST):
            pass


class SelectionStatement(Node):
    def __init__(self, IfExpression=None, ThenBlock=None, ElseBlock = None, Loc=None):
        self.IfExpression = IfExpression
        self.ThenBlock = ThenBlock
        self.ElseBlock = ElseBlock
        self.Loc = Loc

        if self.ThenBlock is not None: self.ThenLabel = Label.DispenseTicket()
        if self.ElseBlock is not None: self.ElseLabel = Label.DispenseTicket()

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
        self.ContitionalExpression = ConditionalExpression
        self.IterativeExpression = IterativeExpression
        self.Statement = Statement
        self.Production = Production

    def GetChildren(self):
        Children = []
        return Children

    #we cannot increment a constant
    def RunSemanticAnalysis(self):
        pass
