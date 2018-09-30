import sys
sys.path.append("/LexicalAnalizer")
from LexicalAnalizer import LexicalAnalizer

class Parser():

    def __init__(self):
        self.LA = LexicalAnalizer()

    def BuildParser():
        #at some point we will use the following code:
        #(See PLY Documentation 6.12)
        # self.parser = yacc.parse(lexer=LA.Lexer)
