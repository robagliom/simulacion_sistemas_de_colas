# -*- coding: utf-8 -*-
import numpy as np

#Reloj del simulación
reloj = 0
#Lista de eventos
prox_arribo_B = 10.0**30
prox_partidas_B = [10.0**30,10.0**30,10.0**30,10.0**30]#[prox partida B1,prox partida B2,prox partida B3,prox partida B4]
prox_arribo_D1 = 10.0**30 #Lo seteamos en infinito
prox_partida_D1 = 10.0**30 #Lo seteamos en infinito
prox_arribo_D2 = 10.0**30 #Lo seteamos en infinito
prox_partida_D2 = 10.0**30 #Lo seteamos en infinito

#Estado del sistema
#Estado servidores: 0:libre, 1:ocupado
#Servidores B
estado_servidores_B = np.zeros(4) #[estado B1,estado B2,estado B3,estado B4]
num_clientes_cola_A = 0 #número de clientes en cola
cola_A = [] #pol_atencion
#Servidores D
estado_servidores_D = np.zeros(2) #[estado D1,estado D2]
num_clientes_cola_C1 = 0 #número de clientes en cola
num_clientes_cola_C2 = 0 #número de clientes en cola
tiempos_arribo_cola_C1 = [] #guardamos los tiempos para la cola C1
cola_C1 = [] #FIFO
tiempos_arribo_cola_C2 = [] #guardamos los tiempos para la cola C2
cola_C2 = [] #FIFO
tiempo_ultimo_evento = 0.0

#Contadores estadísticos
#Número de clientes que completaron demoras en cola
num_completo_demora_A = 0
num_completo_demora_C = np.zeros(2) #[num cli completó demora C1,num cli completó demora C2]
#Demoras acumuladas en cola
demora_acum_A = 0
demora_acum_C = np.zeros(2) #[demora acumulada C1,demora acumulada C2]
#Q(t): área debajo de la función número de clientes en cola
area_num_clientes_cola_A = 0
area_num_clientes_cola_C1 = 0
area_num_clientes_cola_C2 = 0
#B(t): aŕea debajo de la función servidor ocupado: 1 si está ocupado, 0 si está desocupad
area_estado_servidores_B = np.zeros(4) #[area B1,area B2,area B3,area B4]
area_estado_servidores_D = np.zeros(2) #[area D1,area D2]

#Necesarias para avanzar en el tiempo
tiempo_proximo_evento = 0.0
tipo_proximo_evento = ""
#Ai: arribo i, i nombre y número servidor
#Pi: partida i, i nombre y número servidor
tipos_eventos = ['AB','PB','AD1','AD2','PD1','PD2']
