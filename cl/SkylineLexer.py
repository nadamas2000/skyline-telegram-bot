# Generated from Skyline.g by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("F\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\6")
        buf.write("\6)\n\6\r\6\16\6*\3\7\3\7\7\7/\n\7\f\7\16\7\62\13\7\3")
        buf.write("\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\r\3\r")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\17\2\2\20\3\3\5\4\7\5\t\6")
        buf.write("\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\3\2\6\3\2\62;\4\2C\\c|\5\2\62;C\\c|\5\2\13\f\16\17\"")
        buf.write("\"\2G\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write("\3\2\2\2\2\35\3\2\2\2\3\37\3\2\2\2\5!\3\2\2\2\7#\3\2\2")
        buf.write("\2\t%\3\2\2\2\13(\3\2\2\2\r,\3\2\2\2\17\63\3\2\2\2\21")
        buf.write("\65\3\2\2\2\23\67\3\2\2\2\259\3\2\2\2\27<\3\2\2\2\31>")
        buf.write("\3\2\2\2\33@\3\2\2\2\35B\3\2\2\2\37 \7*\2\2 \4\3\2\2\2")
        buf.write("!\"\7+\2\2\"\6\3\2\2\2#$\7}\2\2$\b\3\2\2\2%&\7\177\2\2")
        buf.write("&\n\3\2\2\2\')\t\2\2\2(\'\3\2\2\2)*\3\2\2\2*(\3\2\2\2")
        buf.write("*+\3\2\2\2+\f\3\2\2\2,\60\t\3\2\2-/\t\4\2\2.-\3\2\2\2")
        buf.write("/\62\3\2\2\2\60.\3\2\2\2\60\61\3\2\2\2\61\16\3\2\2\2\62")
        buf.write("\60\3\2\2\2\63\64\7-\2\2\64\20\3\2\2\2\65\66\7/\2\2\66")
        buf.write("\22\3\2\2\2\678\7,\2\28\24\3\2\2\29:\7<\2\2:;\7?\2\2;")
        buf.write("\26\3\2\2\2<=\7]\2\2=\30\3\2\2\2>?\7_\2\2?\32\3\2\2\2")
        buf.write("@A\7.\2\2A\34\3\2\2\2BC\t\5\2\2CD\3\2\2\2DE\b\17\2\2E")
        buf.write("\36\3\2\2\2\5\2*\60\3\b\2\2")
        return buf.getvalue()


class SkylineLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    NUM = 5
    ID = 6
    SUM = 7
    SUB = 8
    MUL = 9
    ASIG = 10
    BEGL = 11
    ENDL = 12
    SEP = 13
    WS = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'{'", "'}'", "'+'", "'-'", "'*'", "':='", "'['", 
            "']'", "','" ]

    symbolicNames = [ "<INVALID>",
            "NUM", "ID", "SUM", "SUB", "MUL", "ASIG", "BEGL", "ENDL", "SEP", 
            "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "NUM", "ID", "SUM", "SUB", 
                  "MUL", "ASIG", "BEGL", "ENDL", "SEP", "WS" ]

    grammarFileName = "Skyline.g"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


