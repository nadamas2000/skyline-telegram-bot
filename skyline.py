import random as rnd

debug = False


# -------------------- Funcions estàtiques --------------------------
def takeBuilding(i, h, f):
    """ Retorna una línia de parells [posició x, alçada] donada per
     l'inici i, la altura h i el final f """
    r = []
    for x in range(i, f):
        r += [[x, h]]
    return r


def cloneHList(hList):
    """ Retorna una còpia de les dades hList """
    ret = []
    for i in hList:
        ret += [i.copy()]
    return ret


def intersection(a, b):
    """ Retorna el resultat de la operació d'intersecció de Skylines """
    ia, ib, ret = 0, 0, []
    while ia < len(a) and ib < len(b):
        if a[ia][0] == b[ib][0]:
            ret += [[a[ia][0], min(a[ia][1], b[ib][1])]]
            ia += 1
            ib += 1
        elif a[ia][0] > b[ib][0]:
            ib += 1
        elif a[ia][0] < b[ib][0]:
            ia += 1
    return ret


def union(a, b):
    """ Retorna el resultat de la operació de unió de Skylines """
    if not len(a):
        return b
    if not len(b):
        return a

    ia, ib, ret = 0, 0, []
    while ia < len(a) or ib < len(b):
        if ia >= len(a):
            for j in range(ib, len(b)):
                ret += [b[ib]]
                ib += 1
            break
        if ib >= len(b):
            for j in range(ia, len(a)):
                ret += [a[ia]]
                ia += 1
            break
        if a[ia][0] == b[ib][0]:
            ret += [[a[ia][0], max(a[ia][1], b[ib][1])]]
            ia += 1
            ib += 1
        elif a[ia][0] > b[ib][0]:
            ret += [b[ib]]
            ib += 1
        elif a[ia][0] < b[ib][0]:
            ret += [a[ia]]
            ia += 1
    return ret


def gen(n, h, w, xmin, xmax):
    """ Genera un Skyline aleatori mitjanzant les dades
     n: Nombre de edificis
     h: Alçada màxima dels edificis
     w: Amplada màsima dels edificis
     xmin: Posició mínima del Skyline
     xmax: Posició màxima del Skyline """
    if n > 1:
        r1 = gen(int(n / 2), h, w, xmin, xmax)
        r2 = gen(n - int(n / 2), h, w, xmin, xmax)
        ret = union(r1, r2)
    else:
        i = rnd.randint(xmin, xmax)
        wb = rnd.randint(1, w)
        hb = rnd.randint(0, h)
        ret = takeBuilding(i, hb, i + wb)
    return ret


