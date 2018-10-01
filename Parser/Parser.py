OPENPARENimport sys
sys.path.append("/LexicalAnalizer")
from LexicalAnalizer import LexicalAnalizer

class Parser():

    def __init__(self):
        self.LA = LexicalAnalizer()

    #PLY Documentation http://www.dabeaz.com/ply/ply.html
    #Starting at 5
    def BuildParser():
        def p_Translation_Unit(p):
            '''translation_unit
        	: external_declaration
        	| translation_unit external_declaration
        	;'''
            return

        def p_External_Declaration(p):
            '''
            external_declaration
        	: function_definition
        	| declaration
        	;
            '''
            if self.DebugProd:
                print("nt -> prod")
            return

        def p_Function_Definition(p):   
            '''
            function_definition
        	: declarator compound_statement
        	| declarator declaration_list compound_statement
        	| declaration_specifiers declarator compound_statement
        	| declaration_specifiers declarator declaration_list compound_statement
        	;
            '''
        def p_Declaration(p):
            '''
            declaration
        	: declaration_specifiers SEMI
        	| declaration_specifiers init_declarator_list SEMI
        	;
            '''
        def p_Declaration_List(p):
            '''
            declaration_list
        	: declaration
        	| declaration_list declaration
        	;
            '''
        def p_Declartion_Specifiers(p):
            '''
            declaration_specifiers
        	: storage_class_specifier
        	| storage_class_specifier declaration_specifiers
        	| type_specifier
        	| type_specifier declaration_specifiers
        	| type_qualifier
        	| type_qualifier declaration_specifiers
        	;
            '''
        def p_Storage_Class_Specifier(p):
            '''
            storage_class_specifier
        	: AUTO
        	| REGISTER
        	| STATIC
        	| EXTERN
        	| TYPEDEF
        	;
            '''

        def p_Type_Specifier(p):
            '''
            type_specifier
        	: VOID
        	| CHAR
        	| SHORT
        	| INT
        	| LONG
        	| FLOAT
        	| DOUBLE
        	| SIGNED
        	| UNSIGNED
        	| struct_or_union_specifier
        	| enum_specifier
        	| TYPEDEF_NAME
        	;
            '''

        def p_Type_Qualifier(p):
            '''
            type_qualifier
        	: CONST
        	| VOLATILE
        	;
            '''

        def p_Struct_Or_Union_Specifier(p):
            '''
            struct_or_union_specifier
        	: struct_or_union identifier OPENBRACE struct_declaration_list CLOSEBRACE
        	| struct_or_union OPENBRACE struct_declaration_list CLOSEBRACE
        	| struct_or_union identifier
        	;
            '''

        def p_Struct_Or_Union(p):
            '''
            struct_or_union
        	: STRUCT
        	| UNION
        	;
            '''

        def p_Struct_Declaration_List(p):
            '''
            struct_declaration_list
        	: struct_declaration
        	| struct_declaration_list struct_declaration
        	;
            '''

        def p_Init_Declarator_List(p):
            '''
            init_declarator_list
        	: init_declarator
        	| init_declarator_list COMMA init_declarator
        	;
            '''

        def p_Init_Declarator(p):
            '''
            init_declarator
        	: declarator
        	| declarator ASSIGN initializer
        	;
            '''

        def p_Struct_Declaration(p):
            '''
            struct_declaration
        	: specifier_qualifier_list struct_declarator_list SEMI
        	;
            '''

        def p_Specifier_Qualifier_List(p):
            '''
            specifier_qualifier_list
        	: type_specifier
        	| type_specifier specifier_qualifier_list
        	| type_qualifier
        	| type_qualifier specifier_qualifier_list
        	;
            '''

        def p_Struct_Declarator_List(p):
            '''
            struct_declarator_list
        	: struct_declarator
        	| struct_declarator_list COMMA struct_declarator
        	;
            '''

        def p_Struct_Declarator(p):
            '''
            struct_declarator
        	: declarator
        	| COLON constant_expression
        	| declarator COLON constant_expression
        	;
            '''

        def p_Enum_Specifier(p):
            '''
            enum_specifier
        	: ENUM OPENBRACE enumerator_list CLOSEBRACE
        	| ENUM identifier OPENBRACE enumerator_list CLOSEBRACE
        	| ENUM identifier
        	;
            '''

        def p_Enumerator_List(p):
            '''
            enumerator_list
        	: enumerator
        	| enumerator_list COMMA enumerator
        	;
            '''

        def p_Enumerator(p):
            '''
            enumerator
        	: identifier
        	| identifier ASSIGN constant_expression
        	;
            '''

        def p_Declarator(p):
            '''
            declarator
        	: direct_declarator
        	| pointer direct_declarator
        	;
            '''

        def p_Direct_Declarator(p):
            '''
            direct_declarator
        	: identifier
        	| OPENPAREN declarator CLOSEPAREN
        	| direct_declarator OPENBRACKET CLOSEBRACKET
        	| direct_declarator OPENBRACKET constant_expression CLOSEBRACKET
        	| direct_declarator OPENPAREN CLOSEPAREN
        	| direct_declarator OPENPAREN parameter_type_list CLOSEPAREN
        	| direct_declarator OPENPAREN identifier_list CLOSEPAREN
        	;
            '''

        def p_Pointer(p):
            '''
            pointer
        	: ASTERISK
        	| ASTERISK type_qualifier_list
        	| ASTERISK pointer
        	| ASTERISK type_qualifier_list pointer
        	;
            '''

        def p_Type_Qualifier_List(p):
            '''
            type_qualifier_list
        	: type_qualifier
        	| type_qualifier_list type_qualifier
        	;
            '''

        def p_Parameter_Type_List(p):
            '''
            parameter_type_list
        	: parameter_list
        	| parameter_list COMMA ELIPSIS
        	;
            '''

        def p_Paramter_List(p):
            '''
            parameter_list
        	: parameter_declaration
        	| parameter_list COMMA parameter_declaration
        	;
            '''

        def p_Parameter_Declaration(p):
            '''
            parameter_declaration
        	: declaration_specifiers declarator
        	| declaration_specifiers
        	| declaration_specifiers abstract_declarator
        	;
            '''

        def p_Identifier_List(p):
            '''
            identifier_list
        	: identifier
        	| identifier_list COMMA identifier
        	;
            '''

        def p_Initializer(p):
            '''
            initializer
        	: assignment_expression
        	| OPENBRACE initializer_list CLOSEBRACE
        	| OPENBRACE initializer_list COMMA CLOSEBRACE
        	;
            '''

        def p_Initializer_List(p):
            '''
            initializer_list
        	: initializer
        	| initializer_list COMMA initializer
        	;
            '''

        def p_Type_Name(p):
            '''
            type_name
        	: specifier_qualifier_list
        	| specifier_qualifier_list abstract_declarator
        	;
            '''

        def p_Abstract_Declarator(p):
            '''
            abstract_declarator
        	: pointer
        	| direct_abstract_declarator
        	| pointer direct_abstract_declarator
        	;
            '''

        def p_Direct_Abstract_Declarator(p):
            '''
            direct_abstract_declarator
        	: OPENPAREN abstract_declarator CLOSEPAREN
        	| OPENBRACKET CLOSEBRACKET
        	| OPENBRACKET constant_expression CLOSEBRACKET
        	| direct_abstract_declarator OPENBRACKET CLOSEBRACKET
        	| direct_abstract_declarator OPENBRACKET constant_expression CLOSEBRACKET
        	| OPENPAREN CLOSEPAREN
        	| OPENPAREN parameter_type_list CLOSEPAREN
        	| direct_abstract_declarator OPENPAREN CLOSEPAREN
        	| direct_abstract_declarator OPENPAREN parameter_type_list CLOSEPAREN
        	;
            '''

        def p_Statement(p):
            '''
            statement
        	: labeled_statement
        	| compound_statement
        	| expression_statement
        	| selection_statement
        	| iteration_statement
        	| jump_statement
        	;
            '''

        def p_Labeled_Statement(p):
            '''
            labeled_statement
        	: identifier COLON statement
        	| CASE constant_expression COLON statement
        	| DEFAULT COLON statement
        	;
            '''

        def p_Expression_Statement(p):
            '''
            expression_statement
        	: SEMI
        	| expression SEMI
        	;
            '''

        def p_Compound_Statement(p):
            '''
            compound_statement
        	: OPENBRACE CLOSEBRACE
        	| OPENBRACE statement_list CLOSEBRACE
        	| OPENBRACE declaration_list CLOSEBRACE
        	| OPENBRACE declaration_list statement_list CLOSEBRACE
        	;
            '''

        def p_Statement_List(p):
            '''
            statement_list
        	: statement
        	| statement_list statement
        	;
            '''

        def p_Selection_Statement(p):
            '''
            selection_statement
        	: IF OPENPAREN expression CLOSEPAREN statement
        	| IF OPENPAREN expression CLOSEPAREN statement ELSE statement
        	| SWITCH OPENPAREN expression CLOSEPAREN statement
        	;
            '''

        def p_Iteration_Statement(p):
            '''
            iteration_statement
        	: WHILE OPENPAREN expression CLOSEPAREN statement
        	| DO statement WHILE OPENPAREN expression CLOSEPAREN SEMI
        	| FOR OPENPAREN SEMI SEMI CLOSEPAREN statement
        	| FOR OPENPAREN SEMI SEMI expression CLOSEPAREN statement
        	| FOR OPENPAREN SEMI expression SEMI CLOSEPAREN statement
        	| FOR OPENPAREN SEMI expression SEMI expression CLOSEPAREN statement
        	| FOR OPENPAREN expression SEMI SEMI CLOSEPAREN statement
        	| FOR OPENPAREN expression SEMI SEMI expression CLOSEPAREN statement
        	| FOR OPENPAREN expression SEMI expression SEMI CLOSEPAREN statement
        	| FOR OPENPAREN expression SEMI expression SEMI expression CLOSEPAREN statement
        	;
            '''

        def p_Jump_Statement(p):
            '''
            jump_statement
        	: GOTO identifier SEMI
        	| CONTINUE SEMI
        	| BREAK SEMI
        	| RETURN SEMI
        	| RETURN expression SEMI
        	;
            '''

        def p_Expression(p):
            '''
            expression
        	: assignment_expression
        	| expression COMMA assignment_expression
        	;
            '''

        def p_Assignment_Expression(p):
            '''
            assignment_expression
        	: conditional_expression
        	| unary_expression assignment_operator assignment_expression
        	;
            '''

        def p_Assignment_Operator(p):
            '''
            assignment_operator
        	: ASSIGN
        	| MUL_ASSIGN
        	| DIV_ASSIGN
        	| MOD_ASSIGN
        	| ADD_ASSIGN
        	| SUB_ASSIGN
        	| LEFT_ASSIGN
        	| RIGHT_ASSIGN
        	| AND_ASSIGN
        	| XOR_ASSIGN
        	| OR_ASSIGN
        	;
            '''

        def p_Conditional_Expression(p):
            '''
            conditional_expression
        	: logical_or_expression
        	| logical_or_expression QMARK expression COLON conditional_expression
        	;
            '''

        def p_Constant_Expression(p):
            '''
            constant_expression
        	: conditional_expression
        	;
            '''

        def p_Logical_Or_Expression(p):
            '''
            logical_or_expression
        	: logical_and_expression
        	| logical_or_expression OR_OP logical_and_expression
        	;
            '''

        def p_Logical_And_Expression(p):
            '''
            logical_and_expression
        	: inclusive_or_expression
        	| logical_and_expression AND_OP inclusive_or_expression
        	;
            '''

        def p_Inclusive_Or_Expression(p):
            '''
            inclusive_or_expression
        	: exclusive_or_expression
        	| inclusive_or_expression PIPE exclusive_or_expression
        	;
            '''

        def p_Exclusive_Or_Expression(p):
            '''
            exclusive_or_expression
        	: and_expression
        	| exclusive_or_expression CARAT and_expression
        	;
            '''

        def p_And_Expression(p):
            '''
            and_expression
        	: equality_expression
        	| and_expression AMPERSAND equality_expression
        	;
            '''

        def p_Equality_Expression(p):
            '''
            equality_expression
        	: relational_expression
        	| equality_expression EQ_OP relational_expression
        	| equality_expression NE_OP relational_expression
        	;
            '''

        def p_Relational_Expression(p):
            '''
            relational_expression
        	: shift_expression
        	| relational_expression LE shift_expression
        	| relational_expression GT shift_expression
        	| relational_expression LE_OP shift_expression
        	| relational_expression GE_OP shift_expression
        	;
            '''

        def p_Shift_Expression(p):
            '''
            shift_expression
        	: additive_expression
        	| shift_expression LEFT_OP additive_expression
        	| shift_expression RIGHT_OP additive_expression
        	;
            '''

        def p_Additive_Expression(p):
            '''
            additive_expression
        	: multiplicative_expression
        	| additive_expression PLUS multiplicative_expression
        	| additive_expression MINUS multiplicative_expression
        	;
            '''

        def p_Multiplicative_Expression(p):
            '''
            multiplicative_expression
        	: cast_expression
        	| multiplicative_expression ASTERISK cast_expression
        	| multiplicative_expression DIV cast_expression
        	| multiplicative_expression PERCENT cast_expression
        	;
            '''

        def p_Cast_Expression(p):
            '''
            cast_expression
        	: unary_expression
        	| OPENPAREN type_name CLOSEPAREN cast_expression
        	;
            '''

        def p_Unary_Expression(p):
            '''
            unary_expression
        	: postfix_expression
        	| INC_OP unary_expression
        	| DEC_OP unary_expression
        	| unary_operator cast_expression
        	| SIZEOF unary_expression
        	| SIZEOF OPENPAREN type_name CLOSEPAREN
        	;
            '''

        def p_Unary_Operator(p):
            '''
            unary_operator
        	: AMPERSAND
        	| ASTERISK
        	| PLUS
        	| MINUS
        	| TILDE
        	| BANG
        	;
            '''

        def p_Postfix_Expression(p):
            '''
            postfix_expression
        	: primary_expression
        	| postfix_expression OPENBRACKET expression CLOSEBRACKET
        	| postfix_expression OPENPAREN CLOSEPAREN
        	| postfix_expression OPENPAREN argument_expression_list CLOSEPAREN
        	| postfix_expression PERIOD identifier
        	| postfix_expression PTR_OP identifier
        	| postfix_expression INC_OP
        	| postfix_expression DEC_OP
        	;
            '''

        def p_Primary_Expression(p):
            '''
            primary_expression
        	: identifier
        	| constant
        	| string
        	| OPENPAREN expression CLOSEPAREN
        	;
            '''

        def p_Argument_Expression_List(p):
            '''
            argument_expression_list
        	: assignment_expression
        	| argument_expression_list COMMA assignment_expression
        	;
            '''

        def p_Constant(p):
            '''
            constant
        	: INTEGER_CONSTANT
        	| CHARACTER_CONSTANT
        	| FLOATING_CONSTANT
        	| ENUMERATION_CONSTANT
        	;
            '''

        def p_String(p):
            '''
            string
        	: STRING_LITERAL
        	;
            '''

        def p_Identifier(p):
            '''
            identifier
        	: IDENTIFIER
        	;
            '''



        #at some point we will use the following code:
        #(See PLY Documentation 6.12)
        # self.parser = yacc.parse(lexer=LA.Lexer)
