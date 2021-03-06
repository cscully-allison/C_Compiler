from graphviz import Digraph

dot = Digraph(comment='C Grammar')

dot.node('Tu', 'translation_unit')
dot.node('Ed', 'external_declaration')
dot.node('Fd', 'function_definition')
dot.node('Dec', 'declaration')
dot.node('Dl', 'declaration_list')
dot.node('Ds', 'declaration_specifiers')
dot.node('Scs', 'storage_class_specifier')
dot.node('Ts', 'type_specifier')
dot.node('Tq', 'type_qualifier')
dot.node('Sous', 'struct_or_union_specifier')
dot.node('Sou', 'struct_or_union')
dot.node('Sdl', 'struct_declaration_list')
dot.node('Idl', 'init_declarator_list')
dot.node('InitD', 'init_declarator')
dot.node('Sd', 'struct_declaration')
dot.node('Sql', 'specifier_qualifier_list')
dot.node('Sdrl', 'struct_declarator_list')
dot.node('Sdr', 'struct_declarator')
dot.node('Es', 'enum_specifier')
dot.node('El', 'enumerator_list')
dot.node('Enum', 'enumerator')
dot.node('Dr', 'declarator')
dot.node('Ddr', 'direct_declarator')
dot.node('Ptr', 'pointer')
dot.node('Tql', 'type_qualifier_list')
dot.node('Ptl', 'parameter_type_list')
dot.node('Pl', 'parameter_list')
dot.node('Pd', 'parameter_declaration')
dot.node('Il', 'identifier_list')
dot.node('Init', 'initializer')
dot.node('InitL', 'initializer_list')
dot.node('Tn', 'type_name')
dot.node('Adr', 'abstract_declarator')
dot.node('Dadr', 'direct_abstract_declarator')
dot.node('Stmt', 'statement')
dot.node('LStmt', 'labeled_statement')
dot.node('EStmt', 'expression_statement')
dot.node('CStmt', 'compound_statement')
dot.node('StmtL', 'statement_list')
dot.node('SStmt', 'selection_statement')
dot.node('IStmt', 'iteration_statement')
dot.node('JStmt', 'jump_statement')
dot.node('Exp', 'expression')
dot.node('AExp', 'assignment_expression')
dot.node('AOp', 'assignment_operator')
dot.node('CExp', 'conditional_expression')
dot.node('ConstExp', 'constant_expression')
dot.node('LOExp', 'logical_or_expression')
dot.node('LAExp', 'logical_and_expression')
dot.node('IOExp', 'inclusive_or_expression')
dot.node('EOExp', 'exclusive_or_expression')
dot.node('AEexp', 'and_expression')
dot.node('EExp', 'equality_expression')
dot.node('REexp', 'relational_expression')
dot.node('SExp', 'shift_expression')
dot.node('AddExp', 'additive_expression')
dot.node('MulExp', 'multiplicative_expression')
dot.node('CastExp', 'cast_expression')
dot.node('Unexp', 'unary_expression')
dot.node('UOp', 'unary_operator')
dot.node('PostExp', 'postfix_expression')
dot.node('PriExp', 'primary_expression')
dot.node('AExpL', 'argument_expression_list')
dot.node('Const', 'constant')
dot.node('Str', 'string')
dot.node('Id', 'identifier')

dot.edge('Tu', 'Tu')
dot.edge('Tu', 'Ed')
dot.edge('Ed', 'Fd')
dot.edge('Ed', 'Dec')
dot.edge('Fd', 'CStmt')
dot.edge('Fd', 'Dec')
dot.edge('Fd', 'Dl')
dot.edge('Fd', 'Ds')
dot.edge('Dec', 'Ds')
dot.edge('Dec', 'Idl')
dot.edge('Dec', ';')
dot.edge('Dl', 'Dec')
dot.edge('Dl', 'Dl')
dot.edge('Ds', 'Scs')
dot.edge('Ds', 'Ds')
dot.edge('Ds', 'Ts')
dot.edge('Ds', 'Tq')
dot.edge('Scs', 'AUTO')
dot.edge('Scs', 'REGISTER')
dot.edge('Scs', 'STATIC')
dot.edge('Scs', 'TYPEDEF')
dot.edge('Scs', 'EXTERN')
# dot.edge('Ts', 'VOID')
# dot.edge('Ts', 'CHAR')
# dot.edge('Ts', 'SHORT')
# dot.edge('Ts', 'INT')
# dot.edge('Ts', 'LONG')
# dot.edge('Ts', 'FLOAT')
# dot.edge('Ts', 'DOUBLE')
# dot.edge('Ts', 'SIGNED')
# dot.edge('Ts', 'UNSIGNED')
dot.edge('Ts', 'Sous')
dot.edge('Ts', 'Es')
dot.edge('Ts', '<DATATYPES>')
# dot.edge('Ts', 'TYPEDEF_NAME')
dot.edge('Tq', 'CONST')
dot.edge('Tq', 'VOLATILE')
dot.edge('Sous','Sou')
dot.edge('Sous','Id')
dot.edge('Sous','Sdl')
dot.edge('Sou','STRUCT')
dot.edge('Sou','UNION')
dot.edge('Sdl','Sd')
dot.edge('Sdl','Sdl')
dot.edge('Idl','Idl')
dot.edge('Idl','InitD')
dot.edge('InitD', 'Dr')
dot.edge('InitD','=')
dot.edge('InitD','Init')
dot.edge('Sd', 'Sql')
dot.edge('Sd', 'Sdrl')
dot.edge('Sql', 'Ts')
dot.edge('Sql', 'Sql')
dot.edge('Sql', 'Tq')
dot.edge('Sdrl', 'Sdr')
dot.edge('Sdrl', 'Sdrl')
dot.edge('Sdr', 'Dr')
dot.edge('Sdr', 'ConstExp')
dot.edge('Es', 'El')
dot.edge('Es', 'ENUM')
dot.edge('Es', 'Id')
dot.edge('El', 'Enum')
dot.edge('El', 'El')
dot.edge('Enum', 'Id')
dot.edge('Es', 'ConstExp')
dot.edge('Dr', 'Ddr')
dot.edge('Dr', 'Ptr')
dot.edge('Ddr', 'Id')
dot.edge('Ddr', 'Ddr')
dot.edge('Ddr', 'Dr')
dot.edge('Ddr', 'ConstExp')
dot.edge('Ddr', 'Ptl')
dot.edge('Ddr', 'Il')
dot.edge('Ptr', 'Tql')
dot.edge('Ptr', 'Ptr')
dot.edge('Tql', 'Tq')
dot.edge('Tql', 'Tql')
dot.edge('Ptl', 'Pl')
dot.edge('Ptl', '. . .')
dot.edge('Pl', 'Pd')
dot.edge('Pl', 'Pl')
dot.edge('Pd', 'Ds')
dot.edge('Pd', 'Dr')
dot.edge('Pd', 'Adr')






















print(dot.source)

dot.render('testoutput.gv', view=True)
