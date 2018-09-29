from SymbolTable import SymbolTable
from bintrees import FastRBTree
from copy import deepcopy

def test_creation():
    ST = SymbolTable()
    assert( type(ST.Table) == type([]) )
    assert( type(ST.TopScope) == type(FastRBTree()) )

def test_add_symbol():
    ST = SymbolTable()
    T = FastRBTree()

    Content = {'DataType': "int" , 'AssignedValue': 110 , 'TokenLocation': (10,2) }
    ST.InsertSymbol("age", Content)
    T.insert("age", Content)

    Content = {'DataType': "float" , 'AssignedValue': 28.9 , 'TokenLocation': (11,2) }
    ST.InsertSymbol("temperature", Content)
    T.insert("temperature", Content)

    Content = {'DataType': "char" , 'AssignedValue': 'a' , 'TokenLocation': (12,2) }
    ST.InsertSymbol("letter", Content)
    T.insert("letter", Content)

    keys = ST.TopScope.keys()
    for key in keys:
        assert(T.__contains__(key))
        assert(T.get(key) == ST.TopScope.get(key))
        assert(T.get(key) is not ST.TopScope.get(key))

    #write test to prove that the returned item is a pointer

    return


def test_push_new_scope():
    ST = SymbolTable()
    ST2 = SymbolTable()

    ST.PushNewScope()
    ST.PushNewScope()
    ST.PushNewScope()

    assert(len(ST2.Table) < len(ST.Table))
    assert(len(ST.Table) == 3)


def test_push_scope():
    ST = SymbolTable()
    T = FastRBTree()
    T2 = FastRBTree()

    ST.PushScope(T)
    assert( len(ST.Table) == 1 )

    ST.PushScope(T2)
    assert( len(ST.Table) == 2 )

    return


def test_find_in_current_scope():
    ST = SymbolTable()

    Content = {'DataType': "int" , 'AssignedValue': 110 , 'TokenLocation': (10,2) }
    ST.InsertSymbol("age", Content)

    assert( ST.FindSymbolInCurrentScope("age") == Content )

    Content = {'DataType': "float" , 'AssignedValue': 28.9 , 'TokenLocation': (11,2) }
    ST.InsertSymbol("temperature", Content)

    assert( ST.FindSymbolInCurrentScope("temperature") == Content )

    Content = {'DataType': "char" , 'AssignedValue': 'a' , 'TokenLocation': (12,2) }
    ST.InsertSymbol("letter", Content)

    assert( ST.FindSymbolInCurrentScope("letter") == Content )

    #nonexistent symbol case
    assert( ST.FindSymbolInCurrentScope("foo") == False )


    return


def test_find_in_table():
    ST = SymbolTable()

    Content1 = {'DataType': "int" , 'AssignedValue': 110 , 'TokenLocation': (10,2) }
    ST.InsertSymbol("age", Content1)
    ST.PushNewScope();
    Content2 = {'DataType': "float" , 'AssignedValue': 28.9 , 'TokenLocation': (11,2) }
    ST.InsertSymbol("temperature", Content2)
    ST.PushNewScope();
    Content3 = {'DataType': "char" , 'AssignedValue': 'a' , 'TokenLocation': (12,2) }
    ST.InsertSymbol("letter", Content3)
    ST.PushNewScope();

    assert( ST.FindSymbolInTable("letter")[0] == {1: Content3} )
    assert( ST.FindSymbolInTable("temperature")[0] == {2: Content2} )

    assert( (ST.FindSymbolInTable("age")[0] is {3: Content1}) == False )

    #nonexistent symbol case
    assert( ST.FindSymbolInTable("foo") == False )

    #searcing in current scope case
    assert( ST.FindSymbolInCurrentScope("age") == False )

    return

def test_toggle_read_mode():
    ST = SymbolTable()
    ST.ToggleReadMode()
    assert(ST.ReadMode == False)
    return

def test_write_symbol_table():
        ST = SymbolTable()
        ST.DebugMode = True

        Content1 = {'DataType': "int" , 'AssignedValue': 110 , 'TokenLocation': (10,2) }
        ST.InsertSymbol("age", Content1)
        ST.PushNewScope();
        Content2 = {'DataType': "float" , 'AssignedValue': 28.9 , 'TokenLocation': (11,2) }
        ST.InsertSymbol("temperature", Content2)
        Content2 = {'DataType': "float" , 'AssignedValue': 38.9 , 'TokenLocation': (12,2) }
        ST.InsertSymbol("t2", Content2)
        ST.PushNewScope();
        Content3 = {'DataType': "char" , 'AssignedValue': 'a' , 'TokenLocation': (13,2) }
        ST.InsertSymbol("letter", Content3)
        ST.PushNewScope();

        ST.WriteSymbolTableToFile("Debug.out")
