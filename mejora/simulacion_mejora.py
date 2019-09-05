# -*- coding: utf-8 -*-
import numpy as np
import random

#Simulación sistema de colas, ver bosquejo: imagen "mejora.png"


#Inicializar variables
#Generar primer arribo
#Ver si hay servidor libre
    #Si hay, se genera salida, se atiende, estado servidor pasa a ocupado
        #Termina el servicio y se pone en la cola de menor gente
            #ENTRA AL OTRO SISTEMA que es MM1
    #Si no hay libre, poner en cola.

#INICIALIZAMOS VARIABLES
fin_simulacion = 10000 #tiempo fin simulación
#Política de atención en cola A: FIFO, LIFO, PRIORIDAD, RANDOM
pol_atencion_cola_A = 'FIFO' #Hacer función que ordene la cola según este campo
#Variables estadístias
tiempo_medio_e_arribos_cola_A = 1
tiempo_medio_servicio_B = 1/4 #para B1, B2, B3 y B4; los declaramos una vez porque todos tienen el mismo
tiempo_medio_servicio_D = 1/2 #para D1, D2, D3 y D4; los declaramos una vez porque todos tienen el mismo

#Reloj del simulación
reloj = 0
#Lista de eventos
prox_arribo_B = reloj + np.random.exponential(tiempo_medio_e_arribos_cola_A) #generamos primer arribo
prox_partidas_B = [10.0**30,10.0**30,10.0**30,10.0**30]#[prox partida B1,prox partida B2,prox partida B3,prox partida B4]
prox_arribo_D = 10.0**30 #Lo seteamos en infinito
prox_partidas_D = [10.0**30,10.0**30] #[prox partida D1,prox partida D2]


#Estado del sistema
#Estado servidores: 0:libre, 1:ocupado
#Servidores B
estado_servidores_B = np.zeros(4) #[estado B1,estado B2,estado B3,estado B4]
num_clientes_cola_A = 0 #número de clientes en cola
cola_A = [] #pol_atencion
#Servidores D
estado_servidores_D = np.zeros(2) #[estado D1,estado D2]
num_clientes_cola_C = 0 #número de clientes en cola
tiempos_arribo_cola_C = []  #guardamos los tiempos para la cola C
cola_C = [] #FIFO
tiempo_ultimo_evento = 0.0

#Contadores estadísticos
#Número de clientes que completaron demoras en cola
num_completo_demora_A = 0
num_completo_demora_C = 0 #num cli completó demora C
#Demoras acumuladas en cola
demora_acum_A = 0
demora_acum_C = 0 #demora acumulada C
#Q(t): área debajo de la función número de clientes en cola
area_num_clientes_cola_A = 0
area_num_clientes_cola_C = 0
#B(t): aŕea debajo de la función servidor ocupado: 1 si está ocupado, 0 si está desocupad
area_estado_servidores_B = np.zeros(4) #[area B1,area B2,area B3,area B4]
area_estado_servidores_D = np.zeros(2) #[area D1,area D2]

#Necesarias para avanzar en el tiempo
tiempo_proximo_evento = 0.0
tipo_proximo_evento = ""
#Ai: arribo i, i nombre y número servidor
#Pi: partida i, i nombre y número servidor
tipos_eventos = ['AB','PB','AD','PD']
#tipos_eventos = ['AB','PB1','PB2','PB3','PB4','AD1','AD2','PD1','PD2']

#Función que determina el tiempo del próximo evento y el tipo
def tiempos():
    global reloj, prox_arribo_B, prox_partidas_B, prox_arribo_D, prox_partidas_D, tiempo_proximo_evento,tipo_proximo_evento,tiempo_ultimo_evento
    #Ponemos en infinito el tiempo del próximo evento
    #Vamos a buscar el menor tiempo entre: prox_arribo_B, prox_partidas_B(1,2,3 y 4), prox_arribo_D, prox_partidas_D(1,2)
    tiempo_proximo_evento = 10.0**30
    print('-------> prox_arribo_B',prox_arribo_B)
    print('-------> prox_partidas_B',prox_partidas_B)
    print('-------> prox_arribo_D',prox_arribo_D)
    print('-------> prox_partidas_D',prox_partidas_D)

    if prox_arribo_B <= tiempo_proximo_evento:
        tiempo_proximo_evento = prox_arribo_B
        tipo_proximo_evento = 'AB'
    for e in prox_partidas_B:
        if e <= tiempo_proximo_evento:
            tiempo_proximo_evento = e
            tipo_proximo_evento = 'PB'
    if prox_arribo_D <= tiempo_proximo_evento:
        tiempo_proximo_evento = prox_arribo_D
        tipo_proximo_evento = 'AD'
    for i in prox_partidas_D:
        if i <= tiempo_proximo_evento:
            tiempo_proximo_evento = i
            tipo_proximo_evento = 'PD'





    #Cambiamos reloj al próximo tiempo
    reloj = tiempo_proximo_evento
    print('** tiempo_proximo_evento',tiempo_proximo_evento,'tipo_proximo_evento',tipo_proximo_evento)
    return

