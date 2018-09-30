import ply.lex as lex

class LexicalAnalizer():
    def __init__(self, SymbolTable, DebugSwitch = None, Output = None):
        self.ST = SymbolTable
        self.DebugLex = False
        self.OutputFile = None
        self.Lexer = None
        self.Tokens = (
            'IDENTIFIER',
            'INTEGER_CONSTANT',
            'FLOATING_CONSTANT',
            'CHARACTER_CONSTANT',
            'ENUMERATION_CONSTANT',
            'STRING_LITERAL',
            'SIZEOF',
            'PTR_OP',
            'INC_OP',
            'DEC_OP',
            'LEFT_OP',
            'RIGHT_OP',
            'LE_OP',
            'GE_OP',
            'EQ_OP',
            'NE_OP',
            'AND_OP',
            'OR_OP',
            'MUL_ASSIGN',
            'DIV_ASSIGN',
            'MOD_ASSIGN',
            'ADD_ASSIGN',
            'SUB_ASSIGN',
            'LEFT_ASSIGN',
            'RIGHT_ASSIGN',
            'AND_ASSIGN',
            'XOR_ASSIGN',
            'OR_ASSIGN',

            'TYPEDEF_NAME',
            'TYPEDEF',
            'EXTERN',
            'STATIC',
            'AUTO',
            'REGISTER',
            'CHAR',
            'SHORT',
            'INT',
            'LONG',
            'SIGNED',
            'UNSIGNED',
            'FLOAT',
            'DOUBLE',
            'CONST',
            'VOLATILE',
            'VOID',
            'STRUCT',
            'UNION',
            'ENUM',
            'ELIPSIS',
            'RANGE',

            'CASE',
            'DEFAULT',
            'IF',
            'ELSE',
            'SWITCH',
            'WHILE',
            'DO',
            'FOR',
            'GOTO',
            'CONTINUE',
            'BREAK',
            'RETURN',

            #we need string literal Tokens
            'SEMI',
            'OPENBRACE',
            'CLOSEBRACE',
            'COMMA',
            'ASSIGN',
            'COLON',
            'OPENBRACKET',
            'CLOSEBRACKET',
            'OPENPAREN',
            'CLOSEPAREN',
            'MULT',
            'PIPE',
            'CARAT',
            'AMPERSAND',
            'LE',
            'GT',
            'PLUS',
            'MINUS',
            'DIV',
            'PERCENT',
            'TILDE',
            'BANG',
            'PERIOD'

        )

        if DebugSwitch and "l" in DebugSwitch:
            self.DebugLex = True
        if DebugSwitch and "s" in DebugSwitch:
            self.ST.DebugMode = True

        if Output:
            self.OutputFile = Output

    #niave implementation, we may move this around a bit
    #(see PLY documentation 4.15)
    def BuildLexer(self):

        #tokens
        tokens = self.Tokens

        #regular expression rules
        #see PLY DOC 4.3 for ordering problems

        t_FLOATING_CONSTANT   = r'[+-]?[0-9]+(\.[0-9]+)?(E[+-]?[0-9])?'
        t_INTEGER_CONSTANT   = r'[+-]?[0-9]+'
        # t_CHARACTER_CONSTANT   = r''
        # ENUMERATION_CONSTANT   = r''
        # STRING_LITERAL   = r''

        # PTR_OP   = r''
        INC_OP   = r'\+\+'
        DEC_OP   = r'--'
        LEFT_OP   = r'<<'
        RIGHT_OP   = r'>>'
        LE_OP   = r'<='
        GE_OP   = r'>='
        EQ_OP   = r'=='
        NE_OP   = r'\!='
        AND_OP   = r'&&'
        OR_OP   = r'\|\|'
        MUL_ASSIGN   = r'\*='
        DIV_ASSIGN   = r'/='
        MOD_ASSIGN   = r'%='
        ADD_ASSIGN   = r'\+='
        SUB_ASSIGN   = r'-='
        LEFT_ASSIGN   = r'<<='
        RIGHT_ASSIGN   = r'>>='
        AND_ASSIGN   = r'&='
        XOR_ASSIGN   = r'\^='
        OR_ASSIGN   = r'\|='

        #we are changing the structure of reserved words
        SIZEOF   = r'sizeof'
        TYPEDEF_NAME   = r''
        TYPEDEF   = r'typedef'
        EXTERN   = r'extern'
        STATIC   = r'static'
        AUTO   = r'auto'
        REGISTER   = r'register'
        CHAR   = r'char'
        SHORT   = r'short'
        INT   = r'int'
        LONG   = r'long'
        SIGNED   = r'signed'
        UNSIGNED   = r'unsigned'
        FLOAT   = r'float'
        DOUBLE   = r'double'
        CONST   = r'const'
        VOLATILE   = r'volatile'
        VOID   = r'void'
        STRUCT   = r'struct'
        UNION   = r'union'
        ENUM   = r'enum'
        ELIPSIS   = r'\.\.\.'
        RANGE   = r' \.\.\. '

        CASE   = r'case'
        DEFAULT   = r'default'
        IF   = r'if'
        ELSE   = r'else'
        SWITCH   = r'switch'
        WHILE   = r'while'
        DO   = r'do'
        FOR   = r'for'
        GOTO   = r'goto'
        CONTINUE   = r'continue'
        BREAK   = r'break'
        RETURN   = r'return'

        # #we need string literal Tokens
        SEMI   = r';'
        OPENBRACE   = r'{'
        CLOSEBRACE   = r'}'
        COMMA   = r','
        ASSIGN   = r'='
        COLON   = r':'
        OPENBRACKET   = r'\['
        CLOSEBRACKET   = r'\]'
        OPENPAREN   = r'\('
        CLOSEPAREN   = r'\)'
        MULT   = r'\*'
        PIPE   = r'\|'
        CARAT   = r'\^'
        AMPERSAND   = r'&'
        LE   = r'<'
        GT   = r'>'
        PLUS   = r'\+'
        MINUS   = r'-'
        DIV   = r'/'
        PERCENT   = r'%'
        TILDE   = r'~'
        BANG  = r'\!'
        PERIOD = r'\.'


        t_IDENTIFIER  = r'[a-z|A-Z][a-zA-Z0-9\_]*'

        #rules

        # Define a rule so we can track line numbers
        def t_newline(t):
            r'\n+'
            t.lexer.lineno += len(t.value)

        # A string containing ignored characters (spaces and tabs)
        t_ignore  = ' \t'

        # Error handling rule
        def t_error(t):
            print("Illegal character '%s'" % t.value[0])
            t.lexer.skip(1)

        self.Lexer = lex.lex()
