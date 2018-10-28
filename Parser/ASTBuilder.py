

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
#Constants
#STRING_LITERALs
#Functions
#if statement
#declaration lists
#type specifiers
#type...modfier things like CONST or whatever
#arrays

class PostfixExpression(Node):
    def __init__(self, Loc=None):
        pass

    def GetChildren(self):
        Children = []
        return Children

    #we cannot increment a constant
    def RunSemanticAnalysis(self):
        pass

    def BuildTreeOutput(self, Parent):
        output = '{} = Node(\"{}\"{})'

        if Parent is None:
            output = output.format(self.__class__.__name__, self.__class__.__name__, "")
        else:
            output = output.format(self.__class__.__name__, self.__class__.__name__, ", parent="+Parent)

        return output




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
       with type and type specifier information.
    '''
    def __init__(self, Left=None, Right=None, Loc=None):
        self.Left = Left
        self.Right = Right
        self.Loc = Loc
        self.UpdateSymbolTable(Right)

    def GetChildren(self):
        Children = []
        if self.Left is not None: Children.append(self.Left)
        if self.Right is not None: Children.append(self.Right)
        return Children


    def UpdateSymbolTableHelper(self):
        self.UpdateSymbolTable(self.Right)

    # Designed for the BASIC CASE
    #  Must be improved with many possible left specificers
    def UpdateSymbolTable(self, DeclList):
        if DeclList is not None:
            for Child in DeclList.GetChildren():
                if Child.__class__.__name__ == 'Identifier':
                    Child.STPtr['Type'] = self.Left
                if Child.__class__.__name__ == 'InitDeclList':
                    self.UpdateSymbolTable(Child)
        else:
            return

    def RunSemanticAnalysis(self):
        pass




class Identifier(Node):
    def __init__(self, Name, STPtr, Loc, ST):
        self.Name = Name
        self.Loc = Loc
        self.STPtr = STPtr

        self.RunSemanticAnalysis(ST)

    def GetChildren(self):
        Children = None
        return Children

    def RunSemanticAnalysis(self, ST):
        #check for access before declaration
        if not ST.FindSymbolInTable(self.Name) and ST.ReadMode:
            #need a pretty error printing class
            raise Exception("Row:{1} Col:{2} Variable \"{3}\" accessed before declaration.".format('{0}', self.Loc[0], self.Loc[2], self.Name))

    # def BuildTreeOutput(self, Parent):
    #     output = '{} = Node(\"{}\"{})'
    #
    #     if Parent is None:
    #         output = output.format(self.__class__.__name__, self.__class__.__name__, "")
    #     else:
    #         output = output.format(self.__class__.__name__, self.__class__.__name__, ", parent="+Parent)
    #
    #     return output


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
        if self.op == 'DIV':
            #if const, get the lexeme
            #if zero, throw div by zero error
            pass
