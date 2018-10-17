from Parser_M import Parser


def driver():
    s = ""
    P = Parser(SourceFile="Source.c")
    P.BuildParser()

    with open("Source.c") as file:
        s = file.read()

    result = P.Parser.parse(s)
    print(result)


driver()
