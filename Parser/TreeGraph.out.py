from anytree import Node, RenderTree 
from anytree.exporter import DotExporter
FunctionDefintion140479643736208 = Node('FunctionDefintion_6208')
DeclarationSpecifiers140479642054352 = Node('DeclarationSpecifiers_4352', parent=FunctionDefintion140479643736208)
leaf = Node('int_4352', parent=DeclarationSpecifiers140479642054352)
FunctionPrototype140479643736080 = Node('FunctionPrototype_6080', parent=FunctionDefintion140479643736208)
Identifier140479642054544 = Node('Identifier_4544', parent=FunctionPrototype140479643736080)
leaf = Node('main_4544', parent=Identifier140479642054544)
leaf = Node("Subtype='Function Prototype', Label='main', Arguments=[{'Type': ['int']}], TokenLocation=(1, 4, 5)", parent=Identifier140479642054544)
Declaration140479643735952 = Node('Declaration_5952', parent=FunctionPrototype140479643736080)
DeclarationSpecifiers140479642054480 = Node('DeclarationSpecifiers_4480', parent=Declaration140479643735952)
leaf = Node('int_4480', parent=DeclarationSpecifiers140479642054480)
Identifier140479643735888 = Node('Identifier_5888', parent=Declaration140479643735952)
leaf = Node('arg1_5888', parent=Identifier140479643735888)
leaf = Node("Type=['int'], TokenLocation=(1, 13, 14)", parent=Identifier140479643735888)
CompoundStatement140479642061840 = Node('CompoundStatement_1840', parent=FunctionDefintion140479643736208)
DeclList140479643737168 = Node('DeclList_7168', parent=CompoundStatement140479642061840)
DeclList140479643736656 = Node('DeclList_6656', parent=DeclList140479643737168)
Declaration140479643736784 = Node('Declaration_6784', parent=DeclList140479643736656)
DeclarationSpecifiers140479643736144 = Node('DeclarationSpecifiers_6144', parent=Declaration140479643736784)
leaf = Node('int_6144', parent=DeclarationSpecifiers140479643736144)
InitDeclList140479643736592 = Node('InitDeclList_6592', parent=Declaration140479643736784)
ArrayDeclaration140479643736464 = Node('ArrayDeclaration_6464', parent=InitDeclList140479643736592)
ArrayDeclaration140479643736528 = Node('ArrayDeclaration_6528', parent=ArrayDeclaration140479643736464)
Identifier140479643736016 = Node('Identifier_6016', parent=ArrayDeclaration140479643736528)
leaf = Node('arr_6016', parent=Identifier140479643736016)
leaf = Node("Array Size=['3', '3'], Subtype='Array', Type=['int'], TokenLocation=(3, 26, 6)", parent=Identifier140479643736016)
PrimaryExpression140479643736400 = Node('PrimaryExpression_6400', parent=ArrayDeclaration140479643736528)
Constant140479643736272 = Node('Constant_6272', parent=PrimaryExpression140479643736400)
leaf = Node('3_6272', parent=Constant140479643736272)
PrimaryExpression140479643736720 = Node('PrimaryExpression_6720', parent=ArrayDeclaration140479643736464)
Constant140479643736336 = Node('Constant_6336', parent=PrimaryExpression140479643736720)
leaf = Node('3_6336', parent=Constant140479643736336)
Declaration140479643737040 = Node('Declaration_7040', parent=DeclList140479643737168)
DeclarationSpecifiers140479643736912 = Node('DeclarationSpecifiers_6912', parent=Declaration140479643737040)
leaf = Node('int_6912', parent=DeclarationSpecifiers140479643736912)
InitDeclList140479643736848 = Node('InitDeclList_6848', parent=Declaration140479643737040)

for pre, fill, node in RenderTree(FunctionDefintion140479643736208):
    if "TokenLocation" in node.name: print("%s%s" % (pre, node.name))
    else: print("%s%s" % (pre, node.name[:-5]) )

    
def f(node):
    if node.is_leaf and "TokenLocation" in node.name:
        return 'label="%s"' % (node.name)
    return 'label="%s"' % (node.name[:-5])

DotExporter(FunctionDefintion140479643736208, nodeattrfunc=f).to_picture("AST.png")
        