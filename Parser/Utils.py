def PrettyErrorPrint(Message, Lineno, Column, SourceText):
    arrow = ""
    i = 0

    #print line
    # with open(self.SourceFile) as file:
    #     for i in range(0,Lineno):
    #         source = file.readline()
    # print(source)
    lines = SourceText.splitlines()

    for i, line in enumerate(lines):
        if i is Lineno-1:
            source = line

    #build arrow
    for i in range(0,Column-1):
        arrow += " "
    arrow += "^\n"


    return Message + '\n' + source + '\n' + arrow + '\n'
