import sys
sys.path.append("LexicalAnalizer/")
sys.path.append("../LexicalAnalizer/")
from Globals import ErrManager
from Utils import PrettyErrorPrint, FindColumn
from LexicalAnalizer import LexicalAnalizer
from SymbolTable import SymbolTable
from ASTBuilder import FunctionPrototype, FunctionCall, Identifier, ArrayDeclaration, PassUpNode, SelectionStatement, DeclarationSpecifiers, DeclList, Declaration, PrimaryExpression, UnaryExpression, Constant, FunctionDefintion, CompoundStatement, AssignmentExpression, InitDeclList, BinOp, IterationStatement, ArrayAccess
import ply.yacc as yacc
# import logging
# logging.basicConfig(
#     level = logging.DEBUG,
#     filename = "parselog.txt",
#     filemode = "w",
#     format = "%(filename)10s:%(lineno)4d:%(message)s"
# )
# log = logging.getLogger()

class Parser():

    #Constructor for parser class
    def __init__(self, SourceFile = None, DebugArgs = None):
        self.ST = SymbolTable(SourceFile)
        self.SourceFile = SourceFile
        self.LA = LexicalAnalizer(self.ST, SourceFile=SourceFile, DebugArgs = DebugArgs)
        self.Parser = None
        self.DebugProd = False
        self.DebugProdL = [False, False]    #for multiple levels of debug
        for args in DebugArgs:
            if args == '-d':
                self.DebugProd = True
                print("parser debug on")
        self.InDeclarationBlock = False
        self.AST = None

    def DebugPrint(self, Reduction, ParseObjs = None):

        s = '''\nReduction: {0}'''
        ParseObj = '''Node {0}: {1}'''

        print(s.format(Reduction))

        if ParseObjs is not None:
            for i, P in enumerate(ParseObjs):
                print(ParseObj.format(i, P))

        print("")

        return

    def RunParser(self):
        try:
            with open(self.SourceFile) as file:
                s = file.read()
            self.Parser.parse(s, debug=0)
        except Exception as e:
            raise e

        return self.AST

    def ToggleDebugMode(self):
        self.DebugProd = not self.DebugProd

    #PLY Documentation http://www.dabeaz.com/ply/ply.html
    #Main function to build up the Parser
    #Contains all the productions
    def BuildParser(self):
        def p_translation_unit_1(p):
            'translation_unit :  external_declaration'
            p[0] = PassUpNode("TranslationUnit", [ p[1] ])
            self.AST = p[0]
            if self.DebugProd == True:
                self.DebugPrint("translation_unit -->  external_declaration", p)
            return

        def p_translation_unit_2(p):
            'translation_unit :  translation_unit external_declaration'
            p[0] = PassUpNode("TranslationUnit", [p[1], p[2]])
            self.AST = p[0]
            if self.DebugProd == True:
                self.DebugPrint("translation_unit -->  translation_unit external_declaration", p)
            return

        def p_external_declaration_1(p):
            'external_declaration : insert_mode_e function_definition'
            p[0] = PassUpNode("ExternalDeclaration", [p[2]])
            if self.DebugProd == True:
                self.DebugPrint("external_declaration -->  function_definition", p)
            return

        def p_external_declaration_2(p):
            'external_declaration : insert_mode_e declaration'
            p[0] = PassUpNode("ExternalDeclaration", [p[2]])
            if self.DebugProd == True:
                self.DebugPrint("external_declaration -->  declaration", p)
            return

        def p_function_definition_1(p):
            'function_definition :  declarator compound_statement'
            p[0] = FunctionDefintion(Declarator = p[1], Statement = p[2], Production=p)
            if self.DebugProd == True:
                self.DebugPrint("function_definition -->  declarator compound_statement", p)
            return

        def p_function_definition_2(p):
            'function_definition :  declarator declaration_list compound_statement'
            p[0] = FunctionDefintion(Declarator = p[1], DeclarationList = p[2], Statement = p[3], Production=p)

            if self.DebugProd == True:
                self.DebugPrint("function_definition -->  declarator declaration_list compound_statement", p)
            return

        def p_function_definition_3(p):
            'function_definition :  declaration_specifiers declarator compound_statement'
            p[0] = FunctionDefintion(ReturnDeclarator = p[1], Declarator = p[2], Statement = p[3], Production=p)
            if self.DebugProd == True:
                self.DebugPrint("function_definition -->  declaration_specifiers declarator compound_statement", p)
            return

        def p_function_definition_4(p):
            'function_definition :  declaration_specifiers declarator declaration_list compound_statement'
            p[0] = FunctionDefintion(ReturnDeclarator = p[1], Declarator = p[2], DeclarationList = p[3], Statement = p[4], Production=p)

            if self.DebugProd == True:
                self.DebugPrint("function_definition -->  declaration_specifiers declarator declaration_list compound_statement", p)
            return

        def p_declaration_1(p):
            'declaration :  declaration_specifiers SEMI'
            p[0] = Declaration(Left=p[1])
            if self.DebugProd == True:
                self.DebugPrint("declaration -->  declaration_specifiers SEMI", p)
            return

        def p_declaration_2(p):
            'declaration :  declaration_specifiers init_declarator_list SEMI'
            p[0] = Declaration(Left=p[1], Right=p[2])

            if self.DebugProd == True:
                self.DebugPrint("declaration -->  declaration_specifiers init_declarator_list SEMI", p)
            return

        ##### GRAMMAR EXSTENSIONS #######

        def p_declaration_3(p):
            'declaration :  PD_O'
            self.DebugProd = True
            if self.DebugProd == True:
                self.DebugPrint("declaration -->  PD_O", p)
            return

        def p_declaration_4(p):
            'declaration :  PD_F'
            self.DebugProd = False
            if self.DebugProd == True:
                self.DebugPrint("declaration -->  PD_F", p)
            return

        ##### END GRAMMAR EXSTENSIONS #######

        def p_declaration_list_1(p):
            'declaration_list :  insert_mode_e declaration'
            p[0] = DeclList(Decl=p[2])
            if self.DebugProd == True:
                self.DebugPrint("declaration_list -->  declaration", p)
            return

        def p_declaration_list_2(p):
            'declaration_list :  declaration_list insert_mode_e declaration'
            p[0] = DeclList(DeclList=p[1], Decl=p[3])
            if self.DebugProd == True:
                self.DebugPrint("declaration_list -->  declaration_list declaration", p)
            return

        def p_declaration_specifiers_1(p):
            'declaration_specifiers :  storage_class_specifier'
            p[0] = DeclarationSpecifiers(SCSpec=p[1])
            if self.DebugProd == True:
                self.DebugPrint("declaration_specifiers -->  storage_class_specifier", p)
            return

        def p_declaration_specifiers_2(p):
            'declaration_specifiers :  storage_class_specifier declaration_specifiers'
            p[0] = DeclarationSpecifiers(SCSpec=p[1], DeclSpec=p[2])
            if self.DebugProd == True:
                self.DebugPrint("declaration_specifiers -->  storage_class_specifier declaration_specifiers", p)
            return

        def p_declaration_specifiers_3(p):
            'declaration_specifiers :  type_specifier'
            p[0] = DeclarationSpecifiers(TSpec=p[1])
            if self.DebugProd == True:
                self.DebugPrint("declaration_specifiers -->  type_specifier", p)
            return

        def p_declaration_specifiers_4(p):
            'declaration_specifiers :  type_specifier declaration_specifiers'
            p[0] = DeclarationSpecifiers(TSpec=p[1], DeclSpec=p[2])
            if self.DebugProd == True:
                self.DebugPrint("declaration_specifiers -->  type_specifier declaration_specifiers", p)
            return

        def p_declaration_specifiers_5(p):
            'declaration_specifiers :  type_qualifier'
            p[0] = DeclarationSpecifiers(TQual=p[1])
            if self.DebugProd == True:
                self.DebugPrint("declaration_specifiers -->  type_qualifier", p)
            return

        def p_declaration_specifiers_6(p):
            'declaration_specifiers :  type_qualifier declaration_specifiers'
            p[0] = DeclarationSpecifiers(TQual=p[1], DeclSpec=p[2])
            if self.DebugProd == True:
                self.DebugPrint("declaration_specifiers -->  type_qualifier declaration_specifiers", p)
            return

        def p_storage_class_specifier_1(p):
            'storage_class_specifier :  AUTO'
            p[0] = p[1]
            if self.DebugProd == True:
                self.DebugPrint("storage_class_specifier -->  AUTO", p)
            return

        def p_storage_class_specifier_2(p):
            'storage_class_specifier :  REGISTER'
            p[0] = p[1]
            if self.DebugProd == True:
                self.DebugPrint("storage_class_specifier -->  REGISTER", p)
            return

        def p_storage_class_specifier_3(p):
            'storage_class_specifier :  STATIC'
            p[0] = p[1]
            if self.DebugProd == True:
                self.DebugPrint("storage_class_specifier -->  STATIC", p)
            return

        def p_storage_class_specifier_4(p):
            'storage_class_specifier :  EXTERN'
            p[0] = p[1]
            if self.DebugProd == True:
                self.DebugPrint("storage_class_specifier -->  EXTERN", p)
            return

        def p_storage_class_specifier_5(p):
            'storage_class_specifier :  TYPEDEF'
            p[0] = p[1]
            if self.DebugProd == True:
                self.DebugPrint("storage_class_specifier -->  TYPEDEF", p)
            return

        def p_type_specifier_1(p):
            'type_specifier :  VOID'
            p[0] = p[1]

            if self.DebugProd == True:
                self.DebugPrint("type_specifier -->  VOID", p)
            return

        def p_type_specifier_2(p):
            'type_specifier :  CHAR'
            p[0] = p[1]

            if self.DebugProd == True:
                self.DebugPrint("type_specifier -->  CHAR", p)
            return

        def p_type_specifier_3(p):
            'type_specifier :  SHORT'
            p[0] = p[1]

            if self.DebugProd == True:
                self.DebugPrint("type_specifier -->  SHORT", p)
            return

        def p_type_specifier_4(p):
            'type_specifier :  INT'
            p[0] = p[1]

            if self.DebugProd == True:
                self.DebugPrint("type_specifier -->  INT", p)
            return

        def p_type_specifier_5(p):
            'type_specifier :  LONG'
            p[0] = p[1]

            if self.DebugProd == True:
                self.DebugPrint("type_specifier -->  LONG", p)
            return

        def p_type_specifier_6(p):
            'type_specifier :  FLOAT'
            p[0] = p[1]

            if self.DebugProd == True:
                self.DebugPrint("type_specifier -->  FLOAT", p)
            return

        def p_type_specifier_7(p):
            'type_specifier :  DOUBLE'
            p[0] = p[1]

            if self.DebugProd == True:
                self.DebugPrint("type_specifier -->  DOUBLE", p)
            return

        def p_type_specifier_8(p):
            'type_specifier :  SIGNED'
            p[0] = p[1]

            if self.DebugProd == True:
                self.DebugPrint("type_specifier -->  SIGNED", p)
            return

        def p_type_specifier_9(p):
            'type_specifier :  UNSIGNED'
            p[0] = p[1]

            if self.DebugProd == True:
                self.DebugPrint("type_specifier -->  UNSIGNED", p)
            return

        def p_type_specifier_10(p):
            'type_specifier :  struct_or_union_specifier'
            p[0] = p[1]

            if self.DebugProd == True:
                self.DebugPrint("type_specifier -->  struct_or_union_specifier", p)
            return

        def p_type_specifier_11(p):
            'type_specifier :  enum_specifier'
            p[0] = p[1]

            if self.DebugProd == True:
                self.DebugPrint("type_specifier -->  enum_specifier", p)
            return

        def p_type_specifier_12(p):
            'type_specifier :  TYPEDEF_NAME'
            p[0] = p[1]

            if self.DebugProd == True:
                self.DebugPrint("type_specifier -->  TYPEDEF_NAME", p)
            return

        def p_type_qualifier_1(p):
            'type_qualifier :  CONST'
            p[0] = p[1]

            if self.DebugProd == True:
                self.DebugPrint("type_qualifier -->  CONST", p)
            return

        def p_type_qualifier_2(p):
            'type_qualifier :  VOLATILE'
            p[0] = p[1]

            if self.DebugProd == True:
                self.DebugPrint("type_qualifier -->  VOLATILE", p)
            return

        def p_struct_or_union_specifier_1(p):
            'struct_or_union_specifier :  struct_or_union identifier OPENBRACE struct_declaration_list CLOSEBRACE'
            if self.DebugProd == True:
                self.DebugPrint("struct_or_union_specifier -->  struct_or_union identifier OPENBRACE struct_declaration_list CLOSEBRACE", p)
            return

        def p_struct_or_union_specifier_2(p):
            'struct_or_union_specifier :  struct_or_union OPENBRACE struct_declaration_list CLOSEBRACE'
            if self.DebugProd == True:
                self.DebugPrint("struct_or_union_specifier -->  struct_or_union OPENBRACE struct_declaration_list CLOSEBRACE", p)
            return

        def p_struct_or_union_specifier_3(p):
            'struct_or_union_specifier :  struct_or_union identifier'
            if self.DebugProd == True:
                self.DebugPrint("struct_or_union_specifier -->  struct_or_union identifier", p)
            return

        def p_struct_or_union_1(p):
            'struct_or_union :  STRUCT'
            p[0] = p[1]
            if self.DebugProd == True:
                self.DebugPrint("struct_or_union -->  STRUCT", p)
            return

        def p_struct_or_union_2(p):
            'struct_or_union :  UNION'
            p[0] = p[1]
            if self.DebugProd == True:
                self.DebugPrint("struct_or_union -->  UNION", p)
            return

        def p_struct_declaration_list_1(p):
            'struct_declaration_list :  struct_declaration'
            if self.DebugProd == True:
                self.DebugPrint("struct_declaration_list -->  struct_declaration", p)
            return

        def p_struct_declaration_list_2(p):
            'struct_declaration_list :  struct_declaration_list struct_declaration'
            if self.DebugProd == True:
                self.DebugPrint("struct_declaration_list -->  struct_declaration_list struct_declaration", p)
            return

        def p_init_declarator_list_1(p):
            'init_declarator_list :  init_declarator'
            p[0] = InitDeclList(Decl=p[1])

            if self.DebugProd == True:
                self.DebugPrint("init_declarator_list -->  init_declarator", p)
            return

        def p_init_declarator_list_2(p):
            'init_declarator_list :  init_declarator_list COMMA init_declarator'
            p[0] = InitDeclList(DeclList=p[1], Decl=p[3])


            if self.DebugProd == True:
                self.DebugPrint("init_declarator_list -->  init_declarator_list COMMA init_declarator", p)
            return


        def p_init_declarator_1(p):
            'init_declarator :  declarator'
            p[0] = p[1]

            if self.DebugProdL[1] == True:
                print(p[1])

            if self.DebugProd == True:
                self.DebugPrint("init_declarator -->  declarator", p)
            return

        def p_init_declarator_2(p):
            'init_declarator :  declarator ASSIGN initializer'
            if self.DebugProd == True:
                self.DebugPrint("init_declarator -->  declarator ASSIGN initializer", p)
            return

        def p_struct_declaration_1(p):
            'struct_declaration :  specifier_qualifier_list struct_declarator_list SEMI'
            if self.DebugProd == True:
                self.DebugPrint("struct_declaration -->  specifier_qualifier_list struct_declarator_list SEMI", p)
            return

        def p_specifier_qualifier_list_1(p):
            'specifier_qualifier_list :  type_specifier'
            if self.DebugProd == True:
                self.DebugPrint("specifier_qualifier_list -->  type_specifier", p)
            return

        def p_specifier_qualifier_list_2(p):
            'specifier_qualifier_list :  type_specifier specifier_qualifier_list'
            if self.DebugProd == True:
                self.DebugPrint("specifier_qualifier_list -->  type_specifier specifier_qualifier_list", p)
            return

        def p_specifier_qualifier_list_3(p):
            'specifier_qualifier_list :  type_qualifier'
            if self.DebugProd == True:
                self.DebugPrint("specifier_qualifier_list -->  type_qualifier", p)
            return

        def p_specifier_qualifier_list_4(p):
            'specifier_qualifier_list :  type_qualifier specifier_qualifier_list'
            if self.DebugProd == True:
                self.DebugPrint("specifier_qualifier_list -->  type_qualifier specifier_qualifier_list", p)
            return

        def p_struct_declarator_list_1(p):
            'struct_declarator_list :  struct_declarator'
            if self.DebugProd == True:
                self.DebugPrint("struct_declarator_list -->  struct_declarator", p)
            return

        def p_struct_declarator_list_2(p):
            'struct_declarator_list :  struct_declarator_list COMMA struct_declarator'
            if self.DebugProd == True:
                self.DebugPrint("struct_declarator_list -->  struct_declarator_list COMMA struct_declarator", p)
            return

        def p_struct_declarator_1(p):
            'struct_declarator :  declarator'
            if self.DebugProd == True:
                self.DebugPrint("struct_declarator -->  declarator", p)
            return

        def p_struct_declarator_2(p):
            'struct_declarator :  COLON constant_expression'
            if self.DebugProd == True:
                self.DebugPrint("struct_declarator -->  COLON constant_expression", p)
            return

        def p_struct_declarator_3(p):
            'struct_declarator :  declarator COLON constant_expression'
            if self.DebugProd == True:
                self.DebugPrint("struct_declarator -->  declarator COLON constant_expression", p)
            return

        def p_enum_specifier_1(p):
            'enum_specifier :  ENUM OPENBRACE enumerator_list CLOSEBRACE'
            if self.DebugProd == True:
                self.DebugPrint("enum_specifier -->  ENUM OPENBRACE enumerator_list CLOSEBRACE", p)
            return

        def p_enum_specifier_2(p):
            'enum_specifier :  ENUM identifier OPENBRACE enumerator_list CLOSEBRACE'
            if self.DebugProd == True:
                self.DebugPrint("enum_specifier -->  ENUM identifier OPENBRACE enumerator_list CLOSEBRACE", p)
            return

        def p_enum_specifier_3(p):
            'enum_specifier :  ENUM identifier'
            if self.DebugProd == True:
                self.DebugPrint("enum_specifier -->  ENUM identifier", p)
            return

        def p_enumerator_list_1(p):
            'enumerator_list :  enumerator'
            if self.DebugProd == True:
                self.DebugPrint("enumerator_list -->  enumerator", p)
            return

        def p_enumerator_list_2(p):
            'enumerator_list :  enumerator_list COMMA enumerator'
            if self.DebugProd == True:
                self.DebugPrint("enumerator_list -->  enumerator_list COMMA enumerator", p)
            return

        def p_enumerator_1(p):
            'enumerator :  identifier'
            if self.DebugProd == True:
                self.DebugPrint("enumerator -->  identifier", p)
            return

        def p_enumerator_2(p):
            'enumerator :  identifier ASSIGN constant_expression'
            if self.DebugProd == True:
                self.DebugPrint("enumerator -->  identifier ASSIGN constant_expression", p)
            return

        def p_declarator_1(p):
            'declarator : direct_declarator'
            #pass up the identifier
            p[0] = PassUpNode("Declarator", [p[1]])

            if self.DebugProd == True:
                self.DebugPrint("declarator -->  direct_declarator", p)
            return

        def p_declarator_2(p):
            'declarator : pointer direct_declarator'
            p[0] = PassUpNode("Declarator", [p[1],p[2]])

            if self.DebugProd == True:
                self.DebugPrint("declarator -->  pointer direct_declarator", p)
            return

        def p_direct_declarator_1(p):
            'direct_declarator :  identifier'
            p[0] = PassUpNode("DirectDeclarator", [p[1]])

            if self.DebugProd == True:
                self.DebugPrint("direct_declarator -->  identifier", p)
            return

        def p_direct_declarator_2(p):
            'direct_declarator :  OPENPAREN declarator CLOSEPAREN'
            p[0] = PassUpNode("DirectDeclarator", [p[2]])

            if self.DebugProd == True:
                self.DebugPrint("direct_declarator -->  OPENPAREN declarator CLOSEPAREN", p)
            return

