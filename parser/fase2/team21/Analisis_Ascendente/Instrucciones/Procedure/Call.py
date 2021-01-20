from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.instruccion import Instruccion
from tytus.parser.fase2.team21.Analisis_Ascendente.Instrucciones.Expresiones.Expresion import *

class Call(Instruccion):
    def __init__(self, caso, id, listaE, linea, columna):
        self.caso = caso
        self.id = id
        self.listaE = listaE
        self.linea = linea
        self.columna = columna


    def traducir(call, ts, consola, exception, tv, regla, antes, optimizado):
        if call.listaE == None:
            consola.append(f'\t{call.id}()\n')
        else:
            temporales = []
            for e in call.listaE:
                t = Expresion.traducir(e, ts, consola, exception, tv, regla, antes, optimizado, None)
                temporales.append(t)

            i = 0
            params = ""
            for te in temporales:
                params += te
                if i + 1 != len(temporales):
                    params += ', '
                i = i + 1
            consola.append(f'\t{call.id}({params})\n')