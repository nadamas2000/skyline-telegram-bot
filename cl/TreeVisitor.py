if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
    from .SkylineVisitor import SkylineVisitor
else:
    from SkylineParser import SkylineParser
    from SkylineVisitor import SkylineVisitor
import sys

sys.path.append('../')
from skyline import Skyline


class TreeVisitor(SkylineVisitor):
    """ Clase que extendeix SkylineVisitor per mostrar l'arbre d'intermpretació del llenguatge """
    def __init__(self):
        """ Creadora que estableix el nivell d'identació a 0 """
        self.nivell = 0

    def visitRoot(self, ctx: SkylineParser.RootContext):
        """ Mètode de crida de l'arrel i el mostra per pantalla"""
        n = next(ctx.getChildren())
        print('  ' * self.nivell + 'ROOT')
        self.nivell += 1
        return self.visit(n)
        self.nivell -= 1

    def visitElems(self, ctx: SkylineParser.ElemsContext):
        """ Mètode de crida als elementes de la creació d'un Skylines per llista d'edificis """
        l = [n for n in ctx.getChildren()]
        for i in l:
            if i.getText() != ',':
                self.visit(i)

    # Visit a parse tree produced by SkylineParser#fivenums.
    def visitFivenums(self, ctx: SkylineParser.FivenumsContext):
        """ Mètode de representació d'un Skyline creat de forma random """
        l = [n for n in ctx.getChildren()]
        sln = int(l[0].getText())
        slh = int(l[2].getText())
        slw = int(l[4].getText())
        slxmin = int(l[6].getText())
        slxmax = int(l[8].getText())
        sl = Skyline(n=sln, h=slh, w=slw, xmin=slxmin, xmax=slxmax)
        self.nivell += 2
        print("  " * self.nivell + ("%s" % sl))
        self.nivell -= 2
        return sl

    def visitThreenums(self, ctx: SkylineParser.ThreenumsContext):
        """ Mètode de representació d'un skyline amb un edifici """
        l = [n for n in ctx.getChildren()]
        i = int(l[0].getText())
        h = int(l[2].getText())
        f = int(l[4].getText())
        sl = Skyline(initial=i, height=h, final=f)
        self.nivell += 2
        print("  " * self.nivell + ("%s" % sl))
        self.nivell -= 2
        return sl

    def visitAssignacio(self, ctx: SkylineParser.AssignacioContext):
        """ Mètode de representació d'una assignació """
        l = [n for n in ctx.getChildren()]
        print("  " * self.nivell + ':=' )
        print("  " + 'ID(' + l[0].getText() + ')')
        self.nivell += 1
        self.visit(l[2])
        self.nivell -= 1

    def visitExpressio(self, ctx: SkylineParser.ExpressioContext):
        """ Mètode de crida i representació de les operacions i elements """
        if ctx.getChildCount() == 1:
            n = next(ctx.getChildren())
            if n.getText()[0] not in [str(num) for num in range(0, 9, 1)]:
                print("  " * self.nivell +
                      'SKYLINE' +
                      '(' + n.getText() + ')')
                self.nivell -= 1
                self.visit(n)
            else:
                print("  " * self.nivell +
                      SkylineParser.symbolicNames[n.getSymbol().type] +
                      '(' + n.getText() + ')')
                self.nivell -= 1
        elif ctx.getChildCount() == 2:
            lst = [n for n in ctx.getChildren()]
            print('  ' * self.nivell + 'NEG(-)')
            self.nivell += 1
            self.visit(lst[1])
            self.nivell -= 1
        elif ctx.getChildCount() == 3:
            lst = [n for n in ctx.getChildren()]
            if lst[0].getText() == '(' and lst[2].getText() == ')':
                print('  ' * self.nivell + '()')
                self.nivell += 1
                self.visit(lst[1])
                self.nivell -= 1
            else:
                switcher = {
                    '+': ('  ' * self.nivell + 'MES(+)'),
                    '-': ('  ' * self.nivell + 'MENS(-)'),
                    '*': ('  ' * self.nivell + 'MULT(*)')
                }
                print(switcher.get(lst[1].getText(), "operació invàlida"))
                self.nivell += 1
                self.visit(lst[0])
                self.nivell += 1
                self.visit(lst[2])
                self.nivell -= 1
