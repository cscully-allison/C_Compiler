import re


def BuildProductionFunction(line, ProdTemplate, CurrentNonTerminal, ProdNumber):
    LineProdTemplate = "{0} : {1}"
    CurrentNonTerminal = re.sub(' |\n', '', CurrentNonTerminal)

    if line[0] == '%' or ";" in line:
        return
    elif len(line.strip()) == 0 :
        return
    elif ":" in line or "|" in line:
        return ProdTemplate.format(
            CurrentNonTerminal,
            ProdNumber,
            LineProdTemplate.format(
                CurrentNonTerminal,
                re.sub('\||:|\n|\t', '', line)
            ),
            CurrentNonTerminal,
            re.sub('\||:|\n|\t', '', line)
        )
    else:
        return



PClass = ''
PProdTemplate = ''
OneProduction = ''
AllProductions = ''

with open("ParserClassTemplate", 'r') as File:
    PClass = File.read()

with open("ProdFunctionTemplate", 'r') as File:
    PProdTemplate = File.read()


with open("C_grammar.y", 'r') as File:
    prior = ""
    CurrentNonTerminal = ""
    ProdNumber = 0

    line = File.readline()
    while line:
        if len(prior.strip()) == 0 and '%' not in line:
            CurrentNonTerminal = line
            ProdNumber = 0

        OneProduction = BuildProductionFunction(line, PProdTemplate, CurrentNonTerminal, ProdNumber)
        if OneProduction is not None:
            AllProductions += OneProduction + "\n"

        ProdNumber += 1
        prior = line
        line = File.readline()

PClass = PClass.format(AllProductions)
with open("G_Parser.py", 'w') as Out:
    Out.write(PClass)
