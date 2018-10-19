from Parser_M import Parser
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
        with open(SourceCodeFile) as file:
            s = file.read()
        result = P.Parser.parse(s)

    except Exception as e:
        print("[Compilation stopped]\nReason: {0}".format(e))
        return


driver()
