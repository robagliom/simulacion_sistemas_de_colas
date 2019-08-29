# -*- coding: utf-8 -*-
import numpy as np
import random

#Simulación sistema de colas, ver bosquejo: imagen "caso_1.png"


#Inicializar variables
#Generar primer arribo
#Ver si hay servidor libre
    #Si hay, se genera salida, se atiende, estado servidor pasa a ocupado
        #Termina el servicio y se pone en la cola de menor gente
            #ENTRA AL OTRO SISTEMA que es MM1
    #Si no hay libre, poner en cola.

#INICIALIZAMOS VARIABLES
fin_simulacion = 10000#tiempo fin simulación
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
#tipos_eventos = ['AB','PB1','PB2','PB3','PB4','AD1','AD2','PD1','PD2']

#Función que determina el tiempo del próximo evento y el tipo
def tiempos():
    global reloj, prox_arribo_B, prox_partidas_B, prox_arribo_D1, prox_arribo_D2, prox_partida_D1, prox_partida_D2,tiempo_proximo_evento,tipo_proximo_evento,tiempo_ultimo_evento
    #Ponemos en infinito el tiempo del próximo evento
    #Vamos a buscar el menor tiempo entre: prox_arribo_B, prox_partidas_B(1,2,3 y 4), prox_arribo_D1, prox_arribo_D2, prox_partida_D1, prox_partida_D2
    tiempo_proximo_evento = 10.0**30
    print('-------> prox_arribo_B',prox_arribo_B)
    print('-------> prox_partidas_B',prox_partidas_B)
    print('-------> prox_arribo_D1',prox_arribo_D1)
    print('-------> prox_arribo_D2',prox_arribo_D2)
    print('-------> prox_partida_D1',prox_partida_D1)
    print('-------> prox_partida_D2',prox_partida_D2)

    if prox_arribo_B <= tiempo_proximo_evento:
        tiempo_proximo_evento = prox_arribo_B
        tipo_proximo_evento = 'AB'
    for e in prox_partidas_B:
        if e <= tiempo_proximo_evento:
            tiempo_proximo_evento = e
            tipo_proximo_evento = 'PB'
    if prox_arribo_D1<=tiempo_proximo_evento:
        tiempo_proximo_evento = prox_arribo_D1
        tipo_proximo_evento = 'AD1'
    if prox_arribo_D2 <= tiempo_proximo_evento:
        tiempo_proximo_evento = prox_arribo_D2
        tipo_proximo_evento = 'AD2'
    if prox_partida_D1 <= tiempo_proximo_evento:
        tiempo_proximo_evento = prox_partida_D1
        tipo_proximo_evento = 'PD1'
    if prox_partida_D2 <= tiempo_proximo_evento:
        tiempo_proximo_evento = prox_partida_D2
        tipo_proximo_evento = 'PD2'

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
    servidor_B_libre = False
    for e in range(len(estado_servidores_B)):
        if estado_servidores_B[e] == 0:
            #El servidor no está ocupado, tiene demora 0
            #estado_servidores_B = [estado B1,estado B2,estado B3,estado B4]
            estado_servidores_B[e] = 1
            #Auxiliar
            servidor_B_libre = True
            #calculamos partida
            prox_partidas_B[e] = reloj + np.random.exponential(tiempo_medio_servicio_B) #generamos próximo partida B
            #Sumamos 1 al número de clientes que completaron demora
            num_completo_demora_A += 1
            #Actualizamos área debajo de la función servidor ocupado
            area_estado_servidores_B[e] += (prox_partidas_B[e] - reloj)#(reloj - tiempo_ultimo_evento)
            #Guardamos el tiempo del último evento
            tiempo_ultimo_evento = reloj

            break
    if not servidor_B_libre:
        #Todos los servidores están ocupados, se agrega a la cola
        num_clientes_cola_A += 1 #sumamos 1 al número de clientes en cola A
        cola_A.append(prox_arribo_B) #guardamos el tiempo de arribo del cliente
        #Actualizamos área debajo de la función número de clientes en cola
        area_num_clientes_cola_A += num_clientes_cola_A*(reloj-tiempo_ultimo_evento)
    return