# ------------------Classe Skyline -----------------------
class Skyline:

    def __init__(self, *args, **kwargs):
        """ Mètode creador de la classe amb diferents tipus de dades:
         heightLine: Llista de parells [posició x, alçada]
         initial, height, final: Punt inicial, alçada, i punt final d'un edifici
         n, h, w, xmin, xmax: Amb descripcció anàloga a la funció (gen)

         També conté un mode de creació per defecte buit si no hi han paràmetres.
         En cas de que no es compleixin les restriccions de paràmetres i els seus
          noms es retornarà error """
        if 'heightLine' in kwargs and type(kwargs.get('heightLine')) is list:
            for i in kwargs.get('heightLine'):
                if i[1] < 0:
                    raise ValueError("No es permeten alçades negatives")
            self.__hLine = kwargs.get('heightLine')

        elif ('initial' in kwargs and type(kwargs.get('initial')) is int and
              'height' in kwargs and type(kwargs.get('height')) is int and
              'final' in kwargs and type(kwargs.get('final')) is int):
            h = kwargs.get('height')
            if h < 0:
                raise ValueError("No es permeten alçades negatives")
            f = kwargs.get('final')
            i = kwargs.get('initial')
            if f < i:
                raise ValueError("El punt inicial ha de ser inferior al punt final")
            self.__hLine = takeBuilding(i, h, f)

        elif ('n' in kwargs and kwargs.get('n') >= 0 and
              'h' in kwargs and kwargs.get('h') >= 0 and
              'w' in kwargs and kwargs.get('w') >= 0 and
              'xmin' in kwargs and
              'xmax' in kwargs):
            if kwargs.get('h') < 0:
                raise ValueError("No es permeten alçades negatives")
            if kwargs.get('w') < 0:
                raise ValueError("No es permeten amplades negatives")
            if kwargs.get('n') < 0:
                raise ValueError("El número d'edificis ha de ser >= 0")
            if kwargs.get('xmin') > kwargs.get('xmax'):
                raise ValueError("xmin ha de ser inferior a xmax")
            self.__hLine = gen(kwargs.get('n'),
                               kwargs.get('h'),
                               kwargs.get('w'),
                               kwargs.get('xmin'),
                               kwargs.get('xmax'))

        # Creació per defecte (buit)
        elif len(kwargs) == 0 and len(args) == 0:
            self.__hLine = []

        # Error en el pas de paràmetres
        else:
            for i in kwargs:
                print("%s: %s as type: %s" % (i, kwargs.get(i), type(kwargs.get(i))))
            txt1 = "Invalid parameters.\n"
            txt2 = "Correct params:\n"
            txt3 = "    (initial=(int), heightLine=(list)),\n"
            txt4 = "    (initial=(int), height=(int), final=(int))\n"
            txt5 = "    (n=(int), h=(int), w=(int), xmin=(int), xmax=(int))\n"
            txt6 = "    ()\n"
            txt = txt1 + txt2 + txt3 + txt4 + txt5 + txt6
            raise ValueError(txt)

    # -------------------- Consulta de dades ------------------------
    def getHLine(self):
        """ Retorna la línia d'alçades que es una llista de parells [posició x, alçada] """
        return self.__hLine

    def getH(self):
        """ Retorna la alçada màxima del Skyline"""
        m = 0
        for i in self.__hLine:
            m = max(m, i[1])
        return m

    def getArea(self):
        """ Retorna l'area del Skyline"""
        s = 0
        for i in self.__hLine:
            s += i[1]
        return s

    # -------------------------- Operadors --------------------------
    def __add__(self, other):
        """ Operació de suma d'un Skyline amb un enter, o unió amb un altre Skyline """
        if debug:
            print('Crida a suma amb:')
            print('   ', self)
            print('   ', other)
        if isinstance(other, int):
            hLine = []
            for i in self.__hLine:
                hLine += [[i[0] + other, i[1]]]
            return Skyline(heightLine=hLine)
        elif isinstance(other, Skyline):
            if debug:
                print('Prepara Unió')
            hLine = union(self.__hLine, other.getHLine())
            if debug:
                print(hLine)
                print('Unio amb:')
                print('   ', len(hLine), 'elements')
            return Skyline(heightLine=hLine)
        else:
            return NotImplemented

    def __radd__(self, other):
        """ Informa de que no es pot sumar/unir un Skyline a cap element que no sigui un Skyline"""
        raise ValueError('No es pot sumar/unir un Skyline a cap element que no sigui un Skyline')

    def __sub__(self, other):
        """ Operació de resta d'un Skyline amb un enter.
        Dona error si es amb cap altre element. """
        if isinstance(other, int):
            return Skyline(heightLine=self.__hLine) + (-other)
        else:
            return NotImplemented

    def __rsub__(self, other):
        """ Informa de que no es pot restar un Skyline a cap element """
        raise ValueError('No es pot restar un Skyline a cap element')

    def __neg__(self):
        """ Retorna el Skyline invertir en x """
        if debug:
            print('Entra a negació')
        hs = []
        for i in self.__hLine:
            hs.append(i[1])
        hs.reverse()
        if debug:
            print('hs reverse:', hs)
        hLine = [[self.__hLine[0][0], hs[0]]]
        lenght = len(self.__hLine)
        if debug:
            print('hLine:', hLine)
        for i in range(1, lenght):
            dif = self.__hLine[lenght - i][0] - self.__hLine[lenght - 1 - i][0]
            hLine.append([hLine[i - 1][0] + dif, hs[i]])
        return Skyline(heightLine=hLine)

    def __mul__(self, other):
        """ Realitza la operació de multimplicació amb enter, o intersecció amb un altre Skyline """
        if isinstance(other, int):
            hLine = []
            for i in range(0, other):
                new = cloneHList(self.__hLine)
                length = len(hLine)
                if i > 0:
                    lastValue = hLine[length - 1][0]
                    firstValue = hLine[0][0]
                    for j in new:
                        j[0] = j[0] + lastValue - firstValue + 1
                hLine += new
            return Skyline(heightLine=hLine)
        elif isinstance(other, Skyline):
            hLine = intersection(self.__hLine, other.__hLine)
            return Skyline(heightLine=hLine)
        return NotImplemented

    def __rmul__(self, other):
        """ Informa de que no es pot multiplicar/intersectar un Skyline a cap element que no sigui un Skyline"""
        raise ValueError('No es pot multiplicar/intersectar un Skyline a cap element que no sigui un Skyline')

    def __len__(self):
        """ Retorna el númro de alçades que conté el Skyline """
        return len(self.__hLine)

    def __repr__(self):
        """ Determina com es representa un Skyline a la linia de comandes """
        return '<Skyline hLine: %s>' % self.__hLine

    def __str__(self):
        """ Representa com es representa un Skyline en un String """
        return 'Skyline with area:%s and height line:%s' % \
               (self.getArea(), self.__hLine)
