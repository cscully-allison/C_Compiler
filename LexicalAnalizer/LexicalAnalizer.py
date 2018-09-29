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
            'EQUALS',
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

        self.BuildLexer()

    def BuildLexer(self):

        #tokens
        tokens = self.Tokens

        #regular expression rules
        t_IDENTIFIER  = r'[a-z|A-Z][a-zA-Z0-9\_]*'
        # INTEGER_CONSTANT   = r''
        # FLOATING_CONSTANT   = r''
        # CHARACTER_CONSTANT   = r''
        # ENUMERATION_CONSTANT   = r''
        # STRING_LITERAL   = r''
        # SIZEOF   = r''
        # PTR_OP   = r''
        # INC_OP   = r''
        # DEC_OP   = r''
        # LEFT_OP   = r''
        # RIGHT_OP   = r''
        # LE_OP   = r''
        # GE_OP   = r''
        # EQ_OP   = r''
        # NE_OP   = r''
        # AND_OP   = r''
        # OR_OP   = r''
        # MUL_ASSIGN   = r''
        # DIV_ASSIGN   = r''
        # MOD_ASSIGN   = r''
        # ADD_ASSIGN   = r''
        # SUB_ASSIGN   = r''
        # LEFT_ASSIGN   = r''
        # RIGHT_ASSIGN   = r''
        # AND_ASSIGN   = r''
        # XOR_ASSIGN   = r''
        # OR_ASSIGN   = r''
        #
        # TYPEDEF_NAME   = r''
        # TYPEDEF   = r''
        # EXTERN   = r''
        # STATIC   = r''
        # AUTO   = r''
        # REGISTER   = r''
        # CHAR   = r''
        # SHORT   = r''
        # INT   = r''
        # LONG   = r''
        # SIGNED   = r''
        # UNSIGNED   = r''
        # FLOAT   = r''
        # DOUBLE   = r''
        # CONST   = r''
        # VOLATILE   = r''
        # VOID   = r''
        # STRUCT   = r''
        # UNION   = r''
        # ENUM   = r''
        # ELIPSIS   = r''
        # RANGE   = r''
        #
        # CASE   = r''
        # DEFAULT   = r''
        # IF   = r''
        # ELSE   = r''
        # SWITCH   = r''
        # WHILE   = r''
        # DO   = r''
        # FOR   = r''
        # GOTO   = r''
        # CONTINUE   = r''
        # BREAK   = r''
        # RETURN   = r''
        #
        # #we need string literal Tokens
        # SEMI   = r''
        # OPENBRACE   = r''
        # CLOSEBRACE   = r''
        # COMMA   = r''
        # EQUALS   = r''
        # COLON   = r''
        # OPENBRACKET   = r''
        # CLOSEBRACKET   = r''
        # OPENPAREN   = r''
        # CLOSEPAREN   = r''
        # MULT   = r''
        # PIPE   = r''
        # CARAT   = r''
        # AMPERSAND   = r''
        # LE   = r''
        # GT   = r''
        # PLUS   = r''
        # MINUS   = r''
        # DIV   = r''
        # PERCENT   = r''
        # TILDE   = r''
        # BANG  = r''
        # PERIOD = r''

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
