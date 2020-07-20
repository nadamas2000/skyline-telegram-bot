# Generated from Skyline.g by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("j\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\2\3\2\5\2\33")
        buf.write("\n\2\3\3\3\3\3\3\3\3\3\4\3\4\5\4#\n\4\3\4\3\4\3\5\3\5")
        buf.write("\3\5\7\5*\n\5\f\5\16\5-\13\5\3\6\3\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\5\nO")
        buf.write("\n\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13")
        buf.write("Z\n\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\7")
        buf.write("\13e\n\13\f\13\16\13h\13\13\3\13\2\3\24\f\2\4\6\b\n\f")
        buf.write("\16\20\22\24\2\2\2k\2\32\3\2\2\2\4\34\3\2\2\2\6 \3\2\2")
        buf.write("\2\b&\3\2\2\2\n.\3\2\2\2\f\62\3\2\2\2\169\3\2\2\2\20=")
        buf.write("\3\2\2\2\22N\3\2\2\2\24Y\3\2\2\2\26\33\5\4\3\2\27\30\5")
        buf.write("\24\13\2\30\31\7\2\2\3\31\33\3\2\2\2\32\26\3\2\2\2\32")
        buf.write("\27\3\2\2\2\33\3\3\2\2\2\34\35\7\b\2\2\35\36\7\f\2\2\36")
        buf.write("\37\5\24\13\2\37\5\3\2\2\2 \"\7\r\2\2!#\5\b\5\2\"!\3\2")
        buf.write("\2\2\"#\3\2\2\2#$\3\2\2\2$%\7\16\2\2%\7\3\2\2\2&+\5\n")
        buf.write("\6\2\'(\7\17\2\2(*\5\n\6\2)\'\3\2\2\2*-\3\2\2\2+)\3\2")
        buf.write("\2\2+,\3\2\2\2,\t\3\2\2\2-+\3\2\2\2./\7\3\2\2/\60\5\f")
        buf.write("\7\2\60\61\7\4\2\2\61\13\3\2\2\2\62\63\7\7\2\2\63\64\7")
        buf.write("\17\2\2\64\65\7\7\2\2\65\66\3\2\2\2\66\67\7\17\2\2\67")
        buf.write("8\7\7\2\28\r\3\2\2\29:\7\5\2\2:;\5\20\t\2;<\7\6\2\2<\17")
        buf.write("\3\2\2\2=>\7\7\2\2>?\7\17\2\2?@\7\7\2\2@A\3\2\2\2AB\7")
        buf.write("\17\2\2BC\7\7\2\2CD\3\2\2\2DE\7\17\2\2EF\7\7\2\2FG\3\2")
        buf.write("\2\2GH\7\17\2\2HI\7\7\2\2I\21\3\2\2\2JO\5\6\4\2KO\5\16")
        buf.write("\b\2LO\5\n\6\2MO\7\b\2\2NJ\3\2\2\2NK\3\2\2\2NL\3\2\2\2")
        buf.write("NM\3\2\2\2O\23\3\2\2\2PQ\b\13\1\2QR\7\3\2\2RS\5\24\13")
        buf.write("\2ST\7\4\2\2TZ\3\2\2\2UV\7\n\2\2VZ\5\24\13\bWZ\5\22\n")
        buf.write("\2XZ\7\7\2\2YP\3\2\2\2YU\3\2\2\2YW\3\2\2\2YX\3\2\2\2Z")
        buf.write("f\3\2\2\2[\\\f\7\2\2\\]\7\13\2\2]e\5\24\13\b^_\f\6\2\2")
        buf.write("_`\7\t\2\2`e\5\24\13\7ab\f\5\2\2bc\7\n\2\2ce\5\24\13\6")
        buf.write("d[\3\2\2\2d^\3\2\2\2da\3\2\2\2eh\3\2\2\2fd\3\2\2\2fg\3")
        buf.write("\2\2\2g\25\3\2\2\2hf\3\2\2\2\t\32\"+NYdf")
        return buf.getvalue()


