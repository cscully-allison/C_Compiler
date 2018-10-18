from Parser_M import Parser


def driver():
    s = ""
    P = Parser(SourceFile="Source.c")
    P.BuildParser()

    with open("Source.c") as file:
        s = file.read()
    try:
        result = P.Parser.parse(s)
    except Exception as e:
        print("[Compilation stopped]\nReason: {0}".format(e))
        return


driver()
