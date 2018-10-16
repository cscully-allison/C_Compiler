from G_Parser import Parser


def driver():
    s = ""
    P = Parser()
    P.BuildParser()

    with open("Source.c") as file:
        s = file.read()

    result = P.Parser.parse(s)
    print(result)


driver()
