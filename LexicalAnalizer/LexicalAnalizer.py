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
        self.Reserved = {
            'if':'IF',
            'auto': 'AUTO',
            'break': 'BREAK',
            'case': 'CASE',
            'char': 'CHAR',
            'const': 'CONST',
            'continue': 'CONTINUE',
            'default': 'DEFAULT',
            'do': 'DO',
            'double': 'DOUBLE',
            'else': 'ELSE',
            'enum': 'ENUM',
            'extern': 'EXTERN',
            'float': 'FLOAT',
            'for': 'FOR',
            'goto': 'GOTO', #THE FORBIDDEN WORD
            'int': 'INT',
            'long': 'LONG',
            'register': 'REGISTER',
            'return': 'RETURN',
            'short': 'SHORT',
            'signed': 'SIGNED',
            'sizeof': 'SIZEOF',
            'static': 'STATIC',
            'struct': 'STRUCT',
            'switch': 'SWITCH',
            'typedef': 'TYPEDEF',
            'union': 'UNION',
            'unsigned': 'UNSIGNED',
            'void': 'VOID',
            'volatile': 'VOLATILE',
            'while': 'WHILE'
         }

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

        t_FLOATING_CONSTANT   = r'^[+-]?[0-9]+((\.[0-9]+)|(E[+-]?[0-9])){1}$'
        t_INTEGER_CONSTANT   = r'[+-]?[0-9]+'
        # t_CHARACTER_CONSTANT   = r''
        # ENUMERATION_CONSTANT   = r''
        # STRING_LITERAL   = r''

        # PTR_OP   = r''
        t_INC_OP   = r'\+\+'
        t_DEC_OP   = r'--'
        t_LEFT_OP   = r'<<'
        t_RIGHT_OP   = r'>>'
        t_LE_OP   = r'<='
        t_GE_OP   = r'>='
        t_EQ_OP   = r'=='
        t_NE_OP   = r'\!='
        t_AND_OP   = r'&&'
        t_OR_OP   = r'\|\|'
        t_MUL_ASSIGN   = r'\*='
        t_DIV_ASSIGN   = r'/='
        t_MOD_ASSIGN   = r'%='
        t_ADD_ASSIGN   = r'\+='
        t_SUB_ASSIGN   = r'-='
        t_LEFT_ASSIGN   = r'<<='
        t_RIGHT_ASSIGN   = r'>>='
        t_AND_ASSIGN   = r'&='
        t_XOR_ASSIGN   = r'\^='
        t_OR_ASSIGN   = r'\|='

        #we are changing the structure of reserved words

        # t_TYPEDEF_NAME   = r''
        t_ELIPSIS   = r'\.\.\.'
        t_RANGE   = r' \.\.\. '

        # #we need string literal Tokens
        t_SEMI   = r';'
        t_OPENBRACE   = r'{'
        t_CLOSEBRACE   = r'}'
        t_COMMA   = r','
        t_ASSIGN   = r'='
        t_COLON   = r':'
        t_OPENBRACKET   = r'\['
        t_CLOSEBRACKET   = r'\]'
        t_OPENPAREN   = r'\('
        t_CLOSEPAREN   = r'\)'
        t_MULT   = r'\*'
        t_PIPE   = r'\|'
        t_CARAT   = r'\^'
        t_AMPERSAND   = r'&'
        t_LE   = r'<'
        t_GT   = r'>'
        t_PLUS   = r'\+'
        t_MINUS   = r'-'
        t_DIV   = r'/'
        t_PERCENT   = r'%'
        t_TILDE   = r'~'
        t_BANG  = r'\!'
        t_PERIOD = r'\.'


        def t_IDENTIFIER(t):
            r'[a-z|A-Z][a-zA-Z0-9_]*'
            t.type = self.Reserved.get(t.value,'IDENTIFIER')
            return t


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
