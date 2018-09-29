import sys
sys.path.append("SymbolTable/")
from SymbolTable import SymbolTable
from LexicalAnalizer import LexicalAnalizer

def test_constructor():
    ST = SymbolTable()
    LA = LexicalAnalizer(ST)

def test_tokenizing():
    #basic token test for identifier
    ST = SymbolTable()
    LA = LexicalAnalizer(ST)

    data = ''' var vary vars '''

    LA.Lexer.input(data)

    for Tok in LA.Lexer:
        assert(Tok.type == 'IDENTIFIER')
