from Globals import ErrManager, ST_G
from Parser_M import Parser
from ASTWalker import ASTWalker, CodeGenerator
from AssemblyGenerator import AssemblyGenerator
import sys

def driver():

    s = ""
    SourceCodeFile = ""

    #find input file
    for i, arg in enumerate(sys.argv):
        if arg == "-i":
            SourceCodeFile = sys.argv[i+1]

    ST_G.SourceFile = SourceCodeFile


    # Construct parser
    P = Parser(SourceFile=SourceCodeFile, DebugArgs = sys.argv)
    P.BuildParser()

    # AST = P.RunParser()

    # Run parser in try except block to enable compliation
    # terminiation under various circumstances
    try:
        AST = P.RunParser()
        if ErrManager.HasErrors():
            raise Exception()
    except Exception as e:
        print(e)
        print("\n[Compliation Stopped]\nThe Following Errors Were Found:\n")
        ErrManager.PrintErrors()
        return

    ST_G.ClearSymbolTable()

    AW = ASTWalker(AST)
    AW.PrintASTHelper(AW.AST)

    ICG = CodeGenerator(AST, "intermediate.3AC")

    ICG.PrettyPrint3AC()

    Assembly = AssemblyGenerator(ThreeAC = ICG.Output)


driver()
