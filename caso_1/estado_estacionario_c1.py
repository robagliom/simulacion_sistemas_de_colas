# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

from simulacion_caso_1 import *

corridas = 1000
prom_demora_promedio_cola_A = []
demora_promedio_acumulada_cola_A = 0

for i in range(1,corridas+1):
    #informe --> tupla
    #0 demora_promedio_cola_A
    #1 demora_promedio_cola_C1
    #2 demora_promedio_cola_C2
    #3 nro_prom_clientes_cola_A
    #4 nro_prom_clientes_cola_C1
    #5 nro_prom_clientes_cola_C2
    #6 utilizacion_prom_B1
    #7 utilizacion_prom_B2
    #8 utilizacion_prom_B3
    #9 utilizacion_prom_B4
    #10 utilizacion_prom_D1
    #11 utilizacion_prom_D2
    informe = programa_principal()

    demora_promedio_acumulada_cola_A += informe[0]
    prom_demora_promedio_cola_A.append([i,demora_promedio_acumulada_cola_A/i]) #+= informe[0]


#Gráfica demora promedio en cola A
x, y = zip(*[m for m in prom_demora_promedio_cola_A])
plt.title('Demora promedio en cola A')  # Colocamos el título
plt.plot(x, y,'ro-', markersize=0.5, lw=0.5)
#plt.plot([esperanza for i in range(n)], linestyle='dashed', color='blue')
plt.grid(True)
plt.xlabel('Corridas')
plt.ylabel('Demora')
plt.show()
