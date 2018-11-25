def SafeCheckDict(Dict, Key, Content = None):
    if Dict is None:
        return False
    if Content is not None:
        if Key in Dict and Dict[Key] == Content:
            return True
        return False
    elif Key in Dict:
        return True

    return False

def GetBytesFromId(ID, DTCBytes):
    Bytes = 0
    TotalSize = 1
    if 'Subtype' in ID and ID['Subtype'] is 'Array':
        for Size in ID['Array Size']:
            TotalSize *= int(Size)
        Bytes += TotalSize * DTCBytes
    else:
        Bytes += DTCBytes

    return Bytes

def GetBytesFromIds(IDs, DTCBytes):
    Bytes = 0
    for ID in IDs:
        TotalSize = 1
        if 'Subtype' in ID and ID['Subtype'] is 'Array':
            for Size in ID['Array Size']:
                TotalSize *= int(Size)
            Bytes += TotalSize * DTCBytes
        else:
            Bytes += DTCBytes

    return Bytes

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


def CalcConversionFactor(DT):
    '''DataType conversion hierarchy from wikipedia C_data_types'''
    '''ConversionFactor: a lower value is higher in the heierachy and coerces to it'''
    DTCH = [
    [ ['long double'] ],
    [ ['double'] ],
    [ ['float'] ],
    [ ['unsigned', 'long', 'long'], ['unsigned', 'long', 'long', 'int']],
    [ ['long', 'long'], ['long','long', 'int'], ['signed', 'long', 'long'], ['signed', 'long', 'long', 'int'] ],
    [ ['unsigned', 'long'], ['unsigned', 'long', 'int'] ],
    [ ['long'], ['long', 'int'], ['signed', 'long'], ['signed', 'long', 'int'] ],
    [ ['unsigned'], ['unsigned', 'int'] ],
    [ ['int'], ['signed'], ['signed', 'int'] ],
    [ ['unsigned', 'short'], ['unsigned', 'short', 'int'] ],
    [ ['short'], ['short', 'int'], ['signed', 'short'], ['signed', 'short', 'int'] ],
    [ ['unsigned', 'char'] ],
    [ ['signed', 'char'] ],
    [ ['char'] ]
    ]

    ConversionFactor = 0

    for i, Tier in enumerate(DTCH):
        for DTCombo in Tier:
            if DT == DTCombo:
                ConversionFactor = i

    return ConversionFactor
