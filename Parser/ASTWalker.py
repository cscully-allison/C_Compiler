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

    def PrintASTHelper(self, Root):
        self.TreeGraphOutPtr.write("from anytree import Node, RenderTree \n")


        if Root is not None and self.IsNode(Root):
            self.TreeGraphOutPtr.write(Root.BuildTreeOutput(None) + '\n')

            if Root.GetChildren() is not None:
                for SubTree in Root.GetChildren():
                    self.PrintAST(Root, SubTree)
        else:
            return

        self.TreeGraphOutPtr.write('''for pre, fill, node in RenderTree({}): print("%s%s" % (pre, node.name))'''.format(Root.__class__.__name__ + str(id(Root))))

    def PrintAST(self, Parent, Child):

        if Child is not None and self.IsNode(Child):
            self.TreeGraphOutPtr.write(Child.BuildTreeOutput(Parent.__class__.__name__ + str(id(Parent))) + '\n')

            if Child.GetChildren() is not None:
                for SubTree in Child.GetChildren():
                    self.PrintAST(Child, SubTree)
        else:

            return
