# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

from caso_1.simulacion_caso_1 import programa_principal_FIFO
from caso_2.simulacion_caso_2 import programa_principal_LIFO
from caso_3.simulacion_caso_3 import programa_principal_RANDOM
from caso_4.simulacion_caso_4 import programa_principal_PRIORIDAD
from mejora.simulacion_mejora import programa_principal_MEJORA

fin_simulacion = 1000

def estado_estacionario(politica):
    corridas = 1000

    prom_demora_promedio_cola_A = []
    demora_promedio_acumulada_cola_A = 0
    prom_demora_promedio_cola_C1 = []
    demora_promedio_acumulada_cola_C1 = 0
    prom_demora_promedio_cola_C2 = []
    demora_promedio_acumulada_cola_C2 = 0
    prom_nro_prom_clientes_cola_A = []
    nro_prom_acum_clientes_cola_A = 0
    prom_nro_prom_clientes_cola_C1 = []
    nro_prom_acum_clientes_cola_C1 = 0
    prom_nro_prom_clientes_cola_C2 = []
    nro_prom_acum_clientes_cola_C2 = 0
    prom_utilizacion_B1 = []
    utilizacion_acum_B1 = 0
    prom_utilizacion_B2 = []
    utilizacion_acum_B2 = 0
    prom_utilizacion_B3 = []
    utilizacion_acum_B3 = 0
    prom_utilizacion_B4 = []
    utilizacion_acum_B4 = 0
    prom_utilizacion_D1 = []
    utilizacion_acum_D1 = 0
    prom_utilizacion_D2 = []
    utilizacion_acum_D2 = 0

    for i in range(1,corridas+1):

        #informe --> diccionario
        if politica == 'FIFO':
            informe = programa_principal_FIFO(fin_simulacion)
        elif politica == 'LIFO':
            informe = programa_principal_LIFO(fin_simulacion)
        elif politica == 'RANDOM':
            informe = programa_principal_RANDOM(fin_simulacion)
        elif politica == 'PRIORIDAD':
            informe = programa_principal_PRIORIDAD(fin_simulacion)
        elif politica == 'MEJORADO':
            informe = programa_principal_MEJORA(fin_simulacion)
        else:
            print('Error en la política')
            break

        demoras = informe['demora_colas']
        clientes = informe['numero_clientes']
        servidores = informe['utilizacion_servidores']

        #0 demora_promedio_cola_A
        if 'A' in demoras:
            demora_promedio_acumulada_cola_A += demoras['A']
            prom_demora_promedio_cola_A.append([i,demora_promedio_acumulada_cola_A/i])
        #1 demora_promedio_cola_C1
        if 'C1' in demoras:
            demora_promedio_acumulada_cola_C1 += demoras['C1']
            prom_demora_promedio_cola_C1.append([i,demora_promedio_acumulada_cola_C1/i])
        #2 demora_promedio_cola_C2
        if 'C2' in demoras:
            demora_promedio_acumulada_cola_C2 += demoras['C2']
            prom_demora_promedio_cola_C2.append([i,demora_promedio_acumulada_cola_C2/i])
        #3 nro_prom_clientes_cola_A
        if 'A' in clientes:
            nro_prom_acum_clientes_cola_A += clientes['A']
            prom_nro_prom_clientes_cola_A.append([i,nro_prom_acum_clientes_cola_A/i])
        #4 nro_prom_clientes_cola_C1
        if 'C1' in clientes:
            nro_prom_acum_clientes_cola_C1 += clientes['C1']
            prom_nro_prom_clientes_cola_C1.append([i,nro_prom_acum_clientes_cola_C1/i])
        #5 nro_prom_clientes_cola_C2
        if 'C2' in clientes:
            nro_prom_acum_clientes_cola_C2 += clientes['C2']
            prom_nro_prom_clientes_cola_C2.append([i,nro_prom_acum_clientes_cola_C2/i])
        #6 utilizacion_prom_B1
        if 'B1' in servidores:
            utilizacion_acum_B1 += servidores['B1']
            prom_utilizacion_B1.append([i,utilizacion_acum_B1/i])
        #7 utilizacion_prom_B2
        if 'B2' in servidores:
            utilizacion_acum_B2 += servidores['B2']
            prom_utilizacion_B2.append([i,utilizacion_acum_B2/i])
        #8 utilizacion_prom_B3
        if 'B3' in servidores:
            utilizacion_acum_B3 += servidores['B3']
            prom_utilizacion_B3.append([i,utilizacion_acum_B3/i])
        #9 utilizacion_prom_B4
        if 'B4' in servidores:
            utilizacion_acum_B4 += servidores['B4']
            prom_utilizacion_B4.append([i,utilizacion_acum_B4/i])
        #10 utilizacion_prom_D1
        if 'D1' in servidores:
            utilizacion_acum_D1 += servidores['D1']
            prom_utilizacion_D1.append([i,utilizacion_acum_D1/i])
        #11 utilizacion_prom_D2
        if 'D2' in servidores:
            utilizacion_acum_D2 += servidores['D2']
            prom_utilizacion_D2.append([i,utilizacion_acum_D2/i])

    #Demora promedio en cola
    plt.figure(1)
    #Gráfica demora promedio en cola A
    plt.subplot(211)
    x, y = zip(*[m for m in prom_demora_promedio_cola_A])
    plt.plot(x, y)
    plt.title('Demora promedio en cola A')  # Colocamos el título
    plt.grid(True)
    plt.xlabel('Corridas')
    plt.ylabel('Demora')
    #Gráfica demora promedio en cola C1
    plt.subplot(223)
    x, y = zip(*[m for m in prom_demora_promedio_cola_C1])
    plt.title('Demora promedio en cola C1')  # Colocamos el título
    plt.plot(x, y)
    plt.grid(True)
    plt.xlabel('Corridas')
    plt.ylabel('Demora')
    #Gráfica demora promedio en cola C2
    if len(prom_demora_promedio_cola_C2)>0:
        plt.subplot(224)
        x, y = zip(*[m for m in prom_demora_promedio_cola_C2])
        plt.title('Demora promedio en cola C2')  # Colocamos el título
        plt.plot(x, y)
        plt.grid(True)
        plt.xlabel('Corridas')
        plt.ylabel('Demora')

    plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25, wspace=0.35)
    plt.show()

    #Número promedio de clientes en cola
    plt.figure(2)
    #Gráfica número promedio en cola A
    plt.subplot(211)
    x, y = zip(*[m for m in prom_nro_prom_clientes_cola_A])
    plt.plot(x, y)
    plt.title('Número promedio de clientes en cola A')  # Colocamos el título
    plt.grid(True)
    plt.xlabel('Corridas')
    plt.ylabel('Número')
    #Gráfica número promedio en cola C1
    plt.subplot(223)
    x, y = zip(*[m for m in prom_nro_prom_clientes_cola_C1])
    plt.title('Número promedio de clientes en cola C1')  # Colocamos el título
    plt.plot(x, y)
    plt.grid(True)
    plt.xlabel('Corridas')
    plt.ylabel('Número')
    #Gráfica número promedio en cola C2
    if len(prom_nro_prom_clientes_cola_C2)>0:
        plt.subplot(224)
        x, y = zip(*[m for m in prom_nro_prom_clientes_cola_C2])
        plt.title('Número promedio de clientes en cola C2')  # Colocamos el título
        plt.plot(x, y)
        plt.grid(True)
        plt.xlabel('Corridas')
        plt.ylabel('Número')

    plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25, wspace=0.35)
    plt.show()

    #Utilización promedio servidores B
    plt.figure(3)
    #Gráfica Utilización promedio servidor B1
    plt.subplot(221)
    x, y = zip(*[m for m in prom_utilizacion_B1])
    plt.plot(x, y)
    plt.title('Utilización promedio servidor B1')  # Colocamos el título
    plt.grid(True)
    plt.xlabel('Corridas')
    plt.ylabel('Utilización')
    #Gráfica Utilización promedio servidor B2
    plt.subplot(222)
    x, y = zip(*[m for m in prom_utilizacion_B2])
    plt.plot(x, y)
    plt.title('Utilización promedio servidor B2')  # Colocamos el título
    plt.grid(True)
    plt.xlabel('Corridas')
    plt.ylabel('Utilización')
    #Gráfica Utilización promedio servidor B3
    plt.subplot(223)
    x, y = zip(*[m for m in prom_utilizacion_B3])
    plt.title('Utilización promedio servidor B3')  # Colocamos el título
    plt.plot(x, y)
    plt.grid(True)
    plt.xlabel('Corridas')
    plt.ylabel('Utilización')
    #Gráfica Utilización promedio servidor B4
    plt.subplot(224)
    x, y = zip(*[m for m in prom_utilizacion_B4])
    plt.title('Utilización promedio servidor B4')  # Colocamos el título
    plt.plot(x, y)
    plt.grid(True)
    plt.xlabel('Corridas')
    plt.ylabel('Utilización')

    plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25, wspace=0.35)
    plt.show()

    #Utilización promedio servidores D
    plt.figure(4)
    #Gráfica Utilización promedio servidor D1
    plt.subplot(211)
    x, y = zip(*[m for m in prom_utilizacion_D1])
    plt.plot(x, y)
    plt.title('Utilización promedio servidor D1')  # Colocamos el título
    plt.grid(True)
    plt.xlabel('Corridas')
    plt.ylabel('Utilización')
    #Gráfica Utilización promedio servidor D2
    plt.subplot(212)
    x, y = zip(*[m for m in prom_utilizacion_D2])
    plt.plot(x, y)
    plt.title('Utilización promedio servidor D2')  # Colocamos el título
    plt.grid(True)
    plt.xlabel('Corridas')
    plt.ylabel('Utilización')

    plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25, wspace=0.35)
    plt.show()


    #Muestro valores
    print('Valores promedios obtenidos luego de ',corridas,'corridas:')
    print('Demora promedio en cola A',demora_promedio_acumulada_cola_A /corridas)
    print('Demora promedio en cola C1',demora_promedio_acumulada_cola_C1/corridas)
    print('Demora promedio en cola C2',demora_promedio_acumulada_cola_C2/corridas)
    print('Número promedio de clientes en cola A',nro_prom_acum_clientes_cola_A/corridas)
    print('Número promedio de clientes en cola C1',nro_prom_acum_clientes_cola_C1/corridas)
    print('Número promedio de clientes en cola C2',nro_prom_acum_clientes_cola_C2/corridas)
    print('Utilización promedio del servidor B1',utilizacion_acum_B1/corridas)
    print('Utilización promedio del servidor B2',utilizacion_acum_B2/corridas)
    print('Utilización promedio del servidor B3',utilizacion_acum_B3/corridas)
    print('Utilización promedio del servidor B4',utilizacion_acum_B4/corridas)
    print('Utilización promedio del servidor C1',utilizacion_acum_D1/corridas)
    print('Utilización promedio del servidor C2',utilizacion_acum_D2/corridas)

    return

#estado_estacionario('FIFO')