#Funciones para cada tipo de evento
def arribo_B():
    global reloj,prox_arribo_B,tiempo_medio_e_arribos_cola_A,estado_servidores_B,tiempo_medio_servicio_B,prox_partidas_B,num_completo_demora_A,area_estado_servidores_B,num_clientes_cola_A,cola_A,area_num_clientes_cola_A,tiempo_ultimo_evento
    print('arribo B',reloj)
    #Un arribo genera un arribo
    prox_arribo_B = reloj + np.random.exponential(tiempo_medio_e_arribos_cola_A) #generamos próximo arribo
    #Veo si hay algún servidor B libre
    servidores_libres = []
    for e in range(len(estado_servidores_B)):
        #Vemos qué servidores están libres
        if estado_servidores_B[e] == 0:
            servidores_libres.append(e)

    if len(servidores_libres)>0:
        #Elegimos al azar un servidor
        if len(servidores_libres)==1:
            cola = servidores_libres[0]
        else:
            cola = random.choice(servidores_libres)

        #El servidor no está ocupado, tiene demora 0
        #estado_servidores_B = [estado B1,estado B2,estado B3,estado B4]
        estado_servidores_B[cola] = 1

        #calculamos partida
        prox_partidas_B[cola] = reloj + np.random.exponential(tiempo_medio_servicio_B) #generamos próximo partida B
        #Sumamos 1 al número de clientes que completaron demora
        num_completo_demora_A += 1
        #Actualizamos área debajo de la función servidor ocupado
        area_estado_servidores_B[cola] += (prox_partidas_B[cola] - reloj)#(reloj - tiempo_ultimo_evento)
        #Guardamos el tiempo del último evento
        tiempo_ultimo_evento = reloj

    else:
        #Todos los servidores están ocupados, se agrega a la cola
        num_clientes_cola_A += 1 #sumamos 1 al número de clientes en cola A
        cola_A.append(prox_arribo_B) #guardamos el tiempo de arribo del cliente
        #Actualizamos área debajo de la función número de clientes en cola
        area_num_clientes_cola_A += num_clientes_cola_A*(reloj-tiempo_ultimo_evento)
    return

def partida_B():
    global reloj,prox_partidas_B, num_clientes_cola_A,tiempo_ultimo_evento,area_num_clientes_cola_A,num_completo_demora_A,tiempo_medio_servicio_B,demora_acum_A,cola_A,estado_servidores_B,num_clientes_cola_C,tiempos_arribo_cola_C,prox_arribo_D, estado_servidores_D
    print('partida B',reloj)
    #Identificamos servidor que se va a desocupar
    servidor = 0
    #Recorro arreglo que tiene las próximas partidas de B
    for i in range(len(prox_partidas_B)):
        #Comparo el tiempo actual con cada partida
        if prox_partidas_B[i] == reloj:
            #Si el tiempo actual es igual al tiempo "i" del arreglo guardo la posición para identificar al servidor
            servidor = i
    #Vemos si hay clientes en cola
    if num_clientes_cola_A > 0:
        #La cola no está vacía
        #Actualizamos área debajo de la función número de clientes en cola
        area_num_clientes_cola_A += num_clientes_cola_A*(reloj-tiempo_ultimo_evento)
        #Guardamos el tiempo del último evento
        tiempo_ultimo_evento = reloj

        #Vamos a atender al próximo cliente con este servidor
        #Restamos 1 al número de clientes en cola
        num_clientes_cola_A -= 1
        #Calculamos la demora
        demora = reloj - cola_A[0]
        #Actualizamos demora acumulada
        demora_acum_A += demora
        #Sumamos 1 al número de clientes que completaron demora
        num_completo_demora_A += 1
        #Generamos próxima partida
        prox_partidas_B[servidor] = reloj + np.random.exponential(tiempo_medio_servicio_B) #generamos próximo partida B

        #Actualizamos área debajo de la función servidor ocupado
        area_estado_servidores_B[servidor] += (prox_partidas_B[servidor]-reloj)#(reloj - tiempo_ultimo_evento)

        #Si la cola no está vacía, mover cada cliente de la cola en una posición
        #if num_clientes_cola_A != 0:
        cola_A.pop(0)

    else:
        #print('cola vacía')
        #La cola está vacía
        #Marcamos servidor como libre
        estado_servidores_B[servidor] = 0
        #Seteamos próxima partida en infinito
        prox_partidas_B[servidor] = 10.0**30
        #print(estado_servidores_B,prox_partidas_B)

    #El cliente que se va pasa a la siguiente cola
    tiempos_arribo_cola_C.append(reloj)
    prox_arribo_D = tiempos_arribo_cola_C[0]

    return

