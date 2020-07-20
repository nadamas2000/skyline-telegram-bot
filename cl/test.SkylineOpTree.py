#!/urs/bin/env python3

from antlr4 import *
from SkylineLexer import SkylineLexer
from SkylineParser import SkylineParser
from TreeVisitor import TreeVisitor


def showTree(input_stream):
    """ Operació de crida i retorn al visitor amb les comandes
     com un strig input_stream"""
    lexer = SkylineLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SkylineParser(token_stream)
    tree = parser.root()
    visitor = TreeVisitor()
    return visitor.visit(tree)


if __name__ == '__main__':
    """ Mètode principal per recollida de operacions """
    inp = input('? ')
    while inp != 'exit':
        if len(inp):
            input_stream = InputStream(inp)
            try:
                showTree(input_stream)
            except Exception as e: \
                    print('Operació no admesa: ', e)
        inp = input('? ')
