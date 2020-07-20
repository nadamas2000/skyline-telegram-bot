if __name__ is not None and "." in __name__:
    from .SkylineParser import SkylineParser
    from .SkylineVisitor import SkylineVisitor
else:
    from SkylineParser import SkylineParser
    from SkylineVisitor import SkylineVisitor
import sys

sys.path.append('../')
from skyline import Skyline

localData = {}
debug = False


class EvalVisitor(SkylineVisitor):
    """ Clase que extendeix SkylineVisitor per operar amb Skylines """
    def __init__(self, *args):
        """ Creadora que carrega la memoria que es passa per paràmetre """
        if len(args):
            localData.update(args[0])

    def visitRoot(self, ctx: SkylineParser.RootContext):
        """ Crida i retorna els Skylines calculats """
        lst = [n for n in ctx.getChildren()]
        if len(lst) == 0:
            return ""
        else:
            n = next(ctx.getChildren())
            return self.visit(n)

    def visitSkylinelist(self, ctx: SkylineParser.SkylinelistContext):
        """ Estableix la crida i retorn de la creació de Skylines per llista d'edificis """
        lst = [n for n in ctx.getChildren()]
        n = lst[1]
        sl = self.visit(n)
        return sl

    def visitElems(self, ctx: SkylineParser.ElemsContext):
        """ Realitza la operació de creació de Skylines amb llista d'edificis """
        lst = [n for n in ctx.getChildren()]
        k = self.visit(lst[0])
        for i in lst:
            if i.getText() != ',':
                k += self.visit(i)
        return k

    def visitSkylinerandom(self, ctx: SkylineParser.SkylinerandomContext):
        """ Realitza la crida i retorn de creació de Skylines random """
        lst = [n for n in ctx.getChildren()]
        n = lst[1]
        sl = self.visit(n)
        return sl

    # Visit a parse tree produced by SkylineParser#fivenums.
    def visitFivenums(self, ctx: SkylineParser.FivenumsContext):
        """ Realitza la operació de creació de Skyline random """
        lst = [n for n in ctx.getChildren()]
        sln = int(lst[0].getText())
        slh = int(lst[2].getText())
        slw = int(lst[4].getText())
        slXMin = int(lst[6].getText())
        slXMax = int(lst[8].getText())
        sl = Skyline(n=sln, h=slh, w=slw, xmin=slXMin, xmax=slXMax)
        return sl

    def visitSkylineobj(self, ctx: SkylineParser.SkylineobjContext):
        """ Crida i retorn d'un Skyline amb qualsevol tipus de mode de creació """
        n = next(ctx.getChildren())
        sl = self.visit(n)
        return sl

    def visitSkylinebuilding(self, ctx: SkylineParser.SkylinebuildingContext):
        """ Crida i retorna la creació d'un edifici """
        lst = [n for n in ctx.getChildren()]
        n = lst[1]
        sl = self.visit(n)
        return sl

    def visitThreenums(self, ctx: SkylineParser.ThreenumsContext):
        """ Realitza la operació de creació d'un edifici i el retorna """
        lst = [n for n in ctx.getChildren()]
        i = int(lst[0].getText())
        h = int(lst[2].getText())
        f = int(lst[4].getText())
        sl = Skyline(initial=i, height=h, final=f)
        return sl

    def visitAssignacio(self, ctx: SkylineParser.AssignacioContext):
        """ Realitza la operació d'assignació, guarda el resultat a memoria
         i retorna la assignació amb el resultat """
        lst = [n for n in ctx.getChildren()]
        ID = lst[0].getText()
        localData[ID] = self.visit(lst[2])
        return ID, localData[ID]

    def visitExpressio(self, ctx: SkylineParser.ExpressioContext):
        """ Determina quin tipus de operació o expressió s'està demanant,
        realitza el seu càlcul, i retorna el resultat."""
        lst = [n for n in ctx.getChildren()]
        if len(lst) == 1:
            if debug:
                print('Entra a Longitut 1')
                for i in lst:
                    print(i.getText())
            n = next(ctx.getChildren())
            if n.getText()[0] not in [str(num) for num in range(0, 9, 1)]:
                if n.getText()[0].isalpha():
                    if n.getText() not in localData:
                        raise ValueError("Variable no definida")
                    else:
                        return localData[n.getText()]
                else:
                    sl = self.visit(n)
                    return sl
            else:
                return int(lst[0].getText())
        elif len(lst) == 2:
            if debug:
                print('Entra a Longitut 2')
                for i in lst:
                    print(i.getText())
            sl = self.visit(lst[1])
            if debug:
                print(sl)
            return -sl
        elif len(lst) == 3:
            if debug:
                print('Entra a Longitut 3')
                for i in lst:
                    print(i.getText())
            if lst[0].getText() == '(' and lst[2].getText() == ')':
                return self.visit(lst[1])
            else:
                if lst[1].getText() == '+':
                    return self.visit(lst[0]) + self.visit(lst[2])
                elif lst[1].getText() == '-':
                    return self.visit(lst[0]) - self.visit(lst[2])
                elif lst[1].getText() == '*':
                    return self.visit(lst[0]) * self.visit(lst[2])
