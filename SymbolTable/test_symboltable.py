from SymbolTable import SymbolTable
from bintrees import FastRBTree

def test_creation():
    ST = SymbolTable()
    assert(type(ST.table) == type([]))
    assert(type(ST.table[0]) == type(FastRBTree()))