def partida_B():
    global reloj,prox_partidas_B, num_clientes_cola_A,tiempo_ultimo_evento,area_num_clientes_cola_A,num_completo_demora_A,tiempo_medio_servicio_B,demora_acum_A,cola_A,estado_servidores_B,num_clientes_cola_C1,num_clientes_cola_C2,tiempos_arribo_cola_C1,tiempos_arribo_cola_C2,prox_arribo_D1,prox_arribo_D2,estado_servidores_D
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
        if num_clientes_cola_A != 0:
            for i in range(1, num_clientes_cola_A):
                j = i + 1
                cola_A[i]=cola_A[j]

    else:
        #print('cola vacía')
        #La cola está vacía
        #Marcamos servidor como libre
        estado_servidores_B[servidor] = 0
        #Seteamos próxima partida en infinito
        prox_partidas_B[servidor] = 10.0**30
        #print(estado_servidores_B,prox_partidas_B)

    #El cliente que se va pasa a la siguiente cola
    #Cliente va a la cola con menor cantidad
    #Primero vemos si las dos colas están vacía, en ese caso ver si un servidor está vacío y usar ese, sino ir a cualquier cosa
    if num_clientes_cola_C1 == 0 and num_clientes_cola_C2 == 0:
        #Vemos si el servidor D1 está desocupado
        if estado_servidores_D[0] == 0:
            tiempos_arribo_cola_C1.append(reloj)
            prox_arribo_D1 = tiempos_arribo_cola_C1[0]
        #Vemos si el servidor D2 está desocupado
        elif estado_servidores_D[1] == 0:
            tiempos_arribo_cola_C2.append(reloj)
            prox_arribo_D2 = tiempos_arribo_cola_C2[0]
        else:
            #Los dos seridores están ocupados
            opciones = [1,2] #Opción 1: cola C1; opción 2: cola C2
            cola = random.choice(opciones)
            if cola == 1:
                tiempos_arribo_cola_C1.append(reloj)
                prox_arribo_D1 = tiempos_arribo_cola_C1[0]
            else:
                tiempos_arribo_cola_C2.append(reloj)
                prox_arribo_D2 = tiempos_arribo_cola_C2[0]
    else:
        if num_clientes_cola_C1 <= num_clientes_cola_C2:
            tiempos_arribo_cola_C1.append(reloj)
            prox_arribo_D1 = tiempos_arribo_cola_C1[0]
        else:
            tiempos_arribo_cola_C2.append(reloj)
            prox_arribo_D2 = tiempos_arribo_cola_C2[0]

    return

def arribo_D1():
    global reloj,cola_C1,prox_arribo_D1, estado_servidores_D,num_clientes_cola_C1,tiempos_arribo_cola_C1,tiempo_ultimo_evento,num_completo_demora_C,demora_acum_C,area_num_clientes_cola_C1,area_estado_servidores_D,prox_partida_D1
    print('arribo D1',reloj)

    #Guardamos el próximo arribo
    if len(tiempos_arribo_cola_C1) > 0:
        prox_arribo_D1 = reloj + tiempos_arribo_cola_C1[0]
        #Eliminamos el arribo ya usado
        tiempos_arribo_cola_C1.pop(0)
    else:
        prox_arribo_D1 = 10.0**30

    #Vemos si el servidor está ocupado
    #D[0]: D1
    if estado_servidores_D[0] == 1:
        #Servidor D1 ocupado
        #Actualizamos área debajo del número de clientes en cola C1
        area_num_clientes_cola_C1 += num_clientes_cola_C1*(reloj-tiempo_ultimo_evento)
        #Actualizamos el tiempo del último evento al actual
        tiempo_ultimo_evento = reloj
        #Agregamos 1 al número de clientes en cola
        num_clientes_cola_C1 += 1
        #Guardamos el tiempo de arribo del cliente
        cola_C1.append(tiempo_ultimo_evento)
    else:
        #Servidor libre, paso a atender al cliente
        #No tiene demora
        #Cambio estado del servidor a ocupado
        estado_servidores_D[0] = 1
        #Agregamos 1 al número de clientes que completaron demora
        num_completo_demora_C[0] += 1
        #Generamos la salida del cliente
        prox_partida_D1 = reloj + np.random.exponential(tiempo_medio_servicio_D)
        #Actualizamos área debajo de la función servidor ocupado
        area_estado_servidores_D[0] += (prox_partida_D1-reloj)#(reloj - tiempo_ultimo_evento)

    return