class SkylineParser ( Parser ):

    grammarFileName = "Skyline.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "<INVALID>", 
                     "<INVALID>", "'+'", "'-'", "'*'", "':='", "'['", "']'", 
                     "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NUM", "ID", "SUM", "SUB", "MUL", "ASIG", 
                      "BEGL", "ENDL", "SEP", "WS" ]

    RULE_root = 0
    RULE_assignacio = 1
    RULE_skylinelist = 2
    RULE_elems = 3
    RULE_skylinebuilding = 4
    RULE_threenums = 5
    RULE_skylinerandom = 6
    RULE_fivenums = 7
    RULE_skylineobj = 8
    RULE_expressio = 9

    ruleNames =  [ "root", "assignacio", "skylinelist", "elems", "skylinebuilding", 
                   "threenums", "skylinerandom", "fivenums", "skylineobj", 
                   "expressio" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    NUM=5
    ID=6
    SUM=7
    SUB=8
    MUL=9
    ASIG=10
    BEGL=11
    ENDL=12
    SEP=13
    WS=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignacio(self):
            return self.getTypedRuleContext(SkylineParser.AssignacioContext,0)


        def expressio(self):
            return self.getTypedRuleContext(SkylineParser.ExpressioContext,0)


        def EOF(self):
            return self.getToken(SkylineParser.EOF, 0)

        def getRuleIndex(self):
            return SkylineParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = SkylineParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.state = 24
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.assignacio()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.expressio(0)
                self.state = 22
                self.match(SkylineParser.EOF)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignacioContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(SkylineParser.ID, 0)

        def ASIG(self):
            return self.getToken(SkylineParser.ASIG, 0)

        def expressio(self):
            return self.getTypedRuleContext(SkylineParser.ExpressioContext,0)


        def getRuleIndex(self):
            return SkylineParser.RULE_assignacio

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignacio" ):
                return visitor.visitAssignacio(self)
            else:
                return visitor.visitChildren(self)




    def assignacio(self):

        localctx = SkylineParser.AssignacioContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_assignacio)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(SkylineParser.ID)
            self.state = 27
            self.match(SkylineParser.ASIG)
            self.state = 28
            self.expressio(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SkylinelistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGL(self):
            return self.getToken(SkylineParser.BEGL, 0)

        def ENDL(self):
            return self.getToken(SkylineParser.ENDL, 0)

        def elems(self):
            return self.getTypedRuleContext(SkylineParser.ElemsContext,0)


        def getRuleIndex(self):
            return SkylineParser.RULE_skylinelist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSkylinelist" ):
                return visitor.visitSkylinelist(self)
            else:
                return visitor.visitChildren(self)




    def skylinelist(self):

        localctx = SkylineParser.SkylinelistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_skylinelist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(SkylineParser.BEGL)
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SkylineParser.T__0:
                self.state = 31
                self.elems()


            self.state = 34
            self.match(SkylineParser.ENDL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElemsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def skylinebuilding(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.SkylinebuildingContext)
            else:
                return self.getTypedRuleContext(SkylineParser.SkylinebuildingContext,i)


        def SEP(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.SEP)
            else:
                return self.getToken(SkylineParser.SEP, i)

        def getRuleIndex(self):
            return SkylineParser.RULE_elems

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElems" ):
                return visitor.visitElems(self)
            else:
                return visitor.visitChildren(self)




    def elems(self):

        localctx = SkylineParser.ElemsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_elems)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.skylinebuilding()
            self.state = 41
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SkylineParser.SEP:
                self.state = 37
                self.match(SkylineParser.SEP)
                self.state = 38
                self.skylinebuilding()
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SkylinebuildingContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.inner = None # ThreenumsContext

        def threenums(self):
            return self.getTypedRuleContext(SkylineParser.ThreenumsContext,0)


        def getRuleIndex(self):
            return SkylineParser.RULE_skylinebuilding

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSkylinebuilding" ):
                return visitor.visitSkylinebuilding(self)
            else:
                return visitor.visitChildren(self)




    def skylinebuilding(self):

        localctx = SkylineParser.SkylinebuildingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_skylinebuilding)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(SkylineParser.T__0)
            self.state = 45
            localctx.inner = self.threenums()
            self.state = 46
            self.match(SkylineParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ThreenumsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.NUM)
            else:
                return self.getToken(SkylineParser.NUM, i)

        def SEP(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.SEP)
            else:
                return self.getToken(SkylineParser.SEP, i)

        def getRuleIndex(self):
            return SkylineParser.RULE_threenums

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThreenums" ):
                return visitor.visitThreenums(self)
            else:
                return visitor.visitChildren(self)




    def threenums(self):

        localctx = SkylineParser.ThreenumsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_threenums)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(SkylineParser.NUM)

            self.state = 49
            self.match(SkylineParser.SEP)
            self.state = 50
            self.match(SkylineParser.NUM)

            self.state = 52
            self.match(SkylineParser.SEP)
            self.state = 53
            self.match(SkylineParser.NUM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SkylinerandomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.inner = None # FivenumsContext

        def fivenums(self):
            return self.getTypedRuleContext(SkylineParser.FivenumsContext,0)


        def getRuleIndex(self):
            return SkylineParser.RULE_skylinerandom

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSkylinerandom" ):
                return visitor.visitSkylinerandom(self)
            else:
                return visitor.visitChildren(self)




    def skylinerandom(self):

        localctx = SkylineParser.SkylinerandomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_skylinerandom)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(SkylineParser.T__2)
            self.state = 56
            localctx.inner = self.fivenums()
            self.state = 57
            self.match(SkylineParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FivenumsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.NUM)
            else:
                return self.getToken(SkylineParser.NUM, i)

        def SEP(self, i:int=None):
            if i is None:
                return self.getTokens(SkylineParser.SEP)
            else:
                return self.getToken(SkylineParser.SEP, i)

        def getRuleIndex(self):
            return SkylineParser.RULE_fivenums

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFivenums" ):
                return visitor.visitFivenums(self)
            else:
                return visitor.visitChildren(self)




    def fivenums(self):

        localctx = SkylineParser.FivenumsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_fivenums)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(SkylineParser.NUM)

            self.state = 60
            self.match(SkylineParser.SEP)
            self.state = 61
            self.match(SkylineParser.NUM)

            self.state = 63
            self.match(SkylineParser.SEP)
            self.state = 64
            self.match(SkylineParser.NUM)

            self.state = 66
            self.match(SkylineParser.SEP)
            self.state = 67
            self.match(SkylineParser.NUM)

            self.state = 69
            self.match(SkylineParser.SEP)
            self.state = 70
            self.match(SkylineParser.NUM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SkylineobjContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def skylinelist(self):
            return self.getTypedRuleContext(SkylineParser.SkylinelistContext,0)


        def skylinerandom(self):
            return self.getTypedRuleContext(SkylineParser.SkylinerandomContext,0)


        def skylinebuilding(self):
            return self.getTypedRuleContext(SkylineParser.SkylinebuildingContext,0)


        def ID(self):
            return self.getToken(SkylineParser.ID, 0)

        def getRuleIndex(self):
            return SkylineParser.RULE_skylineobj

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSkylineobj" ):
                return visitor.visitSkylineobj(self)
            else:
                return visitor.visitChildren(self)




    def skylineobj(self):

        localctx = SkylineParser.SkylineobjContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_skylineobj)
        try:
            self.state = 76
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SkylineParser.BEGL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.skylinelist()
                pass
            elif token in [SkylineParser.T__2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.skylinerandom()
                pass
            elif token in [SkylineParser.T__0]:
                self.enterOuterAlt(localctx, 3)
                self.state = 74
                self.skylinebuilding()
                pass
            elif token in [SkylineParser.ID]:
                self.enterOuterAlt(localctx, 4)
                self.state = 75
                self.match(SkylineParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressioContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.inner = None # ExpressioContext

        def expressio(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SkylineParser.ExpressioContext)
            else:
                return self.getTypedRuleContext(SkylineParser.ExpressioContext,i)


        def SUB(self):
            return self.getToken(SkylineParser.SUB, 0)

        def skylineobj(self):
            return self.getTypedRuleContext(SkylineParser.SkylineobjContext,0)


        def NUM(self):
            return self.getToken(SkylineParser.NUM, 0)

        def MUL(self):
            return self.getToken(SkylineParser.MUL, 0)

        def SUM(self):
            return self.getToken(SkylineParser.SUM, 0)

        def getRuleIndex(self):
            return SkylineParser.RULE_expressio

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressio" ):
                return visitor.visitExpressio(self)
            else:
                return visitor.visitChildren(self)



    def expressio(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SkylineParser.ExpressioContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_expressio, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 79
                self.match(SkylineParser.T__0)
                self.state = 80
                localctx.inner = self.expressio(0)
                self.state = 81
                self.match(SkylineParser.T__1)
                pass

            elif la_ == 2:
                self.state = 83
                self.match(SkylineParser.SUB)
                self.state = 84
                self.expressio(6)
                pass

            elif la_ == 3:
                self.state = 85
                self.skylineobj()
                pass

            elif la_ == 4:
                self.state = 86
                self.match(SkylineParser.NUM)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 100
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 98
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = SkylineParser.ExpressioContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressio)
                        self.state = 89
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 90
                        self.match(SkylineParser.MUL)
                        self.state = 91
                        self.expressio(6)
                        pass

                    elif la_ == 2:
                        localctx = SkylineParser.ExpressioContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressio)
                        self.state = 92
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 93
                        self.match(SkylineParser.SUM)
                        self.state = 94
                        self.expressio(5)
                        pass

                    elif la_ == 3:
                        localctx = SkylineParser.ExpressioContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expressio)
                        self.state = 95
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 96
                        self.match(SkylineParser.SUB)
                        self.state = 97
                        self.expressio(4)
                        pass

             
                self.state = 102
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[9] = self.expressio_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expressio_sempred(self, localctx:ExpressioContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         




