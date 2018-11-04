import json

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

            elif type(Child) is type([]) and Parent.__class__.__name__ is 'CastNode':
                    DataType = ''
                    for SubC in Child:
                        DataType += SubC + " "

                    output = '{} = Node(\'{}\'{})'
                    output = output.format("leaf", DataType + "_" + str(id(Parent))[-4:], ", parent=" +Parent.__class__.__name__ + str(id(Parent)))
                    self.TreeGraphOutPtr.write(output + '\n')

            else:
                output = '{} = Node(\'{}\'{})'
                output = output.format("leaf", Child + "_" + str(id(Parent))[-4:], ", parent=" +Parent.__class__.__name__ + str(id(Parent)))
                self.TreeGraphOutPtr.write(output + '\n')

        else:
            return
