from Parser_M import Parser
import sys

def driver():

    s = ""
    P = Parser(SourceFile="Source.c", DebugArgs = sys.argv)
    P.BuildParser()

    try:
        with open("Source.c") as file:
            s = file.read()
        result = P.Parser.parse(s)

    except Exception as e:
        print("[Compilation stopped]\nReason: {0}".format(e))
        return


driver()
