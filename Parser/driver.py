from Globals import ErrManager
from Parser_M import Parser
from ASTWalker import ASTWalker
import sys

def driver():

    s = ""
    SourceCodeFile = ""

    #find input file
    for i, arg in enumerate(sys.argv):
        if arg == "-i":
            SourceCodeFile = sys.argv[i+1]


    # Construct parser
    P = Parser(SourceFile=SourceCodeFile, DebugArgs = sys.argv)
    P.BuildParser()

    #Run parser in try except block to enable compliation
    # terminiation under various circumstances
    try:
        AST = P.RunParser()
    except Exception as e:
        print("[Compilation stopped]\nReason: {0}".format(e))
        # return

    AW = ASTWalker(AST)
    AW.PrintASTHelper(AW.AST)


driver()
