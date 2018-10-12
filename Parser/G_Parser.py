import sys
sys.path.append("LexicalAnalizer/")
sys.path.append("../LexicalAnalizer/")
from LexicalAnalizer import LexicalAnalizer
from SymbolTable import SymbolTable
import ply.yacc as yacc
import logging
logging.basicConfig(
    level = logging.DEBUG,
    filename = "parselog.txt",
    filemode = "w",
    format = "%(filename)10s:%(lineno)4d:%(message)s"
)
log = logging.getLogger()

class Parser():

    def __init__(self):
        self.ST = SymbolTable()
        self.LA = LexicalAnalizer(self.ST)
        self.Parser = None
        self.DebugProd = True

    #PLY Documentation http://www.dabeaz.com/ply/ply.html
    #Starting at 5
    def BuildParser(self):
        def p_translation_unit_1(p):
            'translation_unit :  external_declaration'
            if self.DebugProd == True:
                print("\ttranslation_unit -->  external_declaration")
            return

        def p_translation_unit_2(p):
            'translation_unit :  translation_unit external_declaration'
            if self.DebugProd == True:
                print("\ttranslation_unit -->  translation_unit external_declaration")
            return

        def p_external_declaration_1(p):
            'external_declaration :  function_definition'
            if self.DebugProd == True:
                print("\texternal_declaration -->  function_definition")
            return

        def p_external_declaration_2(p):
            'external_declaration :  declaration'
            if self.DebugProd == True:
                print("\texternal_declaration -->  declaration")
            return

        def p_function_definition_1(p):
            'function_definition :  declarator compound_statement'
            if self.DebugProd == True:
                print("\tfunction_definition -->  declarator compound_statement")
            return

        def p_function_definition_2(p):
            'function_definition :  declarator declaration_list compound_statement'
            if self.DebugProd == True:
                print("\tfunction_definition -->  declarator declaration_list compound_statement")
            return

        def p_function_definition_3(p):
            'function_definition :  declaration_specifiers declarator compound_statement'
            if self.DebugProd == True:
                print("\tfunction_definition -->  declaration_specifiers declarator compound_statement")
            return

        def p_function_definition_4(p):
            'function_definition :  declaration_specifiers declarator declaration_list compound_statement'
            if self.DebugProd == True:
                print("\tfunction_definition -->  declaration_specifiers declarator declaration_list compound_statement")
            return

        def p_declaration_1(p):
            'declaration :  declaration_specifiers SEMI'
            if self.DebugProd == True:
                print("\tdeclaration -->  declaration_specifiers SEMI")
            return

        def p_declaration_2(p):
            'declaration :  declaration_specifiers init_declarator_list SEMI'
            if self.DebugProd == True:
                print("\tdeclaration -->  declaration_specifiers init_declarator_list SEMI")
            return

        def p_declaration_list_1(p):
            'declaration_list :  declaration'
            if self.DebugProd == True:
                print("\tdeclaration_list -->  declaration")
            return

        def p_declaration_list_2(p):
            'declaration_list :  declaration_list declaration'
            if self.DebugProd == True:
                print("\tdeclaration_list -->  declaration_list declaration")
            return

        def p_declaration_specifiers_1(p):
            'declaration_specifiers :  storage_class_specifier'
            if self.DebugProd == True:
                print("\tdeclaration_specifiers -->  storage_class_specifier")
            return

        def p_declaration_specifiers_2(p):
            'declaration_specifiers :  storage_class_specifier declaration_specifiers'
            if self.DebugProd == True:
                print("\tdeclaration_specifiers -->  storage_class_specifier declaration_specifiers")
            return

        def p_declaration_specifiers_3(p):
            'declaration_specifiers :  type_specifier'
            if self.DebugProd == True:
                print("\tdeclaration_specifiers -->  type_specifier")
            return

        def p_declaration_specifiers_4(p):
            'declaration_specifiers :  type_specifier declaration_specifiers'
            if self.DebugProd == True:
                print("\tdeclaration_specifiers -->  type_specifier declaration_specifiers")
            return

        def p_declaration_specifiers_5(p):
            'declaration_specifiers :  type_qualifier'
            if self.DebugProd == True:
                print("\tdeclaration_specifiers -->  type_qualifier")
            return

        def p_declaration_specifiers_6(p):
            'declaration_specifiers :  type_qualifier declaration_specifiers'
            if self.DebugProd == True:
                print("\tdeclaration_specifiers -->  type_qualifier declaration_specifiers")
            return

        def p_storage_class_specifier_1(p):
            'storage_class_specifier :  AUTO'
            if self.DebugProd == True:
                print("\tstorage_class_specifier -->  AUTO")
            return

        def p_storage_class_specifier_2(p):
            'storage_class_specifier :  REGISTER'
            if self.DebugProd == True:
                print("\tstorage_class_specifier -->  REGISTER")
            return

        def p_storage_class_specifier_3(p):
            'storage_class_specifier :  STATIC'
            if self.DebugProd == True:
                print("\tstorage_class_specifier -->  STATIC")
            return

        def p_storage_class_specifier_4(p):
            'storage_class_specifier :  EXTERN'
            if self.DebugProd == True:
                print("\tstorage_class_specifier -->  EXTERN")
            return

        def p_storage_class_specifier_5(p):
            'storage_class_specifier :  TYPEDEF'
            if self.DebugProd == True:
                print("\tstorage_class_specifier -->  TYPEDEF")
            return

        def p_type_specifier_1(p):
            'type_specifier :  VOID'
            if self.DebugProd == True:
                print("\ttype_specifier -->  VOID")
            return

        def p_type_specifier_2(p):
            'type_specifier :  CHAR'
            if self.DebugProd == True:
                print("\ttype_specifier -->  CHAR")
            return

        def p_type_specifier_3(p):
            'type_specifier :  SHORT'
            if self.DebugProd == True:
                print("\ttype_specifier -->  SHORT")
            return

        def p_type_specifier_4(p):
            'type_specifier :  INT'
            if self.DebugProd == True:
                print("\ttype_specifier -->  INT")
            return

        def p_type_specifier_5(p):
            'type_specifier :  LONG'
            if self.DebugProd == True:
                print("\ttype_specifier -->  LONG")
            return

        def p_type_specifier_6(p):
            'type_specifier :  FLOAT'
            if self.DebugProd == True:
                print("\ttype_specifier -->  FLOAT")
            return

        def p_type_specifier_7(p):
            'type_specifier :  DOUBLE'
            if self.DebugProd == True:
                print("\ttype_specifier -->  DOUBLE")
            return

        def p_type_specifier_8(p):
            'type_specifier :  SIGNED'
            if self.DebugProd == True:
                print("\ttype_specifier -->  SIGNED")
            return

        def p_type_specifier_9(p):
            'type_specifier :  UNSIGNED'
            if self.DebugProd == True:
                print("\ttype_specifier -->  UNSIGNED")
            return

        def p_type_specifier_10(p):
            'type_specifier :  struct_or_union_specifier'
            if self.DebugProd == True:
                print("\ttype_specifier -->  struct_or_union_specifier")
            return

        def p_type_specifier_11(p):
            'type_specifier :  enum_specifier'
            if self.DebugProd == True:
                print("\ttype_specifier -->  enum_specifier")
            return

        def p_type_specifier_12(p):
            'type_specifier :  TYPEDEF_NAME'
            if self.DebugProd == True:
                print("\ttype_specifier -->  TYPEDEF_NAME")
            return

        def p_type_qualifier_1(p):
            'type_qualifier :  CONST'
            if self.DebugProd == True:
                print("\ttype_qualifier -->  CONST")
            return

        def p_type_qualifier_2(p):
            'type_qualifier :  VOLATILE'
            if self.DebugProd == True:
                print("\ttype_qualifier -->  VOLATILE")
            return

        def p_struct_or_union_specifier_1(p):
            'struct_or_union_specifier :  struct_or_union identifier OPENBRACE struct_declaration_list CLOSEBRACE'
            if self.DebugProd == True:
                print("\tstruct_or_union_specifier -->  struct_or_union identifier OPENBRACE struct_declaration_list CLOSEBRACE")
            return

        def p_struct_or_union_specifier_2(p):
            'struct_or_union_specifier :  struct_or_union OPENBRACE struct_declaration_list CLOSEBRACE'
            if self.DebugProd == True:
                print("\tstruct_or_union_specifier -->  struct_or_union OPENBRACE struct_declaration_list CLOSEBRACE")
            return

        def p_struct_or_union_specifier_3(p):
            'struct_or_union_specifier :  struct_or_union identifier'
            if self.DebugProd == True:
                print("\tstruct_or_union_specifier -->  struct_or_union identifier")
            return

        def p_struct_or_union_1(p):
            'struct_or_union :  STRUCT'
            if self.DebugProd == True:
                print("\tstruct_or_union -->  STRUCT")
            return

        def p_struct_or_union_2(p):
            'struct_or_union :  UNION'
            if self.DebugProd == True:
                print("\tstruct_or_union -->  UNION")
            return

        def p_struct_declaration_list_1(p):
            'struct_declaration_list :  struct_declaration'
            if self.DebugProd == True:
                print("\tstruct_declaration_list -->  struct_declaration")
            return

        def p_struct_declaration_list_2(p):
            'struct_declaration_list :  struct_declaration_list struct_declaration'
            if self.DebugProd == True:
                print("\tstruct_declaration_list -->  struct_declaration_list struct_declaration")
            return

        def p_init_declarator_list_1(p):
            'init_declarator_list :  init_declarator'
            if self.DebugProd == True:
                print("\tinit_declarator_list -->  init_declarator")
            return

        def p_init_declarator_list_2(p):
            'init_declarator_list :  init_declarator_list COMMA init_declarator'
            if self.DebugProd == True:
                print("\tinit_declarator_list -->  init_declarator_list COMMA init_declarator")
            return

        def p_init_declarator_1(p):
            'init_declarator :  declarator'
            if self.DebugProd == True:
                print("\tinit_declarator -->  declarator")
            return

        def p_init_declarator_2(p):
            'init_declarator :  declarator ASSIGN initializer'
            if self.DebugProd == True:
                print("\tinit_declarator -->  declarator ASSIGN initializer")
            return

        def p_struct_declaration_1(p):
            'struct_declaration :  specifier_qualifier_list struct_declarator_list SEMI'
            if self.DebugProd == True:
                print("\tstruct_declaration -->  specifier_qualifier_list struct_declarator_list SEMI")
            return

        def p_specifier_qualifier_list_1(p):
            'specifier_qualifier_list :  type_specifier'
            if self.DebugProd == True:
                print("\tspecifier_qualifier_list -->  type_specifier")
            return

        def p_specifier_qualifier_list_2(p):
            'specifier_qualifier_list :  type_specifier specifier_qualifier_list'
            if self.DebugProd == True:
                print("\tspecifier_qualifier_list -->  type_specifier specifier_qualifier_list")
            return

        def p_specifier_qualifier_list_3(p):
            'specifier_qualifier_list :  type_qualifier'
            if self.DebugProd == True:
                print("\tspecifier_qualifier_list -->  type_qualifier")
            return

        def p_specifier_qualifier_list_4(p):
            'specifier_qualifier_list :  type_qualifier specifier_qualifier_list'
            if self.DebugProd == True:
                print("\tspecifier_qualifier_list -->  type_qualifier specifier_qualifier_list")
            return

        def p_struct_declarator_list_1(p):
            'struct_declarator_list :  struct_declarator'
            if self.DebugProd == True:
                print("\tstruct_declarator_list -->  struct_declarator")
            return

        def p_struct_declarator_list_2(p):
            'struct_declarator_list :  struct_declarator_list COMMA struct_declarator'
            if self.DebugProd == True:
                print("\tstruct_declarator_list -->  struct_declarator_list COMMA struct_declarator")
            return

        def p_struct_declarator_1(p):
            'struct_declarator :  declarator'
            if self.DebugProd == True:
                print("\tstruct_declarator -->  declarator")
            return

        def p_struct_declarator_2(p):
            'struct_declarator :  COLON constant_expression'
            if self.DebugProd == True:
                print("\tstruct_declarator -->  COLON constant_expression")
            return

        def p_struct_declarator_3(p):
            'struct_declarator :  declarator COLON constant_expression'
            if self.DebugProd == True:
                print("\tstruct_declarator -->  declarator COLON constant_expression")
            return

        def p_enum_specifier_1(p):
            'enum_specifier :  ENUM OPENBRACE enumerator_list CLOSEBRACE'
            if self.DebugProd == True:
                print("\tenum_specifier -->  ENUM OPENBRACE enumerator_list CLOSEBRACE")
            return

        def p_enum_specifier_2(p):
            'enum_specifier :  ENUM identifier OPENBRACE enumerator_list CLOSEBRACE'
            if self.DebugProd == True:
                print("\tenum_specifier -->  ENUM identifier OPENBRACE enumerator_list CLOSEBRACE")
            return

        def p_enum_specifier_3(p):
            'enum_specifier :  ENUM identifier'
            if self.DebugProd == True:
                print("\tenum_specifier -->  ENUM identifier")
            return

        def p_enumerator_list_1(p):
            'enumerator_list :  enumerator'
            if self.DebugProd == True:
                print("\tenumerator_list -->  enumerator")
            return

        def p_enumerator_list_2(p):
            'enumerator_list :  enumerator_list COMMA enumerator'
            if self.DebugProd == True:
                print("\tenumerator_list -->  enumerator_list COMMA enumerator")
            return

        def p_enumerator_1(p):
            'enumerator :  identifier'
            if self.DebugProd == True:
                print("\tenumerator -->  identifier")
            return

        def p_enumerator_2(p):
            'enumerator :  identifier ASSIGN constant_expression'
            if self.DebugProd == True:
                print("\tenumerator -->  identifier ASSIGN constant_expression")
            return

        def p_declarator_1(p):
            'declarator :  direct_declarator'
            if self.DebugProd == True:
                print("\tdeclarator -->  direct_declarator")
            return

        def p_declarator_2(p):
            'declarator :  pointer direct_declarator'
            if self.DebugProd == True:
                print("\tdeclarator -->  pointer direct_declarator")
            return

        def p_direct_declarator_1(p):
            'direct_declarator :  identifier'
            if self.DebugProd == True:
                print("\tdirect_declarator -->  identifier")
            return

        def p_direct_declarator_2(p):
            'direct_declarator :  OPENPAREN declarator CLOSEPAREN'
            if self.DebugProd == True:
                print("\tdirect_declarator -->  OPENPAREN declarator CLOSEPAREN")
            return

        def p_direct_declarator_3(p):
            'direct_declarator :  direct_declarator OPENBRACKET CLOSEBRACKET'
            if self.DebugProd == True:
                print("\tdirect_declarator -->  direct_declarator OPENBRACKET CLOSEBRACKET")
            return

        def p_direct_declarator_4(p):
            'direct_declarator :  direct_declarator OPENBRACKET constant_expression CLOSEBRACKET'
            if self.DebugProd == True:
                print("\tdirect_declarator -->  direct_declarator OPENBRACKET constant_expression CLOSEBRACKET")
            return

        def p_direct_declarator_5(p):
            'direct_declarator :  direct_declarator OPENPAREN CLOSEPAREN'
            if self.DebugProd == True:
                print("\tdirect_declarator -->  direct_declarator OPENPAREN CLOSEPAREN")
            return

        def p_direct_declarator_6(p):
            'direct_declarator :  direct_declarator OPENPAREN parameter_type_list CLOSEPAREN'
            if self.DebugProd == True:
                print("\tdirect_declarator -->  direct_declarator OPENPAREN parameter_type_list CLOSEPAREN")
            return

        def p_direct_declarator_7(p):
            'direct_declarator :  direct_declarator OPENPAREN identifier_list CLOSEPAREN'
            if self.DebugProd == True:
                print("\tdirect_declarator -->  direct_declarator OPENPAREN identifier_list CLOSEPAREN")
            return

        def p_pointer_1(p):
            'pointer :  ASTERISK'
            if self.DebugProd == True:
                print("\tpointer -->  ASTERISK")
            return

        def p_pointer_2(p):
            'pointer :  ASTERISK type_qualifier_list'
            if self.DebugProd == True:
                print("\tpointer -->  ASTERISK type_qualifier_list")
            return

        def p_pointer_3(p):
            'pointer :  ASTERISK pointer'
            if self.DebugProd == True:
                print("\tpointer -->  ASTERISK pointer")
            return

        def p_pointer_4(p):
            'pointer :  ASTERISK type_qualifier_list pointer'
            if self.DebugProd == True:
                print("\tpointer -->  ASTERISK type_qualifier_list pointer")
            return

        def p_type_qualifier_list_1(p):
            'type_qualifier_list :  type_qualifier'
            if self.DebugProd == True:
                print("\ttype_qualifier_list -->  type_qualifier")
            return

        def p_type_qualifier_list_2(p):
            'type_qualifier_list :  type_qualifier_list type_qualifier'
            if self.DebugProd == True:
                print("\ttype_qualifier_list -->  type_qualifier_list type_qualifier")
            return

        def p_parameter_type_list_1(p):
            'parameter_type_list :  parameter_list'
            if self.DebugProd == True:
                print("\tparameter_type_list -->  parameter_list")
            return

        def p_parameter_type_list_2(p):
            'parameter_type_list :  parameter_list COMMA ELIPSIS'
            if self.DebugProd == True:
                print("\tparameter_type_list -->  parameter_list COMMA ELIPSIS")
            return

        def p_parameter_list_1(p):
            'parameter_list :  parameter_declaration'
            if self.DebugProd == True:
                print("\tparameter_list -->  parameter_declaration")
            return

        def p_parameter_list_2(p):
            'parameter_list :  parameter_list COMMA parameter_declaration'
            if self.DebugProd == True:
                print("\tparameter_list -->  parameter_list COMMA parameter_declaration")
            return

        def p_parameter_declaration_1(p):
            'parameter_declaration :  declaration_specifiers declarator'
            if self.DebugProd == True:
                print("\tparameter_declaration -->  declaration_specifiers declarator")
            return

        def p_parameter_declaration_2(p):
            'parameter_declaration :  declaration_specifiers'
            if self.DebugProd == True:
                print("\tparameter_declaration -->  declaration_specifiers")
            return

        def p_parameter_declaration_3(p):
            'parameter_declaration :  declaration_specifiers abstract_declarator'
            if self.DebugProd == True:
                print("\tparameter_declaration -->  declaration_specifiers abstract_declarator")
            return

        def p_identifier_list_1(p):
            'identifier_list :  identifier'
            if self.DebugProd == True:
                print("\tidentifier_list -->  identifier")
            return

        def p_identifier_list_2(p):
            'identifier_list :  identifier_list COMMA identifier'
            if self.DebugProd == True:
                print("\tidentifier_list -->  identifier_list COMMA identifier")
            return

        def p_initializer_1(p):
            'initializer :  assignment_expression'
            if self.DebugProd == True:
                print("\tinitializer -->  assignment_expression")
            return

        def p_initializer_2(p):
            'initializer :  OPENBRACE initializer_list CLOSEBRACE'
            if self.DebugProd == True:
                print("\tinitializer -->  OPENBRACE initializer_list CLOSEBRACE")
            return

        def p_initializer_3(p):
            'initializer :  OPENBRACE initializer_list COMMA CLOSEBRACE'
            if self.DebugProd == True:
                print("\tinitializer -->  OPENBRACE initializer_list COMMA CLOSEBRACE")
            return

        def p_initializer_list_1(p):
            'initializer_list :  initializer'
            if self.DebugProd == True:
                print("\tinitializer_list -->  initializer")
            return

        def p_initializer_list_2(p):
            'initializer_list :  initializer_list COMMA initializer'
            if self.DebugProd == True:
                print("\tinitializer_list -->  initializer_list COMMA initializer")
            return

        def p_type_name_1(p):
            'type_name :  specifier_qualifier_list'
            if self.DebugProd == True:
                print("\ttype_name -->  specifier_qualifier_list")
            return

        def p_type_name_2(p):
            'type_name :  specifier_qualifier_list abstract_declarator'
            if self.DebugProd == True:
                print("\ttype_name -->  specifier_qualifier_list abstract_declarator")
            return

        def p_abstract_declarator_1(p):
            'abstract_declarator :  pointer'
            if self.DebugProd == True:
                print("\tabstract_declarator -->  pointer")
            return

        def p_abstract_declarator_2(p):
            'abstract_declarator :  direct_abstract_declarator'
            if self.DebugProd == True:
                print("\tabstract_declarator -->  direct_abstract_declarator")
            return

        def p_abstract_declarator_3(p):
            'abstract_declarator :  pointer direct_abstract_declarator'
            if self.DebugProd == True:
                print("\tabstract_declarator -->  pointer direct_abstract_declarator")
            return

        def p_direct_abstract_declarator_1(p):
            'direct_abstract_declarator :  OPENPAREN abstract_declarator CLOSEPAREN'
            if self.DebugProd == True:
                print("\tdirect_abstract_declarator -->  OPENPAREN abstract_declarator CLOSEPAREN")
            return

        def p_direct_abstract_declarator_2(p):
            'direct_abstract_declarator :  OPENBRACKET CLOSEBRACKET'
            if self.DebugProd == True:
                print("\tdirect_abstract_declarator -->  OPENBRACKET CLOSEBRACKET")
            return

        def p_direct_abstract_declarator_3(p):
            'direct_abstract_declarator :  OPENBRACKET constant_expression CLOSEBRACKET'
            if self.DebugProd == True:
                print("\tdirect_abstract_declarator -->  OPENBRACKET constant_expression CLOSEBRACKET")
            return

        def p_direct_abstract_declarator_4(p):
            'direct_abstract_declarator :  direct_abstract_declarator OPENBRACKET CLOSEBRACKET'
            if self.DebugProd == True:
                print("\tdirect_abstract_declarator -->  direct_abstract_declarator OPENBRACKET CLOSEBRACKET")
            return

        def p_direct_abstract_declarator_5(p):
            'direct_abstract_declarator :  direct_abstract_declarator OPENBRACKET constant_expression CLOSEBRACKET'
            if self.DebugProd == True:
                print("\tdirect_abstract_declarator -->  direct_abstract_declarator OPENBRACKET constant_expression CLOSEBRACKET")
            return

        def p_direct_abstract_declarator_6(p):
            'direct_abstract_declarator :  OPENPAREN CLOSEPAREN'
            if self.DebugProd == True:
                print("\tdirect_abstract_declarator -->  OPENPAREN CLOSEPAREN")
            return

        def p_direct_abstract_declarator_7(p):
            'direct_abstract_declarator :  OPENPAREN parameter_type_list CLOSEPAREN'
            if self.DebugProd == True:
                print("\tdirect_abstract_declarator -->  OPENPAREN parameter_type_list CLOSEPAREN")
            return

        def p_direct_abstract_declarator_8(p):
            'direct_abstract_declarator :  direct_abstract_declarator OPENPAREN CLOSEPAREN'
            if self.DebugProd == True:
                print("\tdirect_abstract_declarator -->  direct_abstract_declarator OPENPAREN CLOSEPAREN")
            return

        def p_direct_abstract_declarator_9(p):
            'direct_abstract_declarator :  direct_abstract_declarator OPENPAREN parameter_type_list CLOSEPAREN'
            if self.DebugProd == True:
                print("\tdirect_abstract_declarator -->  direct_abstract_declarator OPENPAREN parameter_type_list CLOSEPAREN")
            return

        def p_statement_1(p):
            'statement :  labeled_statement'
            if self.DebugProd == True:
                print("\tstatement -->  labeled_statement")
            return

        def p_statement_2(p):
            'statement :  compound_statement'
            if self.DebugProd == True:
                print("\tstatement -->  compound_statement")
            return

        def p_statement_3(p):
            'statement :  expression_statement'
            if self.DebugProd == True:
                print("\tstatement -->  expression_statement")
            return

        def p_statement_4(p):
            'statement :  selection_statement'
            if self.DebugProd == True:
                print("\tstatement -->  selection_statement")
            return

        def p_statement_5(p):
            'statement :  iteration_statement'
            if self.DebugProd == True:
                print("\tstatement -->  iteration_statement")
            return

        def p_statement_6(p):
            'statement :  jump_statement'
            if self.DebugProd == True:
                print("\tstatement -->  jump_statement")
            return

        def p_labeled_statement_1(p):
            'labeled_statement :  identifier COLON statement'
            if self.DebugProd == True:
                print("\tlabeled_statement -->  identifier COLON statement")
            return

        def p_labeled_statement_2(p):
            'labeled_statement :  CASE constant_expression COLON statement'
            if self.DebugProd == True:
                print("\tlabeled_statement -->  CASE constant_expression COLON statement")
            return

        def p_labeled_statement_3(p):
            'labeled_statement :  DEFAULT COLON statement'
            if self.DebugProd == True:
                print("\tlabeled_statement -->  DEFAULT COLON statement")
            return

        def p_expression_statement_1(p):
            'expression_statement :  SEMI'
            if self.DebugProd == True:
                print("\texpression_statement -->  SEMI")
            return

        def p_expression_statement_2(p):
            'expression_statement :  expression SEMI'
            if self.DebugProd == True:
                print("\texpression_statement -->  expression SEMI")
            return

        def p_compound_statement_1(p):
            'compound_statement :  OPENBRACE CLOSEBRACE'
            if self.DebugProd == True:
                print("\tcompound_statement -->  OPENBRACE CLOSEBRACE")
            return

        def p_compound_statement_2(p):
            'compound_statement :  OPENBRACE statement_list CLOSEBRACE'
            if self.DebugProd == True:
                print("\tcompound_statement -->  OPENBRACE statement_list CLOSEBRACE")
            return

        def p_compound_statement_3(p):
            'compound_statement :  OPENBRACE declaration_list CLOSEBRACE'
            if self.DebugProd == True:
                print("\tcompound_statement -->  OPENBRACE declaration_list CLOSEBRACE")
            return

        def p_compound_statement_4(p):
            'compound_statement :  OPENBRACE declaration_list statement_list CLOSEBRACE'
            if self.DebugProd == True:
                print("\tcompound_statement -->  OPENBRACE declaration_list statement_list CLOSEBRACE")
            return

        def p_statement_list_1(p):
            'statement_list :  statement'
            if self.DebugProd == True:
                print("\tstatement_list -->  statement")
            return

        def p_statement_list_2(p):
            'statement_list :  statement_list statement'
            if self.DebugProd == True:
                print("\tstatement_list -->  statement_list statement")
            return

        def p_selection_statement_1(p):
            'selection_statement :  IF OPENPAREN expression CLOSEPAREN statement'
            if self.DebugProd == True:
                print("\tselection_statement -->  IF OPENPAREN expression CLOSEPAREN statement")
            return

        def p_selection_statement_2(p):
            'selection_statement :  IF OPENPAREN expression CLOSEPAREN statement ELSE statement'
            if self.DebugProd == True:
                print("\tselection_statement -->  IF OPENPAREN expression CLOSEPAREN statement ELSE statement")
            return

        def p_selection_statement_3(p):
            'selection_statement :  SWITCH OPENPAREN expression CLOSEPAREN statement'
            if self.DebugProd == True:
                print("\tselection_statement -->  SWITCH OPENPAREN expression CLOSEPAREN statement")
            return

        def p_iteration_statement_1(p):
            'iteration_statement :  WHILE OPENPAREN expression CLOSEPAREN statement'
            if self.DebugProd == True:
                print("\titeration_statement -->  WHILE OPENPAREN expression CLOSEPAREN statement")
            return

        def p_iteration_statement_2(p):
            'iteration_statement :  DO statement WHILE OPENPAREN expression CLOSEPAREN SEMI'
            if self.DebugProd == True:
                print("\titeration_statement -->  DO statement WHILE OPENPAREN expression CLOSEPAREN SEMI")
            return

        def p_iteration_statement_3(p):
            'iteration_statement :  FOR OPENPAREN SEMI SEMI CLOSEPAREN statement'
            if self.DebugProd == True:
                print("\titeration_statement -->  FOR OPENPAREN SEMI SEMI CLOSEPAREN statement")
            return

        def p_iteration_statement_4(p):
            'iteration_statement :  FOR OPENPAREN SEMI SEMI expression CLOSEPAREN statement'
            if self.DebugProd == True:
                print("\titeration_statement -->  FOR OPENPAREN SEMI SEMI expression CLOSEPAREN statement")
            return

        def p_iteration_statement_5(p):
            'iteration_statement :  FOR OPENPAREN SEMI expression SEMI CLOSEPAREN statement'
            if self.DebugProd == True:
                print("\titeration_statement -->  FOR OPENPAREN SEMI expression SEMI CLOSEPAREN statement")
            return

        def p_iteration_statement_6(p):
            'iteration_statement :  FOR OPENPAREN SEMI expression SEMI expression CLOSEPAREN statement'
            if self.DebugProd == True:
                print("\titeration_statement -->  FOR OPENPAREN SEMI expression SEMI expression CLOSEPAREN statement")
            return

        def p_iteration_statement_7(p):
            'iteration_statement :  FOR OPENPAREN expression SEMI SEMI CLOSEPAREN statement'
            if self.DebugProd == True:
                print("\titeration_statement -->  FOR OPENPAREN expression SEMI SEMI CLOSEPAREN statement")
            return

        def p_iteration_statement_8(p):
            'iteration_statement :  FOR OPENPAREN expression SEMI SEMI expression CLOSEPAREN statement'
            if self.DebugProd == True:
                print("\titeration_statement -->  FOR OPENPAREN expression SEMI SEMI expression CLOSEPAREN statement")
            return

        def p_iteration_statement_9(p):
            'iteration_statement :  FOR OPENPAREN expression SEMI expression SEMI CLOSEPAREN statement'
            if self.DebugProd == True:
                print("\titeration_statement -->  FOR OPENPAREN expression SEMI expression SEMI CLOSEPAREN statement")
            return

        def p_iteration_statement_10(p):
            'iteration_statement :  FOR OPENPAREN expression SEMI expression SEMI expression CLOSEPAREN statement'
            if self.DebugProd == True:
                print("\titeration_statement -->  FOR OPENPAREN expression SEMI expression SEMI expression CLOSEPAREN statement")
            return

        def p_jump_statement_1(p):
            'jump_statement :  GOTO identifier SEMI'
            if self.DebugProd == True:
                print("\tjump_statement -->  GOTO identifier SEMI")
            return

        def p_jump_statement_2(p):
            'jump_statement :  CONTINUE SEMI'
            if self.DebugProd == True:
                print("\tjump_statement -->  CONTINUE SEMI")
            return

        def p_jump_statement_3(p):
            'jump_statement :  BREAK SEMI'
            if self.DebugProd == True:
                print("\tjump_statement -->  BREAK SEMI")
            return

        def p_jump_statement_4(p):
            'jump_statement :  RETURN SEMI'
            if self.DebugProd == True:
                print("\tjump_statement -->  RETURN SEMI")
            return

        def p_jump_statement_5(p):
            'jump_statement :  RETURN expression SEMI'
            if self.DebugProd == True:
                print("\tjump_statement -->  RETURN expression SEMI")
            return

        def p_expression_1(p):
            'expression :  assignment_expression'
            if self.DebugProd == True:
                print("\texpression -->  assignment_expression")
            return

        def p_expression_2(p):
            'expression :  expression COMMA assignment_expression'
            if self.DebugProd == True:
                print("\texpression -->  expression COMMA assignment_expression")
            return

        def p_assignment_expression_1(p):
            'assignment_expression :  conditional_expression'
            if self.DebugProd == True:
                print("\tassignment_expression -->  conditional_expression")
            return

        def p_assignment_expression_2(p):
            'assignment_expression :  unary_expression assignment_operator assignment_expression'
            if self.DebugProd == True:
                print("\tassignment_expression -->  unary_expression assignment_operator assignment_expression")
            return

        def p_assignment_operator_1(p):
            'assignment_operator :  ASSIGN'
            if self.DebugProd == True:
                print("\tassignment_operator -->  ASSIGN")
            return

        def p_assignment_operator_2(p):
            'assignment_operator :  MUL_ASSIGN'
            if self.DebugProd == True:
                print("\tassignment_operator -->  MUL_ASSIGN")
            return

        def p_assignment_operator_3(p):
            'assignment_operator :  DIV_ASSIGN'
            if self.DebugProd == True:
                print("\tassignment_operator -->  DIV_ASSIGN")
            return

        def p_assignment_operator_4(p):
            'assignment_operator :  MOD_ASSIGN'
            if self.DebugProd == True:
                print("\tassignment_operator -->  MOD_ASSIGN")
            return

        def p_assignment_operator_5(p):
            'assignment_operator :  ADD_ASSIGN'
            if self.DebugProd == True:
                print("\tassignment_operator -->  ADD_ASSIGN")
            return

        def p_assignment_operator_6(p):
            'assignment_operator :  SUB_ASSIGN'
            if self.DebugProd == True:
                print("\tassignment_operator -->  SUB_ASSIGN")
            return

        def p_assignment_operator_7(p):
            'assignment_operator :  LEFT_ASSIGN'
            if self.DebugProd == True:
                print("\tassignment_operator -->  LEFT_ASSIGN")
            return

        def p_assignment_operator_8(p):
            'assignment_operator :  RIGHT_ASSIGN'
            if self.DebugProd == True:
                print("\tassignment_operator -->  RIGHT_ASSIGN")
            return

        def p_assignment_operator_9(p):
            'assignment_operator :  AND_ASSIGN'
            if self.DebugProd == True:
                print("\tassignment_operator -->  AND_ASSIGN")
            return

        def p_assignment_operator_10(p):
            'assignment_operator :  XOR_ASSIGN'
            if self.DebugProd == True:
                print("\tassignment_operator -->  XOR_ASSIGN")
            return

        def p_assignment_operator_11(p):
            'assignment_operator :  OR_ASSIGN'
            if self.DebugProd == True:
                print("\tassignment_operator -->  OR_ASSIGN")
            return

        def p_conditional_expression_1(p):
            'conditional_expression :  logical_or_expression'
            if self.DebugProd == True:
                print("\tconditional_expression -->  logical_or_expression")
            return

        def p_conditional_expression_2(p):
            'conditional_expression :  logical_or_expression QMARK expression COLON conditional_expression'
            if self.DebugProd == True:
                print("\tconditional_expression -->  logical_or_expression QMARK expression COLON conditional_expression")
            return

        def p_constant_expression_1(p):
            'constant_expression :  conditional_expression'
            if self.DebugProd == True:
                print("\tconstant_expression -->  conditional_expression")
            return

        def p_logical_or_expression_1(p):
            'logical_or_expression :  logical_and_expression'
            if self.DebugProd == True:
                print("\tlogical_or_expression -->  logical_and_expression")
            return

        def p_logical_or_expression_2(p):
            'logical_or_expression :  logical_or_expression OR_OP logical_and_expression'
            if self.DebugProd == True:
                print("\tlogical_or_expression -->  logical_or_expression OR_OP logical_and_expression")
            return

        def p_logical_and_expression_1(p):
            'logical_and_expression :  inclusive_or_expression'
            if self.DebugProd == True:
                print("\tlogical_and_expression -->  inclusive_or_expression")
            return

        def p_logical_and_expression_2(p):
            'logical_and_expression :  logical_and_expression AND_OP inclusive_or_expression'
            if self.DebugProd == True:
                print("\tlogical_and_expression -->  logical_and_expression AND_OP inclusive_or_expression")
            return

        def p_inclusive_or_expression_1(p):
            'inclusive_or_expression :  exclusive_or_expression'
            if self.DebugProd == True:
                print("\tinclusive_or_expression -->  exclusive_or_expression")
            return

        def p_inclusive_or_expression_2(p):
            'inclusive_or_expression :  inclusive_or_expression PIPE exclusive_or_expression'
            if self.DebugProd == True:
                print("\tinclusive_or_expression -->  inclusive_or_expression PIPE exclusive_or_expression")
            return

        def p_exclusive_or_expression_1(p):
            'exclusive_or_expression :  and_expression'
            if self.DebugProd == True:
                print("\texclusive_or_expression -->  and_expression")
            return

        def p_exclusive_or_expression_2(p):
            'exclusive_or_expression :  exclusive_or_expression CARAT and_expression'
            if self.DebugProd == True:
                print("\texclusive_or_expression -->  exclusive_or_expression CARAT and_expression")
            return

        def p_and_expression_1(p):
            'and_expression :  equality_expression'
            if self.DebugProd == True:
                print("\tand_expression -->  equality_expression")
            return

        def p_and_expression_2(p):
            'and_expression :  and_expression AMPERSAND equality_expression'
            if self.DebugProd == True:
                print("\tand_expression -->  and_expression AMPERSAND equality_expression")
            return

        def p_equality_expression_1(p):
            'equality_expression :  relational_expression'
            if self.DebugProd == True:
                print("\tequality_expression -->  relational_expression")
            return

        def p_equality_expression_2(p):
            'equality_expression :  equality_expression EQ_OP relational_expression'
            if self.DebugProd == True:
                print("\tequality_expression -->  equality_expression EQ_OP relational_expression")
            return

        def p_equality_expression_3(p):
            'equality_expression :  equality_expression NE_OP relational_expression'
            if self.DebugProd == True:
                print("\tequality_expression -->  equality_expression NE_OP relational_expression")
            return

        def p_relational_expression_1(p):
            'relational_expression :  shift_expression'
            if self.DebugProd == True:
                print("\trelational_expression -->  shift_expression")
            return

        def p_relational_expression_2(p):
            'relational_expression :  relational_expression LE shift_expression'
            if self.DebugProd == True:
                print("\trelational_expression -->  relational_expression LE shift_expression")
            return

        def p_relational_expression_3(p):
            'relational_expression :  relational_expression GT shift_expression'
            if self.DebugProd == True:
                print("\trelational_expression -->  relational_expression GT shift_expression")
            return

        def p_relational_expression_4(p):
            'relational_expression :  relational_expression LE_OP shift_expression'
            if self.DebugProd == True:
                print("\trelational_expression -->  relational_expression LE_OP shift_expression")
            return

        def p_relational_expression_5(p):
            'relational_expression :  relational_expression GE_OP shift_expression'
            if self.DebugProd == True:
                print("\trelational_expression -->  relational_expression GE_OP shift_expression")
            return

        def p_shift_expression_1(p):
            'shift_expression :  additive_expression'
            if self.DebugProd == True:
                print("\tshift_expression -->  additive_expression")
            return

        def p_shift_expression_2(p):
            'shift_expression :  shift_expression LEFT_OP additive_expression'
            if self.DebugProd == True:
                print("\tshift_expression -->  shift_expression LEFT_OP additive_expression")
            return

        def p_shift_expression_3(p):
            'shift_expression :  shift_expression RIGHT_OP additive_expression'
            if self.DebugProd == True:
                print("\tshift_expression -->  shift_expression RIGHT_OP additive_expression")
            return

        def p_additive_expression_1(p):
            'additive_expression :  multiplicative_expression'
            if self.DebugProd == True:
                print("\tadditive_expression -->  multiplicative_expression")
            return

        def p_additive_expression_2(p):
            'additive_expression :  additive_expression PLUS multiplicative_expression'
            if self.DebugProd == True:
                print("\tadditive_expression -->  additive_expression PLUS multiplicative_expression")
            return

        def p_additive_expression_3(p):
            'additive_expression :  additive_expression MINUS multiplicative_expression'
            if self.DebugProd == True:
                print("\tadditive_expression -->  additive_expression MINUS multiplicative_expression")
            return

        def p_multiplicative_expression_1(p):
            'multiplicative_expression :  cast_expression'
            if self.DebugProd == True:
                print("\tmultiplicative_expression -->  cast_expression")
            return

        def p_multiplicative_expression_2(p):
            'multiplicative_expression :  multiplicative_expression ASTERISK cast_expression'
            if self.DebugProd == True:
                print("\tmultiplicative_expression -->  multiplicative_expression ASTERISK cast_expression")
            return

        def p_multiplicative_expression_3(p):
            'multiplicative_expression :  multiplicative_expression DIV cast_expression'
            if self.DebugProd == True:
                print("\tmultiplicative_expression -->  multiplicative_expression DIV cast_expression")
            return

        def p_multiplicative_expression_4(p):
            'multiplicative_expression :  multiplicative_expression PERCENT cast_expression'
            if self.DebugProd == True:
                print("\tmultiplicative_expression -->  multiplicative_expression PERCENT cast_expression")
            return

        def p_cast_expression_1(p):
            'cast_expression :  unary_expression'
            if self.DebugProd == True:
                print("\tcast_expression -->  unary_expression")
            return

        def p_cast_expression_2(p):
            'cast_expression :  OPENPAREN type_name CLOSEPAREN cast_expression'
            if self.DebugProd == True:
                print("\tcast_expression -->  OPENPAREN type_name CLOSEPAREN cast_expression")
            return

        def p_unary_expression_1(p):
            'unary_expression :  postfix_expression'
            if self.DebugProd == True:
                print("\tunary_expression -->  postfix_expression")
            return

        def p_unary_expression_2(p):
            'unary_expression :  INC_OP unary_expression'
            if self.DebugProd == True:
                print("\tunary_expression -->  INC_OP unary_expression")
            return

        def p_unary_expression_3(p):
            'unary_expression :  DEC_OP unary_expression'
            if self.DebugProd == True:
                print("\tunary_expression -->  DEC_OP unary_expression")
            return

        def p_unary_expression_4(p):
            'unary_expression :  unary_operator cast_expression'
            if self.DebugProd == True:
                print("\tunary_expression -->  unary_operator cast_expression")
            return

        def p_unary_expression_5(p):
            'unary_expression :  SIZEOF unary_expression'
            if self.DebugProd == True:
                print("\tunary_expression -->  SIZEOF unary_expression")
            return

        def p_unary_expression_6(p):
            'unary_expression :  SIZEOF OPENPAREN type_name CLOSEPAREN'
            if self.DebugProd == True:
                print("\tunary_expression -->  SIZEOF OPENPAREN type_name CLOSEPAREN")
            return

        def p_unary_operator_1(p):
            'unary_operator :  AMPERSAND'
            if self.DebugProd == True:
                print("\tunary_operator -->  AMPERSAND")
            return

        def p_unary_operator_2(p):
            'unary_operator :  ASTERISK'
            if self.DebugProd == True:
                print("\tunary_operator -->  ASTERISK")
            return

        def p_unary_operator_3(p):
            'unary_operator :  PLUS'
            if self.DebugProd == True:
                print("\tunary_operator -->  PLUS")
            return

        def p_unary_operator_4(p):
            'unary_operator :  MINUS'
            if self.DebugProd == True:
                print("\tunary_operator -->  MINUS")
            return

        def p_unary_operator_5(p):
            'unary_operator :  TILDE'
            if self.DebugProd == True:
                print("\tunary_operator -->  TILDE")
            return

        def p_unary_operator_6(p):
            'unary_operator :  BANG'
            if self.DebugProd == True:
                print("\tunary_operator -->  BANG")
            return

        def p_postfix_expression_1(p):
            'postfix_expression :  primary_expression'
            if self.DebugProd == True:
                print("\tpostfix_expression -->  primary_expression")
            return

        def p_postfix_expression_2(p):
            'postfix_expression :  postfix_expression OPENBRACKET expression CLOSEBRACKET'
            if self.DebugProd == True:
                print("\tpostfix_expression -->  postfix_expression OPENBRACKET expression CLOSEBRACKET")
            return

        def p_postfix_expression_3(p):
            'postfix_expression :  postfix_expression OPENPAREN CLOSEPAREN'
            if self.DebugProd == True:
                print("\tpostfix_expression -->  postfix_expression OPENPAREN CLOSEPAREN")
            return

        def p_postfix_expression_4(p):
            'postfix_expression :  postfix_expression OPENPAREN argument_expression_list CLOSEPAREN'
            if self.DebugProd == True:
                print("\tpostfix_expression -->  postfix_expression OPENPAREN argument_expression_list CLOSEPAREN")
            return

        def p_postfix_expression_5(p):
            'postfix_expression :  postfix_expression PERIOD identifier'
            if self.DebugProd == True:
                print("\tpostfix_expression -->  postfix_expression PERIOD identifier")
            return

        def p_postfix_expression_6(p):
            'postfix_expression :  postfix_expression PTR_OP identifier'
            if self.DebugProd == True:
                print("\tpostfix_expression -->  postfix_expression PTR_OP identifier")
            return

        def p_postfix_expression_7(p):
            'postfix_expression :  postfix_expression INC_OP'
            if self.DebugProd == True:
                print("\tpostfix_expression -->  postfix_expression INC_OP")
            return

        def p_postfix_expression_8(p):
            'postfix_expression :  postfix_expression DEC_OP'
            if self.DebugProd == True:
                print("\tpostfix_expression -->  postfix_expression DEC_OP")
            return

        def p_primary_expression_1(p):
            'primary_expression :  identifier'
            if self.DebugProd == True:
                print("\tprimary_expression -->  identifier")
            return

        def p_primary_expression_2(p):
            'primary_expression :  constant'
            if self.DebugProd == True:
                print("\tprimary_expression -->  constant")
            return

        def p_primary_expression_3(p):
            'primary_expression :  string'
            if self.DebugProd == True:
                print("\tprimary_expression -->  string")
            return

        def p_primary_expression_4(p):
            'primary_expression :  OPENPAREN expression CLOSEPAREN'
            if self.DebugProd == True:
                print("\tprimary_expression -->  OPENPAREN expression CLOSEPAREN")
            return

        def p_argument_expression_list_1(p):
            'argument_expression_list :  assignment_expression'
            if self.DebugProd == True:
                print("\targument_expression_list -->  assignment_expression")
            return

        def p_argument_expression_list_2(p):
            'argument_expression_list :  argument_expression_list COMMA assignment_expression'
            if self.DebugProd == True:
                print("\targument_expression_list -->  argument_expression_list COMMA assignment_expression")
            return

        def p_constant_1(p):
            'constant :  INTEGER_CONSTANT'
            if self.DebugProd == True:
                print("\tconstant -->  INTEGER_CONSTANT")
            return

        def p_constant_2(p):
            'constant :  CHARACTER_CONSTANT'
            if self.DebugProd == True:
                print("\tconstant -->  CHARACTER_CONSTANT")
            return

        def p_constant_3(p):
            'constant :  FLOATING_CONSTANT'
            if self.DebugProd == True:
                print("\tconstant -->  FLOATING_CONSTANT")
            return

        def p_constant_4(p):
            'constant :  ENUMERATION_CONSTANT'
            if self.DebugProd == True:
                print("\tconstant -->  ENUMERATION_CONSTANT")
            return

        def p_string_1(p):
            'string :  STRING_LITERAL'
            if self.DebugProd == True:
                print("\tstring -->  STRING_LITERAL")
            return

        def p_identifier_1(p):
            'identifier :  IDENTIFIER'
            if self.DebugProd == True:
                print("\tidentifier -->  IDENTIFIER")
            return


        tokens = self.LA.Tokens


        #at some point we will use the following code:
        #(See PLY Documentation 6.12)
        self.LA.BuildLexer()
        self.Parser = yacc.yacc(errorlog=log)
