# -*- coding: utf-8 -*-
import sys
from pick import pick
from estado_estacionario import *

def main():
    que_hacer = 'Qué vamos a simular? El sistema planteado normal o el mejorado?: '
    opciones_que_hacer = ['SISTEMA NORMAL', 'SISTEMA MEJORADO', 'X SALIR']
    opcion_que_hacer, index = pick(opciones_que_hacer, que_hacer)

    if opcion_que_hacer == 'SISTEMA NORMAL':
        print(opcion_que_hacer)
        politica_cola = 'Por favor elija la política de la cola A: '
        politicas = ['FIFO', 'LIFO', 'RANDOM', 'PRIORIDAD','FIFO CON UNA COLA C','X VOLVER']
        politica, index = pick(politicas, politica_cola)
        print('Política',politica)
        if politica == 'X VOLVER':
            main()
        else:
            estado_estacionario(politica)
    elif opcion_que_hacer == 'SISTEMA MEJORADO':
        print(opcion_que_hacer)
        estado_estacionario('MEJORA')
    else:
        sys.exit()
        #return

main()
