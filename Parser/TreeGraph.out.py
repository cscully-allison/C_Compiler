from anytree import Node, RenderTree 
from anytree.exporter import DotExporter
PassUpNode140341757637264 = Node('TranslationUnit_7264')
PassUpNode140341757587088 = Node('TranslationUnit_7088', parent=PassUpNode140341757637264)
PassUpNode140341757517584 = Node('TranslationUnit_7584', parent=PassUpNode140341757587088)
PassUpNode140341757515344 = Node('TranslationUnit_5344', parent=PassUpNode140341757517584)
PassUpNode140341757514896 = Node('TranslationUnit_4896', parent=PassUpNode140341757515344)
PassUpNode140341757513872 = Node('TranslationUnit_3872', parent=PassUpNode140341757514896)
Declaration140341757468560 = Node('Declaration_8560', parent=PassUpNode140341757513872)
DeclarationSpecifiers140341761031184 = Node('DeclarationSpecifiers_1184', parent=Declaration140341757468560)
leaf = Node('int_1184', parent=DeclarationSpecifiers140341761031184)
InitDeclList140341761031248 = Node('InitDeclList_1248', parent=Declaration140341757468560)
Identifier140341761095632 = Node('Identifier_5632', parent=InitDeclList140341761031248)
leaf = Node('var0_5632', parent=Identifier140341761095632)
leaf = Node("Type=['int'], TokenLocation=(1, 4, 5)", parent=Identifier140341761095632)
Declaration140341757513936 = Node('Declaration_3936', parent=PassUpNode140341757513872)
DeclarationSpecifiers140341757756560 = Node('DeclarationSpecifiers_6560', parent=Declaration140341757513936)
leaf = Node('char_6560', parent=DeclarationSpecifiers140341757756560)
InitDeclList140341757468624 = Node('InitDeclList_8624', parent=Declaration140341757513936)
Identifier140341757513808 = Node('Identifier_3808', parent=InitDeclList140341757468624)
leaf = Node('var1_3808', parent=Identifier140341757513808)
leaf = Node("Type=['char'], TokenLocation=(2, 15, 6)", parent=Identifier140341757513808)
Declaration140341757514832 = Node('Declaration_4832', parent=PassUpNode140341757514896)
DeclarationSpecifiers140341757514064 = Node('DeclarationSpecifiers_4064', parent=Declaration140341757514832)
leaf = Node('int_4064', parent=DeclarationSpecifiers140341757514064)
InitDeclList140341757514192 = Node('InitDeclList_4192', parent=Declaration140341757514832)
FunctionPrototype140341757514512 = Node('FunctionPrototype_4512', parent=InitDeclList140341757514192)
Identifier140341757514000 = Node('Identifier_4000', parent=FunctionPrototype140341757514512)
leaf = Node('fun1_4000', parent=Identifier140341757514000)
leaf = Node("Return Type=['int'], Subtype='Function Prototype', Label='fun1', Arguments=[{'Array Size Info': ['30', '20'], 'Type': ['int'], 'Subtype': 'Array Argument'}, {'Type': ['char']}], TokenLocation=(6, 53, 5)", parent=Identifier140341757514000)
PassUpNode140341757514704 = Node('ParameterList_4704', parent=FunctionPrototype140341757514512)
PassUpNode140341757514576 = Node('ParameterDeclaration_4576', parent=PassUpNode140341757514704)
DeclarationSpecifiers140341757514256 = Node('DeclarationSpecifiers_4256', parent=PassUpNode140341757514576)
leaf = Node('int_4256', parent=DeclarationSpecifiers140341757514256)
PassUpNode140341757514448 = Node('DirectAbstractDeclarator_4448', parent=PassUpNode140341757514576)
PrimaryExpression140341757514384 = Node('PrimaryExpression_4384', parent=PassUpNode140341757514448)
Constant140341757514128 = Node('Constant_4128', parent=PrimaryExpression140341757514384)
leaf = Node('30_4128', parent=Constant140341757514128)
PrimaryExpression140341757514640 = Node('PrimaryExpression_4640', parent=PassUpNode140341757514448)
Constant140341757514320 = Node('Constant_4320', parent=PrimaryExpression140341757514640)
leaf = Node('20_4320', parent=Constant140341757514320)
DeclarationSpecifiers140341757514768 = Node('DeclarationSpecifiers_4768', parent=PassUpNode140341757514704)
leaf = Node('char_4768', parent=DeclarationSpecifiers140341757514768)
Declaration140341757515280 = Node('Declaration_5280', parent=PassUpNode140341757515344)
DeclarationSpecifiers140341757515024 = Node('DeclarationSpecifiers_5024', parent=Declaration140341757515280)
leaf = Node('int_5024', parent=DeclarationSpecifiers140341757515024)
InitDeclList140341757515152 = Node('InitDeclList_5152', parent=Declaration140341757515280)
FunctionPrototype140341757515088 = Node('FunctionPrototype_5088', parent=InitDeclList140341757515152)
Identifier140341757514960 = Node('Identifier_4960', parent=FunctionPrototype140341757515088)
leaf = Node('fun2_4960', parent=Identifier140341757514960)
leaf = Node("Return Type=['int'], Subtype='Function Prototype', Label='fun2', Arguments=[{'Type': ['int']}], TokenLocation=(7, 82, 5)", parent=Identifier140341757514960)
DeclarationSpecifiers140341757515216 = Node('DeclarationSpecifiers_5216', parent=FunctionPrototype140341757515088)
leaf = Node('int_5216', parent=DeclarationSpecifiers140341757515216)
FunctionDefintion140341757516240 = Node('FunctionDefintion_6240', parent=PassUpNode140341757517584)
DeclarationSpecifiers140341757515472 = Node('DeclarationSpecifiers_5472', parent=FunctionDefintion140341757516240)
leaf = Node('int_5472', parent=DeclarationSpecifiers140341757515472)
FunctionPrototype140341757515856 = Node('FunctionPrototype_5856', parent=FunctionDefintion140341757516240)
Identifier140341757515408 = Node('Identifier_5408', parent=FunctionPrototype140341757515856)
leaf = Node('main_5408', parent=Identifier140341757515408)
leaf = Node("Subtype='Function Prototype', Label='main', Arguments=[{'Type Qualifier': ['const'], 'Type': ['int']}, {'Type': ['char']}], TokenLocation=(9, 98, 5)", parent=Identifier140341757515408)
PassUpNode140341757516176 = Node('ParameterList_6176', parent=FunctionPrototype140341757515856)
Declaration140341757515792 = Node('Declaration_5792', parent=PassUpNode140341757516176)
DeclarationSpecifiers140341757515664 = Node('DeclarationSpecifiers_5664', parent=Declaration140341757515792)
leaf = Node('const_5664', parent=DeclarationSpecifiers140341757515664)
DeclarationSpecifiers140341757515728 = Node('DeclarationSpecifiers_5728', parent=DeclarationSpecifiers140341757515664)
leaf = Node('int_5728', parent=DeclarationSpecifiers140341757515728)
Identifier140341757515536 = Node('Identifier_5536', parent=Declaration140341757515792)
leaf = Node('arg1_5536', parent=Identifier140341757515536)
leaf = Node("Type Qualifier=['const'], Type=['int'], TokenLocation=(9, 113, 20)", parent=Identifier140341757515536)
Declaration140341757516048 = Node('Declaration_6048', parent=PassUpNode140341757516176)
DeclarationSpecifiers140341757515984 = Node('DeclarationSpecifiers_5984', parent=Declaration140341757516048)
leaf = Node('char_5984', parent=DeclarationSpecifiers140341757515984)
Identifier140341757515920 = Node('Identifier_5920', parent=Declaration140341757516048)
leaf = Node('arg2_5920', parent=Identifier140341757515920)
leaf = Node("Type=['char'], TokenLocation=(9, 124, 31)", parent=Identifier140341757515920)
CompoundStatement140341757515600 = Node('CompoundStatement_5600', parent=FunctionDefintion140341757516240)
DeclList140341757516752 = Node('DeclList_6752', parent=CompoundStatement140341757515600)
Declaration140341757516880 = Node('Declaration_6880', parent=DeclList140341757516752)
DeclarationSpecifiers140341757516304 = Node('DeclarationSpecifiers_6304', parent=Declaration140341757516880)
leaf = Node('int_6304', parent=DeclarationSpecifiers140341757516304)
InitDeclList140341757516688 = Node('InitDeclList_6688', parent=Declaration140341757516880)
ArrayDeclaration140341757516560 = Node('ArrayDeclaration_6560', parent=InitDeclList140341757516688)
ArrayDeclaration140341757516624 = Node('ArrayDeclaration_6624', parent=ArrayDeclaration140341757516560)
Identifier140341757516112 = Node('Identifier_6112', parent=ArrayDeclaration140341757516624)
leaf = Node('arr1_6112', parent=Identifier140341757516112)
leaf = Node("Array Size=['30', '20'], Subtype='Array', Type=['int'], TokenLocation=(10, 137, 7)", parent=Identifier140341757516112)
PrimaryExpression140341757516496 = Node('PrimaryExpression_6496', parent=ArrayDeclaration140341757516624)
Constant140341757516368 = Node('Constant_6368', parent=PrimaryExpression140341757516496)
leaf = Node('30_6368', parent=Constant140341757516368)
PrimaryExpression140341757516816 = Node('PrimaryExpression_6816', parent=ArrayDeclaration140341757516560)
Constant140341757516432 = Node('Constant_6432', parent=PrimaryExpression140341757516816)
leaf = Node('20_6432', parent=Constant140341757516432)
FunctionCall140341757517264 = Node('FunctionCall_7264', parent=CompoundStatement140341757515600)
PrimaryExpression140341757517008 = Node('PrimaryExpression_7008', parent=FunctionCall140341757517264)
Identifier140341757516944 = Node('Identifier_6944', parent=PrimaryExpression140341757517008)
leaf = Node('fun1_6944', parent=Identifier140341757516944)
leaf = Node("Return Type=['int'], Subtype='Function Prototype', Label='fun1', Arguments=[{'Array Size Info': ['30', '20'], 'Type': ['int'], 'Subtype': 'Array Argument'}, {'Type': ['char']}], TokenLocation=(6, 53, 5)", parent=Identifier140341757516944)
PassUpNode140341757517520 = Node('ArgumentExpressionList_7520', parent=FunctionCall140341757517264)
PrimaryExpression140341757517200 = Node('PrimaryExpression_7200', parent=PassUpNode140341757517520)
Identifier140341757517136 = Node('Identifier_7136', parent=PrimaryExpression140341757517200)
leaf = Node('arr1_7136', parent=Identifier140341757517136)
leaf = Node("Array Size=['30', '20'], Subtype='Array', Type=['int'], TokenLocation=(10, 137, 7)", parent=Identifier140341757517136)
PrimaryExpression140341757517392 = Node('PrimaryExpression_7392', parent=PassUpNode140341757517520)
Identifier140341757517328 = Node('Identifier_7328', parent=PrimaryExpression140341757517392)
leaf = Node('var1_7328', parent=Identifier140341757517328)
leaf = Node("Type=['char'], TokenLocation=(2, 15, 6)", parent=Identifier140341757517328)
FunctionDefintion140341757584272 = Node('FunctionDefintion_4272', parent=PassUpNode140341757587088)
DeclarationSpecifiers140341757517072 = Node('DeclarationSpecifiers_7072', parent=FunctionDefintion140341757584272)
leaf = Node('int_7072', parent=DeclarationSpecifiers140341757517072)
FunctionPrototype140341757583824 = Node('FunctionPrototype_3824', parent=FunctionDefintion140341757584272)
Identifier140341757517648 = Node('Identifier_7648', parent=FunctionPrototype140341757583824)
leaf = Node('fun1_7648', parent=Identifier140341757517648)
leaf = Node("Return Type=['int'], Subtype='Function Prototype', Label='fun1', Arguments=[{'Array Size Info': ['30', '20'], 'Type': ['int'], 'Subtype': 'Array Argument'}, {'Type': ['char']}], TokenLocation=(6, 53, 5)", parent=Identifier140341757517648)
PassUpNode140341757584208 = Node('ParameterList_4208', parent=FunctionPrototype140341757583824)
Declaration140341757583760 = Node('Declaration_3760', parent=PassUpNode140341757584208)
DeclarationSpecifiers140341757517776 = Node('DeclarationSpecifiers_7776', parent=Declaration140341757583760)
leaf = Node('int_7776', parent=DeclarationSpecifiers140341757517776)
ArrayDeclaration140341757583632 = Node('ArrayDeclaration_3632', parent=Declaration140341757583760)
ArrayDeclaration140341757583696 = Node('ArrayDeclaration_3696', parent=ArrayDeclaration140341757583632)
Identifier140341757517456 = Node('Identifier_7456', parent=ArrayDeclaration140341757583696)
leaf = Node('arg3_7456', parent=Identifier140341757517456)
leaf = Node("Array Size=['30', '20'], Subtype='Array', Type=['int'], TokenLocation=(15, 188, 14)", parent=Identifier140341757517456)
PrimaryExpression140341757583568 = Node('PrimaryExpression_3568', parent=ArrayDeclaration140341757583696)
Constant140341757583440 = Node('Constant_3440', parent=PrimaryExpression140341757583568)
leaf = Node('30_3440', parent=Constant140341757583440)
PrimaryExpression140341757583888 = Node('PrimaryExpression_3888', parent=ArrayDeclaration140341757583632)
Constant140341757583504 = Node('Constant_3504', parent=PrimaryExpression140341757583888)
leaf = Node('20_3504', parent=Constant140341757583504)
Declaration140341757584080 = Node('Declaration_4080', parent=PassUpNode140341757584208)
DeclarationSpecifiers140341757584016 = Node('DeclarationSpecifiers_4016', parent=Declaration140341757584080)
leaf = Node('char_4016', parent=DeclarationSpecifiers140341757584016)
Identifier140341757583952 = Node('Identifier_3952', parent=Declaration140341757584080)
leaf = Node('arg4_3952', parent=Identifier140341757583952)
leaf = Node("Type=['char'], TokenLocation=(15, 207, 33)", parent=Identifier140341757583952)
CompoundStatement140341757517712 = Node('CompoundStatement_7712', parent=FunctionDefintion140341757584272)
DeclList140341757584784 = Node('DeclList_4784', parent=CompoundStatement140341757517712)
DeclList140341757584464 = Node('DeclList_4464', parent=DeclList140341757584784)
Declaration140341757584528 = Node('Declaration_4528', parent=DeclList140341757584464)
DeclarationSpecifiers140341757584336 = Node('DeclarationSpecifiers_4336', parent=Declaration140341757584528)
leaf = Node('int_4336', parent=DeclarationSpecifiers140341757584336)
InitDeclList140341757584400 = Node('InitDeclList_4400', parent=Declaration140341757584528)
Identifier140341757584144 = Node('Identifier_4144', parent=InitDeclList140341757584400)
leaf = Node('var2_4144', parent=Identifier140341757584144)
leaf = Node("Type=['int'], TokenLocation=(16, 222, 9)", parent=Identifier140341757584144)
Declaration140341757584848 = Node('Declaration_4848', parent=DeclList140341757584784)
DeclarationSpecifiers140341757584656 = Node('DeclarationSpecifiers_4656', parent=Declaration140341757584848)
leaf = Node('char_4656', parent=DeclarationSpecifiers140341757584656)
InitDeclList140341757584720 = Node('InitDeclList_4720', parent=Declaration140341757584848)
Identifier140341757584592 = Node('Identifier_4592', parent=InitDeclList140341757584720)
leaf = Node('var3_4592', parent=Identifier140341757584592)
leaf = Node("Type=['char'], TokenLocation=(17, 237, 10)", parent=Identifier140341757584592)
PassUpNode140341757587024 = Node('StatementList_7024', parent=CompoundStatement140341757517712)
PassUpNode140341757585680 = Node('StatementList_5680', parent=PassUpNode140341757587024)
AssignmentExpression140341757585232 = Node('AssignmentExpression_5232', parent=PassUpNode140341757585680)
PrimaryExpression140341757584976 = Node('PrimaryExpression_4976', parent=AssignmentExpression140341757585232)
Identifier140341757584912 = Node('Identifier_4912', parent=PrimaryExpression140341757584976)
leaf = Node('var2_4912', parent=Identifier140341757584912)
leaf = Node("Type=['int'], TokenLocation=(16, 222, 9)", parent=Identifier140341757584912)
BinOp140341757585424 = Node('BinOp_5424', parent=AssignmentExpression140341757585232)
CastNode140341757585488 = Node('CastNode_5488', parent=BinOp140341757585424)
leaf = Node('int _5488', parent=CastNode140341757585488)
leaf = Node('char _5488', parent=CastNode140341757585488)
PrimaryExpression140341757585168 = Node('PrimaryExpression_5168', parent=CastNode140341757585488)
Identifier140341757585040 = Node('Identifier_5040', parent=PrimaryExpression140341757585168)
leaf = Node('arg4_5040', parent=Identifier140341757585040)
leaf = Node("Type=['char'], TokenLocation=(15, 207, 33)", parent=Identifier140341757585040)
leaf = Node('+_5424', parent=BinOp140341757585424)
PrimaryExpression140341757585296 = Node('PrimaryExpression_5296', parent=BinOp140341757585424)
Constant140341757585104 = Node('Constant_5104', parent=PrimaryExpression140341757585296)
leaf = Node('33_5104', parent=Constant140341757585104)
leaf = Node('int _5424', parent=BinOp140341757585424)
SelectionStatement140341757586128 = Node('SelectionStatement_6128', parent=PassUpNode140341757585680)
BinOp140341757586000 = Node('BinOp_6000', parent=SelectionStatement140341757586128)
PrimaryExpression140341757585616 = Node('PrimaryExpression_5616', parent=BinOp140341757586000)
Identifier140341757585360 = Node('Identifier_5360', parent=PrimaryExpression140341757585616)
leaf = Node('var0_5360', parent=Identifier140341757585360)
leaf = Node("Type=['int'], TokenLocation=(1, 4, 5)", parent=Identifier140341757585360)
leaf = Node('<_6000', parent=BinOp140341757586000)
CastNode140341757586064 = Node('CastNode_6064', parent=BinOp140341757586000)
leaf = Node('char _6064', parent=CastNode140341757586064)
leaf = Node('int _6064', parent=CastNode140341757586064)
PrimaryExpression140341757585872 = Node('PrimaryExpression_5872', parent=CastNode140341757586064)
Identifier140341757585808 = Node('Identifier_5808', parent=PrimaryExpression140341757585872)
leaf = Node('var1_5808', parent=Identifier140341757585808)
leaf = Node("Type=['char'], TokenLocation=(2, 15, 6)", parent=Identifier140341757585808)
leaf = Node('int _6000', parent=BinOp140341757586000)
CompoundStatement140341757585744 = Node('CompoundStatement_5744', parent=SelectionStatement140341757586128)
FunctionCall140341757586512 = Node('FunctionCall_6512', parent=CompoundStatement140341757585744)
PrimaryExpression140341757586256 = Node('PrimaryExpression_6256', parent=FunctionCall140341757586512)
Identifier140341757586192 = Node('Identifier_6192', parent=PrimaryExpression140341757586256)
leaf = Node('fun1_6192', parent=Identifier140341757586192)
leaf = Node("Return Type=['int'], Subtype='Function Prototype', Label='fun1', Arguments=[{'Array Size Info': ['30', '20'], 'Type': ['int'], 'Subtype': 'Array Argument'}, {'Type': ['char']}], TokenLocation=(6, 53, 5)", parent=Identifier140341757586192)
PassUpNode140341757586768 = Node('ArgumentExpressionList_6768', parent=FunctionCall140341757586512)
PrimaryExpression140341757586448 = Node('PrimaryExpression_6448', parent=PassUpNode140341757586768)
Identifier140341757586384 = Node('Identifier_6384', parent=PrimaryExpression140341757586448)
leaf = Node('arg3_6384', parent=Identifier140341757586384)
leaf = Node("Array Size=['30', '20'], Subtype='Array', Type=['int'], TokenLocation=(15, 188, 14)", parent=Identifier140341757586384)
PrimaryExpression140341757586640 = Node('PrimaryExpression_6640', parent=PassUpNode140341757586768)
Identifier140341757586576 = Node('Identifier_6576', parent=PrimaryExpression140341757586640)
leaf = Node('arg4_6576', parent=Identifier140341757586576)
leaf = Node("Type=['char'], TokenLocation=(15, 207, 33)", parent=Identifier140341757586576)
FunctionCall140341757586960 = Node('FunctionCall_6960', parent=PassUpNode140341757587024)
PrimaryExpression140341757586320 = Node('PrimaryExpression_6320', parent=FunctionCall140341757586960)
Identifier140341757585552 = Node('Identifier_5552', parent=PrimaryExpression140341757586320)
leaf = Node('fun2_5552', parent=Identifier140341757585552)
leaf = Node("Return Type=['int'], Subtype='Function Prototype', Label='fun2', Arguments=[{'Type': ['int']}], TokenLocation=(7, 82, 5)", parent=Identifier140341757585552)
PrimaryExpression140341757586896 = Node('PrimaryExpression_6896', parent=FunctionCall140341757586960)
Identifier140341757586832 = Node('Identifier_6832', parent=PrimaryExpression140341757586896)
leaf = Node('var3_6832', parent=Identifier140341757586832)
leaf = Node("Type=['char'], TokenLocation=(17, 237, 10)", parent=Identifier140341757586832)
FunctionDefintion140341757636752 = Node('FunctionDefintion_6752', parent=PassUpNode140341757637264)
DeclarationSpecifiers140341757586704 = Node('DeclarationSpecifiers_6704', parent=FunctionDefintion140341757636752)
leaf = Node('int_6704', parent=DeclarationSpecifiers140341757586704)
FunctionPrototype140341757636688 = Node('FunctionPrototype_6688', parent=FunctionDefintion140341757636752)
Identifier140341757585936 = Node('Identifier_5936', parent=FunctionPrototype140341757636688)
leaf = Node('fun2_5936', parent=Identifier140341757585936)
leaf = Node("Return Type=['int'], Subtype='Function Prototype', Label='fun2', Arguments=[{'Type': ['int']}], TokenLocation=(7, 82, 5)", parent=Identifier140341757585936)
Declaration140341757587344 = Node('Declaration_7344', parent=FunctionPrototype140341757636688)
DeclarationSpecifiers140341757587280 = Node('DeclarationSpecifiers_7280', parent=Declaration140341757587344)
leaf = Node('int_7280', parent=DeclarationSpecifiers140341757587280)
Identifier140341757587152 = Node('Identifier_7152', parent=Declaration140341757587344)
leaf = Node('arg5_7152', parent=Identifier140341757587152)
leaf = Node("Type=['int'], TokenLocation=(30, 357, 14)", parent=Identifier140341757587152)
CompoundStatement140341757587216 = Node('CompoundStatement_7216', parent=FunctionDefintion140341757636752)
FunctionCall140341757637136 = Node('FunctionCall_7136', parent=CompoundStatement140341757587216)
PrimaryExpression140341757636816 = Node('PrimaryExpression_6816', parent=FunctionCall140341757637136)
Identifier140341757587408 = Node('Identifier_7408', parent=PrimaryExpression140341757636816)
leaf = Node('fun2_7408', parent=Identifier140341757587408)
leaf = Node("Return Type=['int'], Subtype='Function Prototype', Label='fun2', Arguments=[{'Type': ['int']}], TokenLocation=(7, 82, 5)", parent=Identifier140341757587408)
PrimaryExpression140341757637008 = Node('PrimaryExpression_7008', parent=FunctionCall140341757637136)
Identifier140341757636944 = Node('Identifier_6944', parent=PrimaryExpression140341757637008)
leaf = Node('arg5_6944', parent=Identifier140341757636944)
leaf = Node("Type=['int'], TokenLocation=(30, 357, 14)", parent=Identifier140341757636944)

for pre, fill, node in RenderTree(PassUpNode140341757637264):
    if "TokenLocation" in node.name: print("%s%s" % (pre, node.name))
    else: print("%s%s" % (pre, node.name[:-5]) )

    
def f(node):
    if node.is_leaf and "TokenLocation" in node.name:
        return 'label="%s"' % (node.name)
    return 'label="%s"' % (node.name[:-5])

DotExporter(PassUpNode140341757637264, nodeattrfunc=f).to_picture("AST.png")
        