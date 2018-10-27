class Node(object):
    '''Abstract base class for nodes'''
    def GetChildren(self):
        '''Retrieves an ordered list of all children beneath this node.'''
        pass

    def RunSemanticAnalysis(self):
        '''Run a context sensitive semantic analysis at the current node when being built'''
        pass


#We need to make nodes for the following Items
#Constants
#STRING_LITERALs
#Functions
#if statement
#declaration lists
#type specifiers
#type...modfier things like CONST or whatever
#arrays



class Identifier(Node):
    def __init__(self, Name, Loc, ST):
        self.Name = Name
        self.Loc = Loc

        self.RunSemanticAnalysis(ST)

    def GetChildren(self):
        Children = None
        return Children

    def RunSemanticAnalysis(self, ST):
        #check for access before declaration
        if not ST.FindSymbolInTable(self.Name) and ST.ReadMode:
            #need a pretty error printing class
            raise Exception("Row:{1} Col:{2} Variable \"{3}\" accessed before declaration.".format('{0}', self.Loc[0], self.Loc[2], self.Name))


class PrimaryExpression(Node):
    def __init__(self, Type, Child, Loc=None):
        self.Type = Type
        self.Child = Child
        self.Loc = Loc

    def GetChildren(self):
        Children = []
        Children.append(Child)
        return Children

    def RunSemanticAnalysis(self):
        pass


class PostfixExpression(Node):
    def __init__(self, Loc=None):
        pass

    def GetChildren(self):
        Children = []
        return Children

    #we cannot increment a constant
    def RunSemanticAnalysis(self):
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
