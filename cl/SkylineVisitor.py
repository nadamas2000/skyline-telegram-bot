# Generated from Skyline.g by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
else:
    from SkylineParser import SkylineParser

# This class defines a complete generic visitor for a parse tree produced by SkylineParser.

class SkylineVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SkylineParser#root.
    def visitRoot(self, ctx:SkylineParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#assignacio.
    def visitAssignacio(self, ctx:SkylineParser.AssignacioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#skylinelist.
    def visitSkylinelist(self, ctx:SkylineParser.SkylinelistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#elems.
    def visitElems(self, ctx:SkylineParser.ElemsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#skylinebuilding.
    def visitSkylinebuilding(self, ctx:SkylineParser.SkylinebuildingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#threenums.
    def visitThreenums(self, ctx:SkylineParser.ThreenumsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#skylinerandom.
    def visitSkylinerandom(self, ctx:SkylineParser.SkylinerandomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#fivenums.
    def visitFivenums(self, ctx:SkylineParser.FivenumsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#skylineobj.
    def visitSkylineobj(self, ctx:SkylineParser.SkylineobjContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SkylineParser#expressio.
    def visitExpressio(self, ctx:SkylineParser.ExpressioContext):
        return self.visitChildren(ctx)



del SkylineParser