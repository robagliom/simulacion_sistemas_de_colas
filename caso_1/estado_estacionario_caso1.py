# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

from simulacion_caso_1 import *

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
    #informe --> tupla
    informe = programa_principal()

    #0 demora_promedio_cola_A
    demora_promedio_acumulada_cola_A += informe[0]
    prom_demora_promedio_cola_A.append([i,demora_promedio_acumulada_cola_A/i])
    #1 demora_promedio_cola_C1
    demora_promedio_acumulada_cola_C1 += informe[1]
    prom_demora_promedio_cola_C1.append([i,demora_promedio_acumulada_cola_C1/i])
    #2 demora_promedio_cola_C2
    demora_promedio_acumulada_cola_C2 += informe[2]
    prom_demora_promedio_cola_C2.append([i,demora_promedio_acumulada_cola_C2/i])
    #3 nro_prom_clientes_cola_A
    nro_prom_acum_clientes_cola_A += informe[3]
    prom_nro_prom_clientes_cola_A.append([i,nro_prom_acum_clientes_cola_A/i])
    #4 nro_prom_clientes_cola_C1
    nro_prom_acum_clientes_cola_C1 += informe[4]
    prom_nro_prom_clientes_cola_C1.append([i,nro_prom_acum_clientes_cola_C1/i])
    #5 nro_prom_clientes_cola_C2
    nro_prom_acum_clientes_cola_C2 += informe[5]
    prom_nro_prom_clientes_cola_C2.append([i,nro_prom_acum_clientes_cola_C2/i])
    #6 utilizacion_prom_B1
    utilizacion_acum_B1 += informe[6]
    prom_utilizacion_B1.append([i,utilizacion_acum_B1/i])
    #7 utilizacion_prom_B2
    utilizacion_acum_B2 += informe[7]
    prom_utilizacion_B2.append([i,utilizacion_acum_B2/i])
    #8 utilizacion_prom_B3
    utilizacion_acum_B3 += informe[8]
    prom_utilizacion_B3.append([i,utilizacion_acum_B3/i])
    #9 utilizacion_prom_B4
    utilizacion_acum_B4 += informe[9]
    prom_utilizacion_B4.append([i,utilizacion_acum_B4/i])
    #10 utilizacion_prom_D1
    utilizacion_acum_D1 += informe[10]
    prom_utilizacion_D1.append([i,utilizacion_acum_D1/i])
    #11 utilizacion_prom_D2
    utilizacion_acum_D2 += informe[11]
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
