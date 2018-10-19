import ply.lex as lex

class LexicalAnalizer():

    def __init__(self, SymbolTable, DebugSwitch = None, Output = None, SourceFile = None, DebugArgs = []):
        self.ST = SymbolTable
        self.SourceFile = SourceFile
        self.DebugLex = False
        for args in DebugArgs:
            if args == '-l':
                self.DebugLex = True
                print "lex debug on"
        self.OutputFile = None
        self.Lexer = None
        self.ST.DebugMode = False
        for args in DebugArgs:
            if args == '-s':
                self.ST.DebugMode = True
                print "symbol table debug on"

        for args in DebugArgs:
            if args == '-o':
                self.OutputFile = Output
                print "output flag on"

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
            'SINGLE_LINE_COMMENT',
            'VARYING_COMMENT',

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
            'ASTERISK',
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
            'QMARK',
            'PERIOD',

            'PD_O',     #parser debug on
            'PD_F',     #parser debug off
            'LD_O',     #lexer debug on
            'LD_F',     #lexer debug off
            'ST2_O',    #symbol table debug on
            'ST2_F',    #symbol table debug off
            'DST'       #dump symbol table
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

        


    #niave implementation, we may move this around a bit
    #(see PLY documentation 4.15)
    def BuildLexer(self):

        #tokens
        tokens = self.Tokens

        #regular expression rules
        #see PLY DOC 4.3 for ordering problems

        PTR_OP   = r'->'
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
        t_ASTERISK   = r'\*'
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
        t_QMARK = r'\?'
        t_PERIOD = r'\.'

        def t_FLOATING_CONSTANT(t):
            r'[+-]?\d+((\.\d+){1}|([eE][+-]?\d+){1})'
            return t

        def t_INTEGER_CONSTANT(t):
            r'[+-]?[0-9]+'
            return t

        def t_CHARACTER_CONSTANT(t):
            r'\'[\D\d\n]\''
            return t

        def t_STRING_LITERAL(t):
            r'\"[\D\n\d]*\"'
            return t

        def t_SINGLE_LINE_COMMENT(t):
            r'(//.*)'
            pass

        def t_VARYING_COMMENT(t):
            r'(/\*(.|\n)*?\*/)'
            t.lexer.lineno += t.value.count('\n')
            if self.DebugLex == True:
                print(t)
            pass

        # t_ENUMERATION_CONSTANT   = r''

        def t_IDENTIFIER(t):
            r'[a-zA-Z_][a-zA-Z0-9_]*' #yes all underscores is a valid name
            t.type = self.Reserved.get(t.value,'IDENTIFIER')
            if t.type == 'IDENTIFIER':
                if len(str(t.value)) > 31:
                    print "Warning: Identifier exceeds maximum length"
                contents = {}
                if self.SourceFile is not None:
                    with open(self.SourceFile) as file:
                        source = file.read()
                        Column = self.FindColumn(source, t)
                contents["TokenLocation"] = (t.lineno, t.lexpos, Column)
                t.value = {"lexeme": t.value, "additional": contents}
                # self.ST.InsertSymbol(t.value, contents)

            if self.DebugLex == True:
                print(t)

            return t


        # Define a rule so we can track line numbers
        def t_newline(t):
            r'\n+'
            t.lexer.lineno += len(t.value)

        # A string containing ignored characters (spaces and tabs)
        t_ignore  = ' \t'

        # Error handling rule
        def t_error(t):
            source = ""
            Column = 0

            if self.SourceFile is not None:
                with open(self.SourceFile) as file:
                    source = file.read()
                    Column = self.FindColumn(source, t)

            self.PrettyErrorPrint(self.SourceFile, t.lineno, Column)

            t.lexer.skip(1)



        #dbug Output tokens
        def t_ST2_O(t):
            r'\$!ST2O'
            self.ST.ToggleDebugMode()

        def t_ST2_F(t):
            r'\$!ST2F'
            self.ST.ToggleDebugMode()

        def t_LD_O(t):
            r'\$!LDO'
            self.DebugLex = True

        def t_LD_F(t):
            r'\$!LDF'
            self.DebugLex = False


        def t_DST(t):
            r'\$!ST1'
            self.ST.WriteSymbolTableToFile("SymbolTable.out")

        def t_PD_O(t):
            r'\$!PDO'
            return t

        def t_PD_F(t):
            r'\$!PDF'
            return t

        #build Lexer
        self.Lexer = lex.lex()

    # Compute column.
    #     input is the input text string
    #     token is a token instance
    def FindColumn(self, input, token):
        line_start = input.rfind('\n', 0, token.lexpos) + 1
        return (token.lexpos - line_start) + 1

    def PrettyErrorPrint(self, Source, Lineno, Column):
        arrow = ""

        print("\nInvalid token on line {}\n".format(Lineno))
        #print line
        with open(self.SourceFile) as file:
            for i in range(0,Lineno):
                source = file.readline()
        print(source)

        #build arrow
        for i in range(0,Column-1):
            arrow += "-"
        arrow += "^\n"

        print(arrow)
