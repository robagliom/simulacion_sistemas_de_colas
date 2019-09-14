# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd

from caso_1.simulacion_caso_1 import programa_principal_FIFO
from caso_2.simulacion_caso_2 import programa_principal_LIFO
from caso_3.simulacion_caso_3 import programa_principal_RANDOM
from caso_4.simulacion_caso_4 import programa_principal_PRIORIDAD
from caso_5.simulacion_caso_5 import programa_principal_COLACUNICA
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
        elif politica == 'FIFO CON UNA COLA C':
            informe = programa_principal_COLACUNICA(fin_simulacion)
        elif politica == 'MEJORA':
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
    if politica == 'FIFO CON UNA COLA C':
        #Gráfica demora promedio en cola C
        plt.subplot(212)
        x, y = zip(*[m for m in prom_demora_promedio_cola_C1])
        plt.title('Demora promedio en cola C')  # Colocamos el título
        plt.plot(x, y)
        plt.grid(True)
        plt.xlabel('Corridas')
        plt.ylabel('Demora')
    else:
        #Gráfica demora promedio en cola C1
        plt.subplot(223)
        x, y = zip(*[m for m in prom_demora_promedio_cola_C1])
        plt.title('Demora promedio en cola C1')  # Colocamos el título
        plt.plot(x, y)
        plt.grid(True)
        plt.xlabel('Corridas')
        plt.ylabel('Demora')
        #Gráfica demora promedio en cola C2
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
    if politica == 'FIFO CON UNA COLA C':
        #Gráfica número promedio en cola C
        plt.subplot(212)
        x, y = zip(*[m for m in prom_nro_prom_clientes_cola_C1])
        plt.title('Número promedio de clientes en cola C')  # Colocamos el título
        plt.plot(x, y)
        plt.grid(True)
        plt.xlabel('Corridas')
        plt.ylabel('Número')
    else:
        #Gráfica número promedio en cola C1
        plt.subplot(223)
        x, y = zip(*[m for m in prom_nro_prom_clientes_cola_C1])
        plt.title('Número promedio de clientes en cola C1')  # Colocamos el título
        plt.plot(x, y)
        plt.grid(True)
        plt.xlabel('Corridas')
        plt.ylabel('Número')
        #Gráfica número promedio en cola C2
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
    if politica == 'MEJORA':
        #Gráfica Utilización promedio servidor B1
        plt.subplot(111)
        x, y = zip(*[m for m in prom_utilizacion_B1])
        plt.plot(x, y)
        plt.title('Utilización promedio servidor B')  # Colocamos el título
        plt.grid(True)
        plt.xlabel('Corridas')
        plt.ylabel('Utilización')
    else:
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

    #Muestro tabla con valores
    if politica == 'MEJORA':
        filas = ['Demora promedio en cola A','Demora promedio en cola C1','Demora promedio en cola C2','Número promedio de clientes en cola A','Número promedio de clientes en cola C1','Número promedio de clientes en cola C2','Utilización promedio del servidor B','Utilización promedio del servidor D1','Utilización promedio del servidor D2']
        columna = ['Valores promedios obtenidos luego de {} corridas'.format(corridas)]
        resultados=[[demora_promedio_acumulada_cola_A/corridas],[demora_promedio_acumulada_cola_C1/corridas],[demora_promedio_acumulada_cola_C2/corridas],[nro_prom_acum_clientes_cola_A/corridas],[nro_prom_acum_clientes_cola_C1/corridas],[nro_prom_acum_clientes_cola_C2/corridas],[utilizacion_acum_B1/corridas],[utilizacion_acum_D1/corridas],[utilizacion_acum_D2/corridas]]
    elif politica == 'FIFO CON UNA COLA C':
        filas = ['Demora promedio en cola A','Demora promedio en cola C','Número promedio de clientes en cola A','Número promedio de clientes en cola C','Utilización promedio del servidor B1','Utilización promedio del servidor B2','Utilización promedio del servidor B3','Utilización promedio del servidor B4','Utilización promedio del servidor D1','Utilización promedio del servidor D2']
        columna = ['Valores promedios obtenidos luego de {} corridas'.format(corridas)]
        resultados=[[demora_promedio_acumulada_cola_A/corridas],[demora_promedio_acumulada_cola_C1/corridas],[nro_prom_acum_clientes_cola_A/corridas],[nro_prom_acum_clientes_cola_C1/corridas],[utilizacion_acum_B1/corridas],[utilizacion_acum_B2/corridas],[utilizacion_acum_B3/corridas],[utilizacion_acum_B4/corridas],[utilizacion_acum_D1/corridas],[utilizacion_acum_D2/corridas]]
        #resultados2=[demora_promedio_acumulada_cola_A/corridas,demora_promedio_acumulada_cola_C1/corridas,nro_prom_acum_clientes_cola_A/corridas,nro_prom_acum_clientes_cola_C1/corridas,utilizacion_acum_B1/corridas,utilizacion_acum_B2/corridas,utilizacion_acum_B3/corridas,utilizacion_acum_B4/corridas,utilizacion_acum_D1/corridas,utilizacion_acum_D2/corridas]
    else:
        filas = ['Demora promedio en cola A','Demora promedio en cola C1','Demora promedio en cola C2','Número promedio de clientes en cola A','Número promedio de clientes en cola C1','Número promedio de clientes en cola C2','Utilización promedio del servidor B1','Utilización promedio del servidor B2','Utilización promedio del servidor B3','Utilización promedio del servidor B4','Utilización promedio del servidor D1','Utilización promedio del servidor D2']
        columna = ['Valores promedios obtenidos luego de {} corridas'.format(corridas)]
        resultados=[[demora_promedio_acumulada_cola_A/corridas],[demora_promedio_acumulada_cola_C1/corridas],[demora_promedio_acumulada_cola_C2/corridas],[nro_prom_acum_clientes_cola_A/corridas],[nro_prom_acum_clientes_cola_C1/corridas],[nro_prom_acum_clientes_cola_C2/corridas],[utilizacion_acum_B1/corridas],[utilizacion_acum_B2/corridas],[utilizacion_acum_B3/corridas],[utilizacion_acum_B4/corridas],[utilizacion_acum_D1/corridas],[utilizacion_acum_D2/corridas]]
        #resultados2=[demora_promedio_acumulada_cola_A/corridas,demora_promedio_acumulada_cola_C1/corridas,demora_promedio_acumulada_cola_C2/corridas,nro_prom_acum_clientes_cola_A/corridas,nro_prom_acum_clientes_cola_C1/corridas,nro_prom_acum_clientes_cola_C2/corridas,utilizacion_acum_B1/corridas,utilizacion_acum_B2/corridas,utilizacion_acum_B3/corridas,utilizacion_acum_B4/corridas,utilizacion_acum_D1/corridas,utilizacion_acum_D2/corridas]

    #data = {'Valores promedios obtenidos':resultados2}
    #df = pd.DataFrame(data, index=filas)
    #print(df)

    fig, ax = plt.subplots()
    # hide axes
    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')

    the_table = ax.table(cellText=resultados,
                          rowLabels=filas,
                          colLabels=columna,
                          colWidths=[0.4,0.6],
                          loc='center')
    #the_table.scale(0.5*2,1.5*13)
    the_table.auto_set_font_size(False)
    the_table.set_fontsize(12)
    fig.tight_layout()
    plt.show()

    from programa_principal import main

    return main()

#estado_estacionario('FIFO')