def arribo_D2():
    global reloj,cola_C2,prox_arribo_D2, estado_servidores_D,num_clientes_cola_C2,tiempos_arribo_cola_C2,tiempo_ultimo_evento,num_completo_demora_C,demora_acum_C,area_num_clientes_cola_C2,area_estado_servidores_D,prox_partida_D2
    print('arribo D2',reloj)
    #Guardamos el próximo arribo
    if len(tiempos_arribo_cola_C2) > 0:
        prox_arribo_D2 = reloj + tiempos_arribo_cola_C2[0]
        #Eliminamos el arribo ya usado
        tiempos_arribo_cola_C2.pop(0)
    else:
        prox_arribo_D2 = 10.0**30

    #Vemos si el servidor está ocupado
    #D[1]: D2
    if estado_servidores_D[1] == 1:
        #Servidor D2 ocupado
        #Actualizamos área debajo del número de clientes en cola C2
        area_num_clientes_cola_C2 += num_clientes_cola_C2*(reloj-tiempo_ultimo_evento)
        #Actualizamos el tiempo del último evento al actual
        tiempo_ultimo_evento = reloj
        #Agregamos 1 al número de clientes en cola
        num_clientes_cola_C2 += 1
        #Guardamos el tiempo de arribo del cliente
        cola_C2.append(tiempo_ultimo_evento)
    else:
        #Servidor libre, paso a atender al cliente
        #No tiene demora
        #Cambio estado del servidor a ocupado
        estado_servidores_D[1] = 1
        #Agregamos 1 al número de clientes que completaron demora
        num_completo_demora_C[1] += 1
        #Generamos la salida del cliente
        prox_partida_D2 = reloj + np.random.exponential(tiempo_medio_servicio_D)
        #Actualizamos área debajo de la función servidor ocupado
        area_estado_servidores_D[1] += (prox_partida_D2-reloj)#(reloj-tiempo_ultimo_evento)

    return

def partida_D1():
    global reloj,cola_C1,prox_arribo_D1, estado_servidores_D,num_clientes_cola_C1,tiempos_arribo_cola_C1,tiempo_ultimo_evento,num_completo_demora_C,demora_acum_C,area_num_clientes_cola_C1,area_estado_servidores_D,prox_partida_D1
    print('partida D1',reloj)

    #Vemos si la cola está vacía
    if num_clientes_cola_C1 > 0:
        #Cola no vacía, paso a atender al próximo cliente
        #Actualizamos área debajo de la función número de clientes en cola
        area_num_clientes_cola_C1 += num_clientes_cola_C1*(reloj-tiempo_ultimo_evento)

        tiempo_ultimo_evento = reloj
        #Atendemos al próximo cliente
        #Restamos 1 al número de clientes en cola
        num_clientes_cola_C1 -= 1
        #Calculamos la demora del cliente que está comenzando el servicio
        demora = reloj - cola_C1[0]
        #Actualizamos demora acumulada
        demora_acum_C[0] += demora
        #Agregamos uno al número de clientes que completaron su demora
        num_completo_demora_C[0] += 1
        #Calculamos la partida del cliente
        prox_partida_D1 = reloj + np.random.exponential(tiempo_medio_servicio_D)
        #Actualizamos área debajo de la función servidor ocupado
        area_estado_servidores_D[0] += (prox_partida_D1-reloj)#(reloj-tiempo_ultimo_evento)

        #Si la cola no está vacía, mover cada cliente de la cola en una posición
        if num_clientes_cola_C1 != 0:
            for i in range(1, num_clientes_cola_C1):
                j = i + 1
                cola_C1[i]=cola_C1[j]
    else:
        #Cola vacía
        #Marcamos servidor como libre
        estado_servidores_D[0] = 0
        #Seteamos próxima partida en infinito
        prox_partida_D1 = 10.0**30

    return

