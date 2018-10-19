import sys
sys.path.append("SymbolTable/")
from SymbolTable import SymbolTable
from LexicalAnalizer import LexicalAnalizer

def driver():
    #basic token test for identifier
    ST = SymbolTable()
    LA = LexicalAnalizer(ST)
    LA.BuildLexer()

    data = '''
    auto
    break
    case
    char
    const
    continue
    default
    do
    double
    else
    enum
    extern
    float
    for
    goto
    if
    int
    long
    register
    return
    short
    signed
    sizeof
    static
    struct
    switch
    typedef
    union
    unsigned
    void
    volatile
    while
    {}()[]!?/*^%&~$
    var 4382
    vary vars 42.26
    ___ ____
    43E-25 43e+25
    '\t' 'a' '\n' '\0' abl '"' '\'' '8'
    "In a little hole in the ground there lived a hobbit. 12345 ' ' \" \' and some other thing \0 \n \t"
    t'challa
    '''

    LA.Lexer.input(data)

    for Tok in LA.Lexer:
        print(Tok)

driver()
