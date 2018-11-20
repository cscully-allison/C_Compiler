import json
from Globals import CM, ST_G
from Utils import GetBytesFromId



class CodeGenerator(object):
    def __init__(self, AST, File):
        self.AST = AST
        self.File = File
        self.Output = []
        self.Ouput3AC(AST)

    def IsNode(self, Node):
        for base in Node.__class__.__bases__:
            if base.__name__ is 'Node':
                return True
        return False

    def IsNodeType(self, Node, Name):
        if self.IsNode(Node):
            if Node.__class__.__name__ == Name:
                return True
        return False

    def IsIdentifier(self, Node):
        for base in Node.__class__.__bases__:
            if base.__name__ is 'Identifier':
                return True
        return False

    def IsPassUpNode(self, Node):
        if Node.__class__.__name__ == 'PassUpNode':
            return True;
        return False;

    def Load3AC(self, Instruction = None, Dest = None, OperandA = None, OperandB = None, LineNo = None):
        self.Output.append({'Instruction': Instruction, 'Dest': Dest, 'OpA': OperandA, 'OpB': OperandB, 'LineNo': LineNo})


    def Declaration(self, DeclNode):
        # add declaration to symbol table
        for ID in DeclNode.ID:
            ID['Size In Bytes'] = GetBytesFromId(ID, CM.TypeToBytes(ID['Type']))
            ID['Local Offset'] = ST_G.CalcLocalOffset()
            ST_G.InsertSymbol(ID['Label'], ID)


        return DeclNode.Bytes

    def GetStackFrameSize(self, CompoundStatement):
        if CompoundStatement is None: return 0
        if not self.IsNode(CompoundStatement): return 0
        if CompoundStatement.GetChildren() is None: return 0

        RunningSize = 0

        for Child in CompoundStatement.GetChildren():
            if self.IsNodeType(Child, 'CompoundStatement'):
                RunningSize += self.GetStackFrameSize(Child)
            elif self.IsNodeType(Child, 'Declaration'):
                RunningSize += self.Declaration(Child)
            else:
                RunningSize += self.GetStackFrameSize(Child)

        return RunningSize

    def FunctionDefintion(self, FunctSubtree):
        StackFrameSize = 0
        ArgsSize = 0

        # push a new scope on
        ST_G.PushNewScope()

        # add stack frame size from Arguments
        for Arg in FunctSubtree.FunctionArguments:

            Arg['Size In Bytes'] = GetBytesFromId(Arg, CM.TypeToBytes(Arg['Type']))
            Arg['Local Offset'] = ST_G.CalcLocalOffset()
            ST_G.InsertSymbol(Arg['Label'], Arg)

            ArgsSize += Arg['Size In Bytes']

        # fetch stack frame size from locals
        for Child in FunctSubtree.GetChildren():
            if self.IsNodeType(Child, 'CompoundStatement'):
                StackFrameSize = self.GetStackFrameSize(Child)


        # Loading label, argsize in bytes, and StackFrameSize in bytes
        self.Load3AC(Instruction = "PROCENTRY", Dest=FunctSubtree.IDPtr['Label'], OperandA = StackFrameSize, OperandB = ArgsSize)


        ST_G.WriteSymbolTableToFile("walkerst.out")

        #recursively call Output 3AC on CompoundStatement to maintain correct scoping in ST

        #pop scope


    def Ouput3AC(self, Subtree):
        # Base Case
        if Subtree is None: return
        if not self.IsNode(Subtree): return
        if Subtree.GetChildren() is None: return

        #Pass Up Node
        if self.IsPassUpNode(Subtree):
            for Child in Subtree.GetChildren():
                self.Ouput3AC(Child)
        elif self.IsNodeType(Subtree, 'FunctionDefintion'):
            self.FunctionDefintion(Subtree)
        else:
            for Child in Subtree.GetChildren():
                self.Ouput3AC(Child)




class ASTWalker(object):
    def __init__(self, AST, TreeGraphOut = "TreeGraph.out.py"):
        self.AST = AST
        self.TreeGraphOut = "TreeGraph.out.py"
        self.TreeGraphOutPtr = open(self.TreeGraphOut, "w")

    def IsNode(self, Node):
        for base in Node.__class__.__bases__:
            if base.__name__ is 'Node':
                return True
        return False

    def IsIdentifier(self, Node):
        for base in Node.__class__.__bases__:
            if base.__name__ is 'Identifier':
                return True
        return False



    def PrintASTHelper(self, Root):
        self.TreeGraphOutPtr.write("from anytree import Node, RenderTree \n")
        self.TreeGraphOutPtr.write("from anytree.exporter import DotExporter\n")


        if Root is not None and self.IsNode(Root):
            self.TreeGraphOutPtr.write(Root.BuildTreeOutput(None) + '\n')

            if Root.GetChildren() is not None:
                for SubTree in Root.GetChildren():
                    self.PrintAST(Root, SubTree)
        else:
            return

        # Write out trailing functions
        self.TreeGraphOutPtr.write('''
for pre, fill, node in RenderTree({}):
    if "TokenLocation" in node.name: print("%s%s" % (pre, node.name))
    else: print("%s%s" % (pre, node.name[:-5]) )\n
    '''.format(Root.__class__.__name__ + str(id(Root))))

        self.TreeGraphOutPtr.write('''
def f(node):
    if node.is_leaf and "TokenLocation" in node.name:
        return 'label="%s"' % (node.name)
    return 'label="%s"' % (node.name[:-5])

DotExporter({}, nodeattrfunc=f).to_picture("AST.png")
        '''.format(Root.__class__.__name__ + str(id(Root))))


    def PrintAST(self, Parent, Child):
        ''' This function is called where the child is our current node. Parent was the callee.
        '''
        #base check
        if Child is not None and Child is not False:
            if self.IsNode(Child):
                self.TreeGraphOutPtr.write(Child.BuildTreeOutput(Parent.__class__.__name__ + str(id(Parent))) + '\n')

                #recursive call
                if Child.GetChildren() is not None:
                    for SubTree in Child.GetChildren():
                        self.PrintAST(Child, SubTree)

            # check if child is a dictonary
            elif type(Child) is type({}):
                output = '{} = Node(\"{}\"{})'
                output = output.format("leaf", ', '.join("{!s}={!r}".format(key,val) for (key,val) in Child.items()), ", parent=" +Parent.__class__.__name__ + str(id(Parent)))
                self.TreeGraphOutPtr.write(output + '\n')

            elif type(Child) is type([]):
                    DataType = ''
                    for SubC in Child:
                        DataType += SubC + " "

                    output = '{} = Node(\'{}\'{})'
                    output = output.format("leaf", DataType + "_" + str(id(Parent))[-4:], ", parent=" +Parent.__class__.__name__ + str(id(Parent)))
                    self.TreeGraphOutPtr.write(output + '\n')

            else:
                output = '{} = Node(\"{}\"{})'
                output = output.format("leaf", Child + "_" + str(id(Parent))[-4:], ", parent=" +Parent.__class__.__name__ + str(id(Parent)))
                self.TreeGraphOutPtr.write(output + '\n')

        else:
            return