def partida_D2():
    global reloj,cola_C2,prox_arribo_D2, estado_servidores_D,num_clientes_cola_C2,tiempos_arribo_cola_C2,tiempo_ultimo_evento,num_completo_demora_C,demora_acum_C,area_num_clientes_cola_C2,area_estado_servidores_D,prox_partida_D2
    print('partida D2',reloj)

    #Vemos si la cola está vacía
    if num_clientes_cola_C2 > 0:
        #Cola no vacía, paso a atender al próximo cliente
        #Actualizamos área debajo de la función número de clientes en cola
        area_num_clientes_cola_C2 += num_clientes_cola_C2*(reloj-tiempo_ultimo_evento)

        tiempo_ultimo_evento = reloj
        #Atendemos al próximo cliente
        #Restamos 1 al número de clientes en cola
        num_clientes_cola_C2 -= 1
        #Calculamos la demora del cliente que está comenzando el servicio
        demora = reloj - cola_C2[0]
        #Actualizamos demora acumulada
        demora_acum_C[1] += demora
        #Agregamos uno al número de clientes que completaron su demora
        num_completo_demora_C[1] += 1
        #Calculamos la partida del cliente
        prox_partida_D2 = reloj + np.random.exponential(tiempo_medio_servicio_D)
        #Actualizamos área debajo de la función servidor ocupado
        area_estado_servidores_D[1] += (prox_partida_D2-reloj)#(reloj-tiempo_ultimo_evento)

        #Si la cola no está vacía, mover cada cliente de la cola en una posición
        if num_clientes_cola_C2 != 0:
            for i in range(1, num_clientes_cola_C2):
                j = i + 1
                cola_C2[i]=cola_C2[j]
    else:
        #Cola vacía
        #Marcamos servidor como libre
        estado_servidores_D[1] = 0
        #Seteamos próxima partida en infinito
        prox_partida_D2 = 10.0**30

    return

def informes():
    global num_clientes_cola_A,num_clientes_cola_C1,num_clientes_cola_C2,num_completo_demora_A,num_completo_demora_C,demora_acum_A,demora_acum_C,tiempo_ultimo_evento,area_num_clientes_cola_A,area_num_clientes_cola_C1,area_num_clientes_cola_C2,area_estado_servidores_B,area_estado_servidores_D
    print('Informes')

    #print('Número clientes en cola A:', num_clientes_cola_A)
    #print('Número clientes en cola C1:', num_clientes_cola_C1)
    #print('Número clientes en cola C2:', num_clientes_cola_C2)
    print('Tiempo de simulación:',reloj)
    print('Tiempo último evento:', tiempo_ultimo_evento)

    print('Número clientes que completaron demora en cola A:',num_completo_demora_A)
    print('Número de clientes que completaron demora en cola C1',num_completo_demora_C[0])
    print('Número de clientes que completaron demora en cola C2',num_completo_demora_C[1])

    try:
        print('Demora acumulada en cola A:',demora_acum_A/num_completo_demora_A)
    except ZeroDivisionError:
        print('No hay demora acumulada en cola A, ningún cliente completó demora')
    try:
        print('Demora acumulada en cola C1:', demora_acum_C[0]/num_completo_demora_C[0])
    except ZeroDivisionError:
        print('No hay demora acumulada en cola C1, ningún cliente completó demora')
    try:
        print('Demora acumulada en cola C2:', demora_acum_C[1]/num_completo_demora_C[1])
    except ZeroDivisionError:
        print('No hay demora acumulada en cola C2, ningún cliente completó demora')

    try:
        print('Q(t): número promedio de clientes en cola A:',area_num_clientes_cola_A/tiempo_ultimo_evento)
    except ZeroDivisionError:
        pass
    try:
        print('Q(t): número promedio de clientes en cola C1:',area_num_clientes_cola_C1/tiempo_ultimo_evento)
    except ZeroDivisionError:
        pass
    try:
        print('Q(t): número promedio de clientes en cola C2:',area_num_clientes_cola_C2/tiempo_ultimo_evento)
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
        elif tipo_proximo_evento == 'AD1':
            arribo_D1()
        elif tipo_proximo_evento == 'AD2':
            arribo_D2()
        elif tipo_proximo_evento == 'PD1':
            partida_D1()
        elif tipo_proximo_evento == 'PD2':
            partida_D2()
        else:
            print('Error, no hay ningún evento de ese tipo')

    informes()

    return

programa_principal()
