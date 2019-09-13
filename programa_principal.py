# -*- coding: utf-8 -*-
from pick import pick
from estado_estacionario import *

que_hacer = 'Qué vamos a simular? El sistema planteado normal o el mejorado?: '
opciones_que_hacer = ['SISTEMA NORMAL', 'SISTEMA MEJORADO']
opcion_que_hacer, index = pick(opciones_que_hacer, que_hacer)

if opcion_que_hacer == 'SISTEMA NORMAL':
    print(opcion_que_hacer)
    politica_cola = 'Por favor elija la política de la cola A: '
    politicas = ['FIFO', 'LIFO', 'RANDOM', 'PRIORIDAD']
    politica, index = pick(politicas, politica_cola)
    print('Política',politica)
    estado_estacionario(politica)
else:
    print(opcion_que_hacer)
    estado_estacionario('MEJORADO')