def arribo_D():
    global reloj,prox_arribo_D,tiempos_arribo_cola_C,estado_servidores_D,tiempo_medio_servicio_D,prox_partidas_D,num_completo_demora_C,area_estado_servidores_D,num_clientes_cola_C,cola_C,area_num_clientes_cola_C, demora_acum_C, tiempo_ultimo_evento
    print('arribo D',reloj)
    #eliminamos el arribo ya usado
    tiempos_arribo_cola_C.pop(0)
    #Un arribo genera un arribo
    if len(tiempos_arribo_cola_C) > 0:
        prox_arribo_D = reloj + tiempos_arribo_cola_C[0]
        #Eliminamos el arribo ya usado
        #tiempos_arribo_cola_C.pop(0) #lo tengo que borrar apenas ocurre no si hay mas, ademas me da mal el len()
    else:
        prox_arribo_D = 10.0**30

    #Vemos si hay algún servidor D libre
    if estado_servidores_D[0] == 0 and estado_servidores_D[1]== 0:
        #Elegimos al azar un servidor
        opciones = [0,1]
        op = random.choice(opciones)
        estado_servidores_D[op] = 1
        #calculamos partida
        prox_partidas_D[op] = reloj + np.random.exponential(tiempo_medio_servicio_D) #generamos próxima partida D
        #Sumamos 1 al número de clientes que completaron demora
        num_completo_demora_C += 1
        #Actualizamos área debajo de la función servidor ocupado
        area_estado_servidores_D[op] += (prox_partidas_D[op] - reloj)#(reloj - tiempo_ultimo_evento)
        #Guardamos el tiempo del último evento
        tiempo_ultimo_evento = reloj
    elif estado_servidores_D[0] == 0:
        estado_servidores_D[0] = 1
        #calculamos partida
        prox_partidas_D[0] = reloj + np.random.exponential(tiempo_medio_servicio_D) #generamos próxima partida D
        #Sumamos 1 al número de clientes que completaron demora
        num_completo_demora_C += 1
        #Actualizamos área debajo de la función servidor ocupado
        area_estado_servidores_D[0] += (prox_partidas_D[0] - reloj)#(reloj - tiempo_ultimo_evento)
        #Guardamos el tiempo del último evento
        tiempo_ultimo_evento = reloj
    elif estado_servidores_D[1] == 0:
        estado_servidores_D[1] = 1
        #calculamos partida
        prox_partidas_D[1] = reloj + np.random.exponential(tiempo_medio_servicio_D) #generamos próxima partida D
        #Sumamos 1 al número de clientes que completaron demora
        num_completo_demora_C += 1
        #Actualizamos área debajo de la función servidor ocupado
        area_estado_servidores_D[1] += (prox_partidas_D[1] - reloj)#(reloj - tiempo_ultimo_evento)
        #Guardamos el tiempo del último evento
        tiempo_ultimo_evento = reloj
    else:
        #Todos los servidores están ocupados, se agrega a la cola
        num_clientes_cola_C += 1 #sumamos 1 al número de clientes en cola C
        cola_C.append(reloj) #guardamos el tiempo de arribo del cliente
        #Actualizamos área debajo de la función número de clientes en cola
        area_num_clientes_cola_C += num_clientes_cola_C*(reloj-tiempo_ultimo_evento)
    return




