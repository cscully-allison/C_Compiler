import sys
sys.path.append("SymbolTable/")
from SymbolTable import SymbolTable
from LexicalAnalizer import LexicalAnalizer

def test_constructor():
    ST = SymbolTable("")
    LA = LexicalAnalizer(ST)

def test_reservedWords():
    #basic token test for identifier
    ST = SymbolTable("")
    LA = LexicalAnalizer(ST)
    LA.BuildLexer()

    data = '''int'''

    LA.Lexer.input(data)

    for Tok in LA.Lexer:
        assert(Tok.type == 'INT')

    data = '''goto'''

    LA.Lexer.input(data)

    for Tok in LA.Lexer:
        assert(Tok.type == 'GOTO')

    data = '''continue'''

    LA.Lexer.input(data)

    for Tok in LA.Lexer:
        assert(Tok.type == 'CONTINUE')

    data = '''struct'''

    LA.Lexer.input(data)

    for Tok in LA.Lexer:
        assert(Tok.type == 'STRUCT')

    data = '''volatile'''

    LA.Lexer.input(data)

    for Tok in LA.Lexer:
        assert(Tok.type == 'VOLATILE')

    data = '''typedef'''

    LA.Lexer.input(data)

    for Tok in LA.Lexer:
        assert(Tok.type == 'TYPEDEF')

def test_literals():
    #basic token test for character literals
    ST = SymbolTable("")
    LA = LexicalAnalizer(ST)
    LA.BuildLexer()

    data = '''='''

    LA.Lexer.input(data)

    for Tok in LA.Lexer:
        assert(Tok.type == 'ASSIGN')
    
    data = '''>='''

    LA.Lexer.input(data)

    for Tok in LA.Lexer:
        assert(Tok.type == 'GE_OP')

    data = '''*'''

    LA.Lexer.input(data)

    for Tok in LA.Lexer:
        assert(Tok.type == 'ASTERISK')

    data = '''!'''

    LA.Lexer.input(data)

    for Tok in LA.Lexer:
        assert(Tok.type == 'BANG')

def test_constants():
    #basic token test for constants
    ST = SymbolTable("")
    LA = LexicalAnalizer(ST)
    LA.BuildLexer()

    data = '''\'a\''''

    LA.Lexer.input(data)

    for Tok in LA.Lexer:
        assert(Tok.type == 'CHARACTER_CONSTANT')

    data = '''//words'''

    LA.Lexer.input(data)

    for Tok in LA.Lexer:
        assert(Tok.type == 'SINGLE_LINE_COMMENT')   

    data = '''-456.89'''

    LA.Lexer.input(data)

    for Tok in LA.Lexer:
        assert(Tok.type == 'FLOATING_CONSTANT')   

    data = '''\"this is string\"'''

    LA.Lexer.input(data)

    for Tok in LA.Lexer:
        assert(Tok.type == 'STRING_LITERAL')       