##################Arrays and function declarations#####################
        def p_direct_declarator_3(p):
            'direct_declarator :  direct_declarator OPENBRACKET CLOSEBRACKET'
            p[0] = ArrayDeclaration(p[1], None, p)
            if self.DebugProd == True:
                self.DebugPrint("direct_declarator -->  direct_declarator OPENBRACKET CLOSEBRACKET", p)
            return

        def p_direct_declarator_4(p):
            'direct_declarator :  direct_declarator OPENBRACKET constant_expression CLOSEBRACKET'
            p[0] = ArrayDeclaration(p[1], p[3], p)
            if self.DebugProd == True:
                self.DebugPrint("direct_declarator -->  direct_declarator OPENBRACKET constant_expression CLOSEBRACKET", p)
            return

        def p_direct_declarator_5(p):
            'direct_declarator :  direct_declarator OPENPAREN CLOSEPAREN'
            p[0] = PassUpNode("DirectDeclarator", [p[1]])
            if self.DebugProd == True:
                self.DebugPrint("direct_declarator -->  direct_declarator OPENPAREN CLOSEPAREN", p)
            return

        def p_direct_declarator_6(p):
            'direct_declarator :  direct_declarator OPENPAREN parameter_type_list CLOSEPAREN'
            #this should assign some things as well
            p[0] = FunctionPrototype(DirectDeclarator=p[1], ParameterTypeList=p[3], Production=p)

            if self.DebugProd == True:
                self.DebugPrint("direct_declarator -->  direct_declarator OPENPAREN parameter_type_list CLOSEPAREN", p)
            return

        def p_direct_declarator_7(p):
            'direct_declarator :  direct_declarator OPENPAREN identifier_list CLOSEPAREN'
            p[0] = PassUpNode("DirectDeclarator", [p[1],p[3]])
            if self.DebugProd == True:
                self.DebugPrint("direct_declarator -->  direct_declarator OPENPAREN identifier_list CLOSEPAREN", p)
            return

        def p_pointer_1(p):
            'pointer :  ASTERISK'
            if self.DebugProd == True:
                self.DebugPrint("pointer -->  ASTERISK", p)
            return

        def p_pointer_2(p):
            'pointer :  ASTERISK type_qualifier_list'
            if self.DebugProd == True:
                self.DebugPrint("pointer -->  ASTERISK type_qualifier_list", p)
            return

        def p_pointer_3(p):
            'pointer :  ASTERISK pointer'
            if self.DebugProd == True:
                self.DebugPrint("pointer -->  ASTERISK pointer", p)
            return

        def p_pointer_4(p):
            'pointer :  ASTERISK type_qualifier_list pointer'
            if self.DebugProd == True:
                self.DebugPrint("pointer -->  ASTERISK type_qualifier_list pointer", p)
            return

        def p_type_qualifier_list_1(p):
            'type_qualifier_list :  type_qualifier'
            p[0] = PassUpNode("TypeQualifierList", [p[1]])
            if self.DebugProd == True:
                self.DebugPrint("type_qualifier_list -->  type_qualifier", p)
            return

        def p_type_qualifier_list_2(p):
            'type_qualifier_list :  type_qualifier_list type_qualifier'
            p[0] = PassUpNode("TypeQualifierList", [p[1],p[2]])
            if self.DebugProd == True:
                self.DebugPrint("type_qualifier_list -->  type_qualifier_list type_qualifier", p)
            return

        def p_parameter_type_list_1(p):
            'parameter_type_list :  parameter_list'
            p[0] = PassUpNode("ParameterTypeList", [p[1]])
            if self.DebugProd == True:
                self.DebugPrint("parameter_type_list -->  parameter_list", p)
            return

        def p_parameter_type_list_2(p):
            'parameter_type_list :  parameter_list COMMA ELIPSIS'
            p[0] = PassUpNode("ParameterTypeList", [p[1],p[3]])
            if self.DebugProd == True:
                self.DebugPrint("parameter_type_list -->  parameter_list COMMA ELIPSIS", p)
            return

        def p_parameter_list_1(p):
            'parameter_list :  parameter_declaration'
            p[0] = PassUpNode("ParameterList", [p[1]])
            if self.DebugProd == True:
                self.DebugPrint("parameter_list -->  parameter_declaration", p)
            return

        def p_parameter_list_2(p):
            'parameter_list :  parameter_list COMMA parameter_declaration'
            p[0] = PassUpNode("ParameterList", [p[1], p[3]])
            if self.DebugProd == True:
                self.DebugPrint("parameter_list -->  parameter_list COMMA parameter_declaration", p)
            return

        def p_parameter_declaration_1(p):
            'parameter_declaration :  declaration_specifiers declarator'
            p[0] = Declaration(p[1], p[2])
            if self.DebugProd == True:
                self.DebugPrint("parameter_declaration -->  declaration_specifiers declarator", p)
            return

        def p_parameter_declaration_2(p):
            'parameter_declaration :  declaration_specifiers'
            p[0] = PassUpNode("ParameterDeclaration", [p[1]])
            if self.DebugProd == True:
                self.DebugPrint("parameter_declaration -->  declaration_specifiers", p)
            return

        def p_parameter_declaration_3(p):
            'parameter_declaration :  declaration_specifiers abstract_declarator'
            p[0] = PassUpNode("ParameterDeclaration", [p[1], p[2]])
            if self.DebugProd == True:
                self.DebugPrint("parameter_declaration -->  declaration_specifiers abstract_declarator", p)
            return

        def p_identifier_list_1(p):
            'identifier_list :  identifier'
            if self.DebugProd == True:
                self.DebugPrint("identifier_list -->  identifier", p)
            return

        def p_identifier_list_2(p):
            'identifier_list :  identifier_list COMMA identifier'
            if self.DebugProd == True:
                self.DebugPrint("identifier_list -->  identifier_list COMMA identifier", p)
            return

        def p_initializer_1(p):
            'initializer :  assignment_expression'
            if self.DebugProd == True:
                self.DebugPrint("initializer -->  assignment_expression", p)
            return

        def p_initializer_2(p):
            'initializer :  OPENBRACE initializer_list CLOSEBRACE'
            if self.DebugProd == True:
                self.DebugPrint("initializer -->  OPENBRACE initializer_list CLOSEBRACE", p)
            return

        def p_initializer_3(p):
            'initializer :  OPENBRACE initializer_list COMMA CLOSEBRACE'
            if self.DebugProd == True:
                self.DebugPrint("initializer -->  OPENBRACE initializer_list COMMA CLOSEBRACE", p)
            return

        def p_initializer_list_1(p):
            'initializer_list :  initializer'
            if self.DebugProd == True:
                self.DebugPrint("initializer_list -->  initializer", p)
            return

        def p_initializer_list_2(p):
            'initializer_list :  initializer_list COMMA initializer'
            if self.DebugProd == True:
                self.DebugPrint("initializer_list -->  initializer_list COMMA initializer", p)
            return

        def p_type_name_1(p):
            'type_name :  specifier_qualifier_list'
            if self.DebugProd == True:
                self.DebugPrint("type_name -->  specifier_qualifier_list", p)
            return

        def p_type_name_2(p):
            'type_name :  specifier_qualifier_list abstract_declarator'
            if self.DebugProd == True:
                self.DebugPrint("type_name -->  specifier_qualifier_list abstract_declarator", p)
            return

        def p_abstract_declarator_1(p):
            'abstract_declarator :  pointer'
            if self.DebugProd == True:
                self.DebugPrint("abstract_declarator -->  pointer", p)
            return

        def p_abstract_declarator_2(p):
            'abstract_declarator :  direct_abstract_declarator'
            p[0] = PassUpNode("AbstractDeclarator", [p[1]])
            if self.DebugProd == True:
                self.DebugPrint("abstract_declarator -->  direct_abstract_declarator", p)
            return

        def p_abstract_declarator_3(p):
            'abstract_declarator :  pointer direct_abstract_declarator'
            if self.DebugProd == True:
                self.DebugPrint("abstract_declarator -->  pointer direct_abstract_declarator", p)
            return

        def p_direct_abstract_declarator_1(p):
            'direct_abstract_declarator :  OPENPAREN abstract_declarator CLOSEPAREN'
            if self.DebugProd == True:
                self.DebugPrint("direct_abstract_declarator -->  OPENPAREN abstract_declarator CLOSEPAREN", p)
            return

        def p_direct_abstract_declarator_2(p):
            'direct_abstract_declarator :  OPENBRACKET CLOSEBRACKET'
            p[0] = PassUpNode("DirectAbstractDeclarator", [])
            if self.DebugProd == True:
                self.DebugPrint("direct_abstract_declarator -->  OPENBRACKET CLOSEBRACKET", p)
            return

        def p_direct_abstract_declarator_3(p):
            'direct_abstract_declarator :  OPENBRACKET constant_expression CLOSEBRACKET'
            p[0] = PassUpNode("DirectAbstractDeclarator", [p[2]])
            if self.DebugProd == True:
                self.DebugPrint("direct_abstract_declarator -->  OPENBRACKET constant_expression CLOSEBRACKET", p)
            return

        def p_direct_abstract_declarator_4(p):
            'direct_abstract_declarator :  direct_abstract_declarator OPENBRACKET CLOSEBRACKET'
            p[0] = PassUpNode("DirectAbstractDeclarator", [p[1]])
            if self.DebugProd == True:
                self.DebugPrint("direct_abstract_declarator -->  direct_abstract_declarator OPENBRACKET CLOSEBRACKET", p)
            return

        def p_direct_abstract_declarator_5(p):
            'direct_abstract_declarator :  direct_abstract_declarator OPENBRACKET constant_expression CLOSEBRACKET'
            p[0] = PassUpNode("DirectAbstractDeclarator", [p[1], p[3]])
            if self.DebugProd == True:
                self.DebugPrint("direct_abstract_declarator -->  direct_abstract_declarator OPENBRACKET constant_expression CLOSEBRACKET", p)
            return

        def p_direct_abstract_declarator_6(p):
            'direct_abstract_declarator :  OPENPAREN CLOSEPAREN'
            if self.DebugProd == True:
                self.DebugPrint("direct_abstract_declarator -->  OPENPAREN CLOSEPAREN", p)
            return

        def p_direct_abstract_declarator_7(p):
            'direct_abstract_declarator :  OPENPAREN parameter_type_list CLOSEPAREN'
            if self.DebugProd == True:
                self.DebugPrint("direct_abstract_declarator -->  OPENPAREN parameter_type_list CLOSEPAREN", p)
            return

        def p_direct_abstract_declarator_8(p):
            'direct_abstract_declarator :  direct_abstract_declarator OPENPAREN CLOSEPAREN'
            if self.DebugProd == True:
                self.DebugPrint("direct_abstract_declarator -->  direct_abstract_declarator OPENPAREN CLOSEPAREN", p)
            return

        def p_direct_abstract_declarator_9(p):
            'direct_abstract_declarator :  direct_abstract_declarator OPENPAREN parameter_type_list CLOSEPAREN'
            if self.DebugProd == True:
                self.DebugPrint("direct_abstract_declarator -->  direct_abstract_declarator OPENPAREN parameter_type_list CLOSEPAREN", p)
            return

        def p_statement_1(p):
            'statement :  labeled_statement'
            p[0] = PassUpNode("Statement", [p[1]])
            if self.DebugProd == True:
                self.DebugPrint("statement -->  labeled_statement", p)
            return

        def p_statement_2(p):
            'statement :  compound_statement'
            p[0] = PassUpNode("Statement", [p[1]])
            if self.DebugProd == True:
                self.DebugPrint("statement -->  compound_statement", p)
            return

        def p_statement_3(p):
            'statement :  expression_statement'
            p[0] = PassUpNode("Statement", [p[1]])
            if self.DebugProd == True:
                self.DebugPrint("statement -->  expression_statement", p)
            return

        def p_statement_4(p):
            'statement :  selection_statement'
            p[0] = PassUpNode("Statement", [p[1]])
            if self.DebugProd == True:
                self.DebugPrint("statement -->  selection_statement", p)
            return

        def p_statement_5(p):
            'statement :  iteration_statement'
            p[0] = PassUpNode("Statement", [p[1]])
            if self.DebugProd == True:
                self.DebugPrint("statement -->  iteration_statement", p)
            return

        def p_statement_6(p):
            'statement :  jump_statement'
            p[0] = PassUpNode("Statement", [p[1]])
            if self.DebugProd == True:
                self.DebugPrint("statement -->  jump_statement", p)
            return

        def p_statement_7(p):
            'statement : PD_O'
            self.DebugProd = True
            if self.DebugProd == True:
                self.DebugPrint("statement -->  PD_O", p)
            return

        def p_statement_8(p):
            'statement : PD_F'
            self.DebugProd = False
            if self.DebugProd == True:
                self.DebugPrint("statement -->  PD_F", p)
            return

        def p_labeled_statement_1(p):
            'labeled_statement :  identifier COLON statement'
            if self.DebugProd == True:
                self.DebugPrint("labeled_statement -->  identifier COLON statement", p)
            return

        def p_labeled_statement_2(p):
            'labeled_statement :  CASE constant_expression COLON statement'
            if self.DebugProd == True:
                self.DebugPrint("labeled_statement -->  CASE constant_expression COLON statement", p)
            return

        def p_labeled_statement_3(p):
            'labeled_statement :  DEFAULT COLON statement'
            if self.DebugProd == True:
                self.DebugPrint("labeled_statement -->  DEFAULT COLON statement", p)
            return

        def p_expression_statement_1(p):
            'expression_statement :  SEMI'
            if self.DebugProd == True:
                self.DebugPrint("expression_statement -->  SEMI", p)
            return

        def p_expression_statement_2(p):
            'expression_statement :  expression SEMI'
            p[0] = p[1]
            if self.DebugProd == True:
                self.DebugPrint("expression_statement -->  expression SEMI", p)
            return

        def p_compound_statement_1(p):
            'compound_statement :  OPENBRACE CLOSEBRACE'
            p[0] = CompoundStatement()
            if self.DebugProd == True:
                self.DebugPrint("compound_statement -->  OPENBRACE CLOSEBRACE", p)
            return

        def p_compound_statement_2(p):
            'compound_statement :  OPENBRACE push_scope_e statement_list pop_scope_e CLOSEBRACE'
            p[0] = CompoundStatement(StmtList=p[3])
            if self.DebugProd == True:
                self.DebugPrint("compound_statement -->  OPENBRACE statement_list CLOSEBRACE", p)
            return

        def p_compound_statement_3(p):
            'compound_statement :  OPENBRACE push_scope_e declaration_list pop_scope_e CLOSEBRACE'
            p[0] = CompoundStatement(DecList=p[3])
            if self.DebugProd == True:
                self.DebugPrint("compound_statement -->  OPENBRACE declaration_list CLOSEBRACE", p)
            return

        def p_compound_statement_4(p):
            'compound_statement :  OPENBRACE push_scope_e declaration_list statement_list insert_mode_e pop_scope_e CLOSEBRACE'
            p[0] = CompoundStatement(DecList=p[3], StmtList=p[4])
            if self.DebugProd == True:
                self.DebugPrint("compound_statement -->  OPENBRACE declaration_list statement_list CLOSEBRACE", p)
            return

        def p_statement_list_1(p):
            'statement_list : read_mode_e statement'
            p[0] = PassUpNode("StatementList", [p[2]])
            if self.DebugProd == True:
                self.DebugPrint("statement_list -->  statement", p)
            return

        def p_statement_list_2(p):
            'statement_list :  statement_list read_mode_e statement'
            p[0] = PassUpNode("StatementList", [p[1], p[3]])
            if self.DebugProd == True:
                self.DebugPrint("statement_list -->  statement_list statement", p)
            return

        def p_selection_statement_1(p):
            'selection_statement :  IF OPENPAREN expression CLOSEPAREN statement'

            p[0] = SelectionStatement(IfExpression=p[3], ThenBlock=p[5])

            if self.DebugProd == True:
                self.DebugPrint("selection_statement -->  IF OPENPAREN expression CLOSEPAREN statement", p)
            return

        def p_selection_statement_2(p):
            'selection_statement :  IF OPENPAREN expression CLOSEPAREN statement ELSE statement'

            p[0] = SelectionStatement(IfExpression=p[3], ThenBlock=p[5], ElseBlock=p[7])

            if self.DebugProd == True:
                self.DebugPrint("selection_statement -->  IF OPENPAREN expression CLOSEPAREN statement ELSE statement", p)
            return

        def p_selection_statement_3(p):
            'selection_statement :  SWITCH OPENPAREN expression CLOSEPAREN statement'
            if self.DebugProd == True:
                self.DebugPrint("selection_statement -->  SWITCH OPENPAREN expression CLOSEPAREN statement", p)
            return

        def p_iteration_statement_1(p):
            'iteration_statement :  WHILE OPENPAREN expression CLOSEPAREN statement'
            p[0] = IterationStatement(ConditionalExpression = p[3], Statement = p[5], Production = p)
            if self.DebugProd == True:
                self.DebugPrint("iteration_statement -->  WHILE OPENPAREN expression CLOSEPAREN statement", p)
            return

        def p_iteration_statement_2(p):
            'iteration_statement :  DO statement WHILE OPENPAREN expression CLOSEPAREN SEMI'
            p[0] = IterationStatement(ConditionalExpression = p[5], Statement = p[2], Production = p)
            if self.DebugProd == True:
                self.DebugPrint("iteration_statement -->  DO statement WHILE OPENPAREN expression CLOSEPAREN SEMI", p)
            return

        def p_iteration_statement_3(p):
            'iteration_statement :  FOR OPENPAREN SEMI SEMI CLOSEPAREN statement'
            p[0] = IterationStatement(Statement = p[6], Production = p)
            if self.DebugProd == True:
                self.DebugPrint("iteration_statement -->  FOR OPENPAREN SEMI SEMI CLOSEPAREN statement", p)
            return

        def p_iteration_statement_4(p):
            'iteration_statement :  FOR OPENPAREN SEMI SEMI expression CLOSEPAREN statement'
            p[0] = IterationStatement(IterativeExpression = p[5], Statement = p[7], Production = p)
            if self.DebugProd == True:
                self.DebugPrint("iteration_statement -->  FOR OPENPAREN SEMI SEMI expression CLOSEPAREN statement", p)
            return

        def p_iteration_statement_5(p):
            'iteration_statement :  FOR OPENPAREN SEMI expression SEMI CLOSEPAREN statement'
            p[0] = IterationStatement(ConditionalExpression = p[4], Statement = p[7], Production = p)
            if self.DebugProd == True:
                self.DebugPrint("iteration_statement -->  FOR OPENPAREN SEMI expression SEMI CLOSEPAREN statement", p)
            return

        def p_iteration_statement_6(p):
            'iteration_statement :  FOR OPENPAREN SEMI expression SEMI expression CLOSEPAREN statement'
            p[0] = IterationStatement(ConditionalExpression = p[4], IterativeExpression = p[6], Statement = p[8], Production = p)
            if self.DebugProd == True:
                self.DebugPrint("iteration_statement -->  FOR OPENPAREN SEMI expression SEMI expression CLOSEPAREN statement", p)
            return

        def p_iteration_statement_7(p):
            'iteration_statement :  FOR OPENPAREN expression SEMI SEMI CLOSEPAREN statement'
            p[0] = IterationStatement(AssignmentExpression = p[3], Statement = p[7], Production = p)
            if self.DebugProd == True:
                self.DebugPrint("iteration_statement -->  FOR OPENPAREN expression SEMI SEMI CLOSEPAREN statement", p)
            return

        def p_iteration_statement_8(p):
            'iteration_statement :  FOR OPENPAREN expression SEMI SEMI expression CLOSEPAREN statement'
            p[0] = IterationStatement(AssignmentExpression = p[3], IterativeExpression = p[6], Statement = p[8], Production = p)
            if self.DebugProd == True:
                self.DebugPrint("iteration_statement -->  FOR OPENPAREN expression SEMI SEMI expression CLOSEPAREN statement", p)
            return

        def p_iteration_statement_9(p):
            'iteration_statement :  FOR OPENPAREN expression SEMI expression SEMI CLOSEPAREN statement'
            p[0] = IterationStatement(AssignmentExpression = p[3], ConditionalExpression = p[5], Statement = p[8], Production = p)
            if self.DebugProd == True:
                self.DebugPrint("iteration_statement -->  FOR OPENPAREN expression SEMI expression SEMI CLOSEPAREN statement", p)
            return

        def p_iteration_statement_10(p):
            'iteration_statement :  FOR OPENPAREN expression SEMI expression SEMI expression CLOSEPAREN statement'
            p[0] = IterationStatement(AssignmentExpression = p[3], ConditionalExpression = p[5], IterativeExpression = p[7], Statement = p[9], Production = p)
            if self.DebugProd == True:
                self.DebugPrint("iteration_statement -->  FOR OPENPAREN expression SEMI expression SEMI expression CLOSEPAREN statement", p)
            return

        def p_jump_statement_1(p):
            'jump_statement :  GOTO identifier SEMI'
            if self.DebugProd == True:
                self.DebugPrint("jump_statement -->  GOTO identifier SEMI", p)
            return

        def p_jump_statement_2(p):
            'jump_statement :  CONTINUE SEMI'
            if self.DebugProd == True:
                self.DebugPrint("jump_statement -->  CONTINUE SEMI", p)
            return

        def p_jump_statement_3(p):
            'jump_statement :  BREAK SEMI'
            if self.DebugProd == True:
                self.DebugPrint("jump_statement -->  BREAK SEMI", p)
            return

        def p_jump_statement_4(p):
            'jump_statement :  RETURN SEMI'
            p[0] = PassUpNode("JumpStatement", [p[1]])
            if self.DebugProd == True:
                self.DebugPrint("jump_statement -->  RETURN SEMI", p)
            return

        def p_jump_statement_5(p):
            'jump_statement :  RETURN expression SEMI'
            p[0] = PassUpNode("JumpStatement", [p[1], p[2]])
            if self.DebugProd == True:
                self.DebugPrint("jump_statement -->  RETURN expression SEMI", p)
            return

        def p_expression_1(p):
            'expression :  assignment_expression'
            p[0] = PassUpNode("Expression", [p[1]])
            if self.DebugProd == True:
                self.DebugPrint("expression -->  assignment_expression", p)
            return

        def p_expression_2(p):
            'expression :  expression COMMA assignment_expression'
            p[0] = PassUpNode("Expression", [p[1],p[3]])
            if self.DebugProd == True:
                self.DebugPrint("expression -->  expression COMMA assignment_expression", p)
            return

        def p_assignment_expression_1(p):
            'assignment_expression :  conditional_expression'
            p[0] = PassUpNode("AssignmentExpression", [p[1]])
            if self.DebugProd == True:
                self.DebugPrint("assignment_expression -->  conditional_expression", p)
            return

        def p_assignment_expression_2(p):
            'assignment_expression :  unary_expression assignment_operator assignment_expression'
            # this should be a binary operation
            p[0] = AssignmentExpression(p[2], p[1], p[3], self.ST, Production = p)
            if self.DebugProd == True:
                self.DebugPrint("assignment_expression -->  unary_expression assignment_operator assignment_expression", p)
            return

        #Assignment operators are only leaves that need to be passed up
        #The corresponding assignment operator can be treated as a leaf
        def p_assignment_operator_1(p):
            'assignment_operator :  ASSIGN'
            p[0] = p[1]
            if self.DebugProd == True:
                self.DebugPrint("assignment_operator -->  ASSIGN", p)
            return

        def p_assignment_operator_2(p):
            'assignment_operator :  MUL_ASSIGN'
            p[0] = p[1]
            if self.DebugProd == True:
                self.DebugPrint("assignment_operator -->  MUL_ASSIGN", p)
            return

        def p_assignment_operator_3(p):
            'assignment_operator :  DIV_ASSIGN'
            p[0] = p[1]
            if self.DebugProd == True:
                self.DebugPrint("assignment_operator -->  DIV_ASSIGN", p)
            return

        def p_assignment_operator_4(p):
            'assignment_operator :  MOD_ASSIGN'
            p[0] = p[1]
            if self.DebugProd == True:
                self.DebugPrint("assignment_operator -->  MOD_ASSIGN", p)
            return

        def p_assignment_operator_5(p):
            'assignment_operator :  ADD_ASSIGN'
            p[0] = p[1]
            if self.DebugProd == True:
                self.DebugPrint("assignment_operator -->  ADD_ASSIGN", p)
            return

        def p_assignment_operator_6(p):
            'assignment_operator :  SUB_ASSIGN'
            p[0] = p[1]
            if self.DebugProd == True:
                self.DebugPrint("assignment_operator -->  SUB_ASSIGN", p)
            return

        def p_assignment_operator_7(p):
            'assignment_operator :  LEFT_ASSIGN'
            if self.DebugProd == True:
                self.DebugPrint("assignment_operator -->  LEFT_ASSIGN", p)
            return

        def p_assignment_operator_8(p):
            'assignment_operator :  RIGHT_ASSIGN'
            p[0] = p[1]
            if self.DebugProd == True:
                self.DebugPrint("assignment_operator -->  RIGHT_ASSIGN", p)
            return

        def p_assignment_operator_9(p):
            'assignment_operator :  AND_ASSIGN'
            p[0] = p[1]
            if self.DebugProd == True:
                self.DebugPrint("assignment_operator -->  AND_ASSIGN", p)
            return

        def p_assignment_operator_10(p):
            'assignment_operator :  XOR_ASSIGN'
            p[0] = p[1]
            if self.DebugProd == True:
                self.DebugPrint("assignment_operator -->  XOR_ASSIGN", p)
            return

        def p_assignment_operator_11(p):
            'assignment_operator :  OR_ASSIGN'
            p[0] = p[1]
            if self.DebugProd == True:
                self.DebugPrint("assignment_operator -->  OR_ASSIGN", p)
            return

        def p_conditional_expression_1(p):
            'conditional_expression :  logical_or_expression'
            p[0] = PassUpNode("ConditionalExpression",[p[1]])
            if self.DebugProd == True:
                self.DebugPrint("conditional_expression -->  logical_or_expression", p)
            return

        def p_conditional_expression_2(p):
            'conditional_expression :  logical_or_expression QMARK expression COLON conditional_expression'
            if self.DebugProd == True:
                self.DebugPrint("conditional_expression -->  logical_or_expression QMARK expression COLON conditional_expression", p)
            return

        def p_constant_expression_1(p):
            'constant_expression :  conditional_expression'
            p[0] = PassUpNode("ConstantExpression",[p[1]])
            if self.DebugProd == True:
                self.DebugPrint("constant_expression -->  conditional_expression", p)
            return

        def p_logical_or_expression_1(p):
            'logical_or_expression :  logical_and_expression'
            p[0] = PassUpNode("LogicalOrExpression",[p[1]])
            if self.DebugProd == True:
                self.DebugPrint("logical_or_expression -->  logical_and_expression", p)
            return

        def p_logical_or_expression_2(p):
            'logical_or_expression :  logical_or_expression OR_OP logical_and_expression'
            p[0] = BinOp(Op=p[2], Left=p[1], Right=p[3], Production=p)
            if self.DebugProd == True:
                self.DebugPrint("logical_or_expression -->  logical_or_expression OR_OP logical_and_expression", p)
            return

        def p_logical_and_expression_1(p):
            'logical_and_expression :  inclusive_or_expression'
            p[0] = PassUpNode("LogicalAndExpression",[p[1]])
            if self.DebugProd == True:
                self.DebugPrint("logical_and_expression -->  inclusive_or_expression", p)
            return

        def p_logical_and_expression_2(p):
            'logical_and_expression :  logical_and_expression AND_OP inclusive_or_expression'
            p[0] = BinOp(Op=p[2], Left=p[1], Right=p[3], Production=p)
            if self.DebugProd == True:
                self.DebugPrint("logical_and_expression -->  logical_and_expression AND_OP inclusive_or_expression", p)
            return

        def p_inclusive_or_expression_1(p):
            'inclusive_or_expression :  exclusive_or_expression'
            p[0] = PassUpNode("InclusiveOrExpression",[p[1]])
            if self.DebugProd == True:
                self.DebugPrint("inclusive_or_expression -->  exclusive_or_expression", p)
            return

        def p_inclusive_or_expression_2(p):
            'inclusive_or_expression :  inclusive_or_expression PIPE exclusive_or_expression'
            p[0] = BinOp(Op=p[2], Left=p[1], Right=p[3], Production=p)
            if self.DebugProd == True:
                self.DebugPrint("inclusive_or_expression -->  inclusive_or_expression PIPE exclusive_or_expression", p)
            return

        def p_exclusive_or_expression_1(p):
            'exclusive_or_expression :  and_expression'
            p[0] = PassUpNode("ExclusiveOrExpression",[p[1]])
            if self.DebugProd == True:
                self.DebugPrint("exclusive_or_expression -->  and_expression", p)
            return

        def p_exclusive_or_expression_2(p):
            'exclusive_or_expression :  exclusive_or_expression CARAT and_expression'
            p[0] = BinOp(Op=p[2], Left=p[1], Right=p[3], Production=p)
            if self.DebugProd == True:
                self.DebugPrint("exclusive_or_expression -->  exclusive_or_expression CARAT and_expression", p)
            return

        def p_and_expression_1(p):
            'and_expression :  equality_expression'
            p[0] = PassUpNode("AndExpression",[p[1]])
            if self.DebugProd == True:
                self.DebugPrint("and_expression -->  equality_expression", p)
            return

        def p_and_expression_2(p):
            'and_expression :  and_expression AMPERSAND equality_expression'
            p[0] = BinOp(Op=p[2], Left=p[1], Right=p[3], Production=p)
            if self.DebugProd == True:
                self.DebugPrint("and_expression -->  and_expression AMPERSAND equality_expression", p)
            return

        def p_equality_expression_1(p):
            'equality_expression :  relational_expression'
            p[0] = PassUpNode("EqalityExpression",[p[1]])
            if self.DebugProd == True:
                self.DebugPrint("equality_expression -->  relational_expression", p)
            return

        def p_equality_expression_2(p):
            'equality_expression :  equality_expression EQ_OP relational_expression'
            p[0] = BinOp(Op=p[2], Left=p[1], Right=p[3], Production=p)
            if self.DebugProd == True:
                self.DebugPrint("equality_expression -->  equality_expression EQ_OP relational_expression", p)
            return

        def p_equality_expression_3(p):
            'equality_expression :  equality_expression NE_OP relational_expression'
            p[0] = BinOp(Op=p[2], Left=p[1], Right=p[3], Production=p)
            if self.DebugProd == True:
                self.DebugPrint("equality_expression -->  equality_expression NE_OP relational_expression", p)
            return

        def p_relational_expression_1(p):
            'relational_expression :  shift_expression'
            p[0] = PassUpNode("ShiftExpression",[p[1]])
            if self.DebugProd == True:
                self.DebugPrint("relational_expression -->  shift_expression", p)
            return

        def p_relational_expression_2(p):
            'relational_expression :  relational_expression LE shift_expression'
            p[0] = BinOp(Op=p[2], Left=p[1], Right=p[3], Production=p)
            if self.DebugProd == True:
                self.DebugPrint("relational_expression -->  relational_expression LE shift_expression", p)
            return

        def p_relational_expression_3(p):
            'relational_expression :  relational_expression GT shift_expression'
            p[0] = BinOp(Op=p[2], Left=p[1], Right=p[3], Production=p)
            if self.DebugProd == True:
                self.DebugPrint("relational_expression -->  relational_expression GT shift_expression", p)
            return

        def p_relational_expression_4(p):
            'relational_expression :  relational_expression LE_OP shift_expression'
            p[0] = BinOp(Op=p[2], Left=p[1], Right=p[3], Production=p)
            if self.DebugProd == True:
                self.DebugPrint("relational_expression -->  relational_expression LE_OP shift_expression", p)
            return

        def p_relational_expression_5(p):
            'relational_expression :  relational_expression GE_OP shift_expression'
            p[0] = BinOp(Op=p[2], Left=p[1], Right=p[3], Production=p)
            if self.DebugProd == True:
                self.DebugPrint("relational_expression -->  relational_expression GE_OP shift_expression", p)
            return

        def p_shift_expression_1(p):
            'shift_expression :  additive_expression'
            p[0] = PassUpNode("ShiftExpression",[p[1]])
            if self.DebugProd == True:
                self.DebugPrint("shift_expression -->  additive_expression", p)
            return

        def p_shift_expression_2(p):
            'shift_expression :  shift_expression LEFT_OP additive_expression'
            p[0] = BinOp(Op=p[2], Left=p[1], Right=p[3], Production=p)
            if self.DebugProd == True:
                self.DebugPrint("shift_expression -->  shift_expression LEFT_OP additive_expression", p)
            return

        def p_shift_expression_3(p):
            'shift_expression :  shift_expression RIGHT_OP additive_expression'
            p[0] = BinOp(Op=p[2], Left=p[1], Right=p[3], Production=p)
            if self.DebugProd == True:
                self.DebugPrint("shift_expression -->  shift_expression RIGHT_OP additive_expression", p)
            return

        def p_additive_expression_1(p):
            'additive_expression :  multiplicative_expression'
            p[0] = PassUpNode("AdditiveExpression",[p[1]])
            if self.DebugProd == True:
                self.DebugPrint("additive_expression -->  multiplicative_expression", p)
            return

        def p_additive_expression_2(p):
            'additive_expression :  additive_expression PLUS multiplicative_expression'
            p[0] = BinOp(Op=p[2], Left=p[1], Right=p[3], Production=p)
            if self.DebugProd == True:
                self.DebugPrint("additive_expression -->  additive_expression PLUS multiplicative_expression", p)
            return

        def p_additive_expression_3(p):
            'additive_expression :  additive_expression MINUS multiplicative_expression'
            p[0] = BinOp(Op=p[2], Left=p[1], Right=p[3], Production=p)
            if self.DebugProd == True:
                self.DebugPrint("additive_expression -->  additive_expression MINUS multiplicative_expression", p)
            return

        def p_multiplicative_expression_1(p):
            'multiplicative_expression :  cast_expression'
            p[0] = PassUpNode("MultiplicativeExpression",[p[1]])

            if self.DebugProd == True:
                self.DebugPrint("multiplicative_expression -->  cast_expression", p)
            return

        def p_multiplicative_expression_2(p):
            'multiplicative_expression :  multiplicative_expression ASTERISK cast_expression'
            p[0] = BinOp(Op=p[2], Left=p[1], Right=p[3], Production=p)
            if self.DebugProd == True:
                self.DebugPrint("multiplicative_expression -->  multiplicative_expression ASTERISK cast_expression", p)
            return

        def p_multiplicative_expression_3(p):
            'multiplicative_expression :  multiplicative_expression DIV cast_expression'
            p[0] = BinOp(Op=p[2], Left=p[1], Right=p[3], Production=p)
            if self.DebugProd == True:
                self.DebugPrint("multiplicative_expression -->  multiplicative_expression DIV cast_expression", p)
            return

        def p_multiplicative_expression_4(p):
            'multiplicative_expression :  multiplicative_expression PERCENT cast_expression'
            p[0] = BinOp(Op=p[2], Left=p[1], Right=p[3], Production=p)
            if self.DebugProd == True:
                self.DebugPrint("multiplicative_expression -->  multiplicative_expression PERCENT cast_expression", p)
            return

        def p_cast_expression_1(p):
            'cast_expression :  unary_expression'
            p[0] = PassUpNode("CastExpression",[p[1]])
            if self.DebugProd == True:
                self.DebugPrint("cast_expression -->  unary_expression", p)
            return

        def p_cast_expression_2(p):
            'cast_expression :  OPENPAREN type_name CLOSEPAREN cast_expression'
            if self.DebugProd == True:
                self.DebugPrint("cast_expression -->  OPENPAREN type_name CLOSEPAREN cast_expression", p)
            return


        def p_unary_expression_1(p):
            'unary_expression :  postfix_expression'
            p[0] = PassUpNode("UnaryExpression",[p[1]])

            if self.DebugProd == True:
                self.DebugPrint("unary_expression -->  postfix_expression", p)
            return

        def p_unary_expression_2(p):
            'unary_expression :  INC_OP unary_expression'

            p[0] = UnaryExpression(p[1], p[2], Loc=(p.lexer.lineno, p.lexer.lexpos))

            if self.DebugProd == True:
                self.DebugPrint("unary_expression -->  INC_OP unary_expression", p)
            return

        def p_unary_expression_3(p):
            'unary_expression :  DEC_OP unary_expression'
            p[0] = UnaryExpression(p[1], p[2], Loc=(p.lexer.lineno, p.lexer.lexpos))

            if self.DebugProd == True:
                self.DebugPrint("unary_expression -->  DEC_OP unary_expression", p)
            return

        def p_unary_expression_4(p):
            'unary_expression :  unary_operator cast_expression'

            if self.DebugProd == True:
                self.DebugPrint("unary_expression -->  unary_operator cast_expression", p)
            return

        def p_unary_expression_5(p):
            'unary_expression :  SIZEOF unary_expression'

            if self.DebugProd == True:
                self.DebugPrint("unary_expression -->  SIZEOF unary_expression", p)
            return

        def p_unary_expression_6(p):
            'unary_expression :  SIZEOF OPENPAREN type_name CLOSEPAREN'

            if self.DebugProd == True:
                self.DebugPrint("unary_expression -->  SIZEOF OPENPAREN type_name CLOSEPAREN", p)
            return


        #Unary Operators need only to be passed up. No need to create a node yet
        def p_unary_operator_1(p):
            'unary_operator :  AMPERSAND'
            p[0] = p[1]

            if self.DebugProd == True:
                self.DebugPrint("unary_operator -->  AMPERSAND", p)
            return

        def p_unary_operator_2(p):
            'unary_operator :  ASTERISK'
            p[0] = p[1]

            if self.DebugProd == True:
                self.DebugPrint("unary_operator -->  ASTERISK", p)
            return

        def p_unary_operator_3(p):
            'unary_operator :  PLUS'
            p[0] = p[1]

            if self.DebugProd == True:
                self.DebugPrint("unary_operator -->  PLUS", p)
            return

        def p_unary_operator_4(p):
            'unary_operator :  MINUS'
            p[0] = p[1]

            if self.DebugProd == True:
                self.DebugPrint("unary_operator -->  MINUS", p)
            return

        def p_unary_operator_5(p):
            'unary_operator :  TILDE'
            p[0] = p[1]

            if self.DebugProd == True:
                self.DebugPrint("unary_operator -->  TILDE", p)
            return

        def p_unary_operator_6(p):
            'unary_operator :  BANG'
            p[0] = p[1]

            if self.DebugProd == True:
                self.DebugPrint("unary_operator -->  BANG", p)
            return

        #This is array access and function calls, will definately need to modify
        def p_postfix_expression_1(p):
            'postfix_expression :  primary_expression'
            p[0] = PassUpNode("PostfixExpression",[p[1]])
            if self.DebugProd == True:
                self.DebugPrint("postfix_expression -->  primary_expression", p)
            return

        def p_postfix_expression_2(p):
            'postfix_expression :  postfix_expression OPENBRACKET expression CLOSEBRACKET'
            p[0] = ArrayAccess(ArrayName=p[1], ArrayOffset=p[3])
            if self.DebugProd == True:
                self.DebugPrint("postfix_expression -->  postfix_expression OPENBRACKET expression CLOSEBRACKET", p)
            return

        def p_postfix_expression_3(p):
            'postfix_expression :  postfix_expression OPENPAREN CLOSEPAREN'
            p[0] = FunctionCall(IdentifierSubtree=p[1], Production=p, ST=self.ST)
            if self.DebugProd == True:
                self.DebugPrint("postfix_expression -->  postfix_expression OPENPAREN CLOSEPAREN", p)
            return

        def p_postfix_expression_4(p):
            'postfix_expression :  postfix_expression OPENPAREN argument_expression_list CLOSEPAREN'
            p[0] = FunctionCall(p[1], p[3], p, self.ST)
            if self.DebugProd == True:
                self.DebugPrint("postfix_expression -->  postfix_expression OPENPAREN argument_expression_list CLOSEPAREN", p)
            return

        def p_postfix_expression_5(p):
            'postfix_expression :  postfix_expression PERIOD identifier'
            if self.DebugProd == True:
                self.DebugPrint("postfix_expression -->  postfix_expression PERIOD identifier", p)
            return

        def p_postfix_expression_6(p):
            'postfix_expression :  postfix_expression PTR_OP identifier'
            if self.DebugProd == True:
                self.DebugPrint("postfix_expression -->  postfix_expression PTR_OP identifier", p)
            return

        def p_postfix_expression_7(p):
            'postfix_expression :  postfix_expression INC_OP'
            p[0] = p[1]
            if self.DebugProd == True:
                self.DebugPrint("postfix_expression -->  postfix_expression INC_OP", p)
            return

        def p_postfix_expression_8(p):
            'postfix_expression :  postfix_expression DEC_OP'
            p[0] = p[1]
            if self.DebugProd == True:
                self.DebugPrint("postfix_expression -->  postfix_expression DEC_OP", p)
            return

        #primary expressions are used by many operations
        def p_primary_expression_1(p):
            'primary_expression :  identifier'

            p[0] = PrimaryExpression('identifier', p[1])

            if self.DebugProd == True:
                self.DebugPrint("primary_expression -->  identifier", p)
            return

        def p_primary_expression_2(p):
            'primary_expression :  constant'
            p[0] = PrimaryExpression('constant', p[1])

            if self.DebugProd == True:
                self.DebugPrint("primary_expression -->  constant", p)
            return

        def p_primary_expression_3(p):
            'primary_expression :  string'
            p[0] = PrimaryExpression('string', P[1])

            if self.DebugProd == True:
                self.DebugPrint("primary_expression -->  string", p)
            return

        def p_primary_expression_4(p):
            'primary_expression :  OPENPAREN expression CLOSEPAREN'
            p[0] = PrimaryExpression('expression', P[2])

            if self.DebugProd == True:
                self.DebugPrint("primary_expression -->  OPENPAREN expression CLOSEPAREN", p)
            return

        def p_argument_expression_list_1(p):
            'argument_expression_list :  assignment_expression'
            p[0] = PassUpNode("ArgumentExpressionList",[p[1]])

            if self.DebugProd == True:
                self.DebugPrint("argument_expression_list -->  assignment_expression", p)
            return

        def p_argument_expression_list_2(p):
            'argument_expression_list :  argument_expression_list COMMA assignment_expression'
            p[0] = PassUpNode("ArgumentExpressionList",[p[1],p[3]])

            if self.DebugProd == True:
                self.DebugPrint("argument_expression_list -->  argument_expression_list COMMA assignment_expression", p)
            return

        def p_constant_1(p):
            'constant :  INTEGER_CONSTANT'
            p[0]=Constant('int', p[1])
            if self.DebugProd == True:
                self.DebugPrint("constant -->  INTEGER_CONSTANT", p)
            return

        def p_constant_2(p):
            'constant :  CHARACTER_CONSTANT'
            p[0]=Constant('char', p[1])
            if self.DebugProd == True:
                self.DebugPrint("constant -->  CHARACTER_CONSTANT", p)
            return

        def p_constant_3(p):
            'constant :  FLOATING_CONSTANT'
            p[0]=Constant('float', p[1])
            if self.DebugProd == True:
                self.DebugPrint("constant -->  FLOATING_CONSTANT", p)
            return

        def p_constant_4(p):
            'constant :  ENUMERATION_CONSTANT'
            p[0]=Constant('enum', p[1])
            if self.DebugProd == True:
                self.DebugPrint("constant -->  ENUMERATION_CONSTANT", p)
            return

        def p_string_1(p):
            'string :  STRING_LITERAL'
            p[0]=Constant('char*', p[1])
            if self.DebugProd == True:
                self.DebugPrint("string -->  STRING_LITERAL", p)
            return

        def p_identifier_1(p):
            'identifier :  IDENTIFIER'
            #passing up the identifier
            # p[0] = p[1]

            IdPtr = self.ST.InsertSymbol(p[1]['lexeme'], {'TokenLocation': p[1]['additional']['TokenLocation']})

            p[0] = Identifier(p[1]['lexeme'], IdPtr, p[1]['additional']['TokenLocation'], self.ST, p)

            if self.DebugProd == True:
                self.DebugPrint("identifier -->  IDENTIFIER", p)


        #empty productions
        def p_empty_insertmode(p):
            'insert_mode_e :'

            self.ST.InsertMode()

            if self.DebugProd == True:
                print("insert_mode_e -->  ", p)

            return

        def p_empty_readmode(p):
            'read_mode_e :'

            self.ST.ReadModeOn()

            if self.DebugProd == True:
                print("read_mode_e -->  ", p)

            return

        def p_empty_push_scope(p):
            'push_scope_e :'

            self.ST.PushNewScope()
            if self.DebugProd == True:
                print("push_scope_e -->  ", p)
            return

        def p_empty_pop_scope(p):
            'pop_scope_e :'

            self.ST.PopScope()
            if self.DebugProd == True:
                print("pop_scope_e -->  ", p)
            return

        def p_error(p):
            ErrManager.AddError(PrettyErrorPrint("Syntax Error. Did you possibly forget a semicolon somewhere?", p.lexer.lineno, FindColumn(p.lexer.lexdata, p.lexer), p.lexer.lexdata))
            return


        #must be here to make parser build correctly
        tokens = self.LA.Tokens


        #at some point we will use the following code:
        #(See PLY Documentation 6.12)
        self.LA.BuildLexer()
        self.Parser = yacc.yacc()