def partida_D():
    global reloj,cola_C,estado_servidores_D,num_clientes_cola_C,tiempos_arribo_cola_C,tiempo_ultimo_evento,num_completo_demora_C,demora_acum_C,area_num_clientes_cola_C,area_estado_servidores_D,prox_partidas_D
    print('partida D',reloj)
    #Identificamos servidor que se va a desocupar
    servidor = 0
    #Recorro arreglo que tiene las próximas partidas de D
    for i in range(len(prox_partidas_D)):
        #Comparo el tiempo actual con cada partida
        if prox_partidas_D[i] == reloj:
            #Si el tiempo actual es igual al tiempo "i" del arreglo guardo la posición para identificar al servidor
            servidor = i

    #Vemos si la cola está vacía
    if num_clientes_cola_C > 0:
        #Cola no vacía, paso a atender al próximo cliente
        #Actualizamos área debajo de la función número de clientes en cola
        area_num_clientes_cola_C += num_clientes_cola_C*(reloj-tiempo_ultimo_evento)

        tiempo_ultimo_evento = reloj
        #Atendemos al próximo cliente
        #Restamos 1 al número de clientes en cola
        num_clientes_cola_C -= 1
        #Calculamos la demora del cliente que está comenzando el servicio
        demora = reloj - cola_C[0]
        #Actualizamos demora acumulada
        demora_acum_C += demora
        #Agregamos uno al número de clientes que completaron su demora
        num_completo_demora_C += 1
        #Calculamos la partida del cliente
        prox_partidas_D[servidor] = reloj + np.random.exponential(tiempo_medio_servicio_D)
        #Actualizamos área debajo de la función servidor ocupado
        area_estado_servidores_D[servidor] += (prox_partidas_D[servidor]-reloj)#(reloj-tiempo_ultimo_evento)

        #Si la cola no está vacía, mover cada cliente de la cola en una posición

        cola_C.pop(0)

    else:
        #Cola vacía
        #Marcamos servidor como libre
        estado_servidores_D[servidor] = 0
        #Seteamos próxima partida en infinito
        prox_partidas_D[servidor] = 10.0**30

    return


def informes():
    global num_clientes_cola_A,num_clientes_cola_C,num_completo_demora_A,num_completo_demora_C,demora_acum_A,demora_acum_C,tiempo_ultimo_evento,area_num_clientes_cola_A,area_num_clientes_cola_C,area_estado_servidores_B,area_estado_servidores_D
    print('Informes')

    #print('Número clientes en cola A:', num_clientes_cola_A)
    #print('Número clientes en cola C:', num_clientes_cola_C)

    print('Tiempo de simulación:',reloj)
    print('Tiempo último evento:', tiempo_ultimo_evento)

    print('Número clientes que completaron demora en cola A:',num_completo_demora_A)
    print('Número de clientes que completaron demora en cola C',num_completo_demora_C)

    try:
        print('Demora promedio en cola A:',abs(demora_acum_A/num_completo_demora_A))
    except ZeroDivisionError:
        print('No hay demora acumulada en cola A, ningún cliente completó demora')
    try:
        print('Demora promedio en cola C:', demora_acum_C/num_completo_demora_C)
    except ZeroDivisionError:
        print('No hay demora acumulada en cola C, ningún cliente completó demora')

    try:
        print('Q(t): número promedio de clientes en cola A:',area_num_clientes_cola_A/tiempo_ultimo_evento)
    except ZeroDivisionError:
        pass
    try:
        print('Q(t): número promedio de clientes en cola C:',area_num_clientes_cola_C/tiempo_ultimo_evento)
    except ZeroDivisionError:
        pass


    try:
        print('B(t): utilización promedio del servidor B1:',area_estado_servidores_B[0]/tiempo_ultimo_evento)
    except ZeroDivisionError:
        pass
    try:
        print('B(t): utilización promedio del servidor B2:',area_estado_servidores_B[1]/tiempo_ultimo_evento)
    except ZeroDivisionError:
        pass
    try:
        print('B(t): utilización promedio del servidor B3:',area_estado_servidores_B[2]/tiempo_ultimo_evento)
    except ZeroDivisionError:
        pass
    try:
        print('B(t): utilización promedio del servidor B4:',area_estado_servidores_B[3]/tiempo_ultimo_evento)
    except ZeroDivisionError:
        pass
    try:
        print('B(t): utilización promedio del servidor D1:',area_estado_servidores_D[0]/tiempo_ultimo_evento)
    except ZeroDivisionError:
        pass
    try:
        print('B(t): utilización promedio del servidor D2:',area_estado_servidores_D[1]/tiempo_ultimo_evento)
    except ZeroDivisionError:
        pass

    return

def programa_principal():
    global reloj, fin_simulacion,tipo_proximo_evento

    while reloj <= fin_simulacion:
        tiempos()
        if tipo_proximo_evento == 'AB':
            arribo_B()
        elif tipo_proximo_evento == 'PB':
            partida_B()
        elif tipo_proximo_evento == 'AD':
            arribo_D()
        elif tipo_proximo_evento == 'PD':
            partida_D()
        else:
            print('Error, no hay ningún evento de ese tipo')

    informes()

    return

programa_principal()
