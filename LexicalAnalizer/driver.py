import sys
sys.path.append("SymbolTable/")
from SymbolTable import SymbolTable
from LexicalAnalizer import LexicalAnalizer

def driver():
    #basic token test for identifier
    ST = SymbolTable()
    LA = LexicalAnalizer(ST)

    data = '''
    int var
    vary vars 
    '''

    LA.Lexer.input(data)

    for Tok in LA.Lexer:
        print(Tok)

driver()
