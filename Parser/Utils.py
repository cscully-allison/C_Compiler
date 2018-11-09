def PrettyErrorPrint(Message, Lineno, Column, SourceText):
    arrow = ""
    preface = "Error: Line:{} Column:{} ".format(Lineno, Column)

    lines = SourceText.splitlines()

    for i, line in enumerate(lines):
        if i is Lineno-1:
            source = line

    #build arrow
    for i in range(0,Column-1):
        arrow += " "
    arrow += "^\n"


    return preface + Message + '\n' + source + '\n' + arrow + '\n'

def FunctPrettyErrorPrint(Message, Lineno, Column, SourceText):
    arrow = ""
    postface = "On Line:{} Column:{} ".format(Lineno, Column)

    lines = SourceText.splitlines()

    for i, line in enumerate(lines):
        if i is Lineno-1:
            source = line

    #build arrow
    for i in range(0,Column-1):
        arrow += " "
    arrow += "^\n"


    return  Message + '\n' + postface + '\n\n' + source + '\n' + arrow + '\n'


def FindColumn(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

def IsNode(Node):
    for base in Node.__class__.__bases__:
        if base.__name__ is 'Node':
            return True
    return False

def GetLoc(production):
    return (production.lexer.lineno, production.lexer.lexpos, FindColumn(production.lexer.lexdata, production.lexer) )

def BuildArrayString(DataType, SizeArr):
    string = ''
    sizes = ''

    for type in DataType:
        string += type + ' '

    for size in SizeArr:
        sizes += '[' + size + ']'

    string += sizes

    return string
