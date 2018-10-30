

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
        output = '{} = Node(\"{}\"{})'

        if Parent is None:
            output = output.format(self.__class__.__name__ + str(id(self)), self.__class__.__name__, "")
        else:
            output = output.format(self.__class__.__name__ + str(id(self)), self.__class__.__name__, ", parent="+Parent)

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
        output = '{} = Node(\"{}\"{})'

        if Parent is None:
            output = output.format(self.__class__.__name__ + str(id(self)), self.ProductionName, "")
        else:
            output = output.format(self.__class__.__name__ + str(id(self)), self.ProductionName, ", parent="+Parent)

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
        #there will likely be other fancy things here
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
        if DeclList is not None:
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


class Identifier(Node):
    def __init__(self, Name, STPtr, Loc, ST):
        self.Name = Name
        self.STPtr = STPtr
        self.Loc = Loc

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
            raise Exception("Row:{1} Col:{2} Variable \"{3}\" accessed before declaration.".format('{0}', self.Loc[0], self.Loc[2], self.Name))


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
                raise Exception("Row:{1} Col:{2} Attempted increment of constant.".format('{0}', self.Loc[0], self.Loc[1]))
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
    def __init__(self, Op, Left, Right, Loc=None):
        self.Op = Op
        self.Loc = Loc
        self.Left = Left
        self.Right = Right

        self.RunSemanticAnalysis()


    def GetChildren(self):
        Children = []
        if self.Left is not None: Children.append(self.Left)
        if self.Right is not None: Children.append(self.Right)
        return Children

    #we cannot increment a constant
    def RunSemanticAnalysis(self):
        pass

    def AddImplicitCast(self):
        pass


class BinOp(Node):
    def __init__(self, Op, Left, Right, Loc):
        self.Left = Left
        self.Right = Right
        self.Op = Op

        self.RunSemanticAnalysis()

    def GetChildren(self):
        Children = []

        if self.Left is not None:
            Children.append(self.Left)
        if self.Right is not None:
            Children.append(self.Right)

        return Children

    def RunSemanticAnalysis(self, ST):
            pass
