import pygame
import math
import random
from constantes import *
import tarjeta
import pygame


'''
ANCHO_PANTALLA = 500
ALTO_PANTALLA = 550
ALTO_TEXTO = 50
CANTIDAD_TARJETAS_H = 2
CANTIDAD_TARJETAS_V = 2
'''
def init(cant_tarjetas_v, cant_tarjetas_h):
    '''
    Crea una lista de tarjetas
    Recibe como parametro la cantidad de tarjetas
    Retorna un dict tablero
    '''
    dic_tablero = {}
    lista_tarjetas = []

    i = 1
    for x in range(0,ANCHO_PANTALLA,ANCHO_TARJETA):
        for y in range(0,ALTO_PANTALLA-ALTO_TEXTO,ALTO_TARJETA):
            if(i > CANTIDAD_TARJETAS_UNICAS):
                tarjeta_test = tarjeta.init("0{0}.png".format(i-CANTIDAD_TARJETAS_UNICAS),r"00.png",x,y)
            else:
                tarjeta_test = tarjeta.init("0{0}.png".format(i),r"00.png",x,y)
            #tarjeta_test["visible"] = True
            lista_tarjetas.append(tarjeta_test)
            i = i + 1
   # contador_imagen = 1
   # x=0
   # x_2 = 0
   # y=0
   # ancho_tarjeta = ANCHO_PANTALLA / cant_tarjetas_h
   # alto_tarjeta = ALTO_PANTALLA / cant_tarjetas_v
#
   # for i in range(cant_tarjetas_v + cant_tarjetas_h):
   #     nombre_imagen = r"\0{0}.png".format(contador_imagen)
   #     if i <= (cant_tarjetas_h - 1):
   #         lista_tarjetas.append(tarjeta.init(nombre_imagen, r"\00.png", x,y, ancho_tarjeta, alto_tarjeta))
   #         contador_imagen += 1 
   #         x += ancho_tarjeta
   #     else:
   #         y = alto_tarjeta
   #         lista_tarjetas.append(tarjeta.init(nombre_imagen, r"\00.png", x_2, y, ancho_tarjeta, alto_tarjeta))
   #         x_2 += ancho_tarjeta
   #         contador_imagen += 1 
        
    dic_tablero["lista_tarjetas"] = lista_tarjetas
    print(lista_tarjetas)
    return dic_tablero

def colicion(d_tablero,pos_xy):
    '''
    verifica si existe una colicion alguna tarjetas del tablero y la coordenada recivida como parametro
    Recibe como parametro el tablero y una tupla (X,Y)
    Retorna el indice de la tarjeta que colisiono con la coordenada
    '''
    indice_tarjeta = None
    if pos_xy != None:
        print("colision en colision")
        for i in range(len(d_tablero["lista_tarjetas"])):
            if d_tablero["lista_tarjetas"][i]["rect"].collidepoint(pos_xy):
                indice_tarjeta = i
    return indice_tarjeta    

def update(d_tablero, pos_mouse):
    '''
    verifica si es necesario actualizar el estado de alguna tarjeta, 
    en funcion de su propio estado y el de las otras
    Recibe como parametro el tablero y el tiempo transcurrido desde el ultimo llamado
    '''
    
    tarjeta_a_descubrir = colicion(d_tablero, pos_mouse)
    if tarjeta_a_descubrir != None:
        print("COlision")
        d_tablero["lista_tarjetas"][tarjeta_a_descubrir]["visible"] = True

    lista_tarjetas = d_tablero["lista_tarjetas"]
    #for i in range(len("lisa_tarjetas")):
    #for i in range(2):
        #print(lista_tarjetas)
        #if lista_tarjetas[i]["visible"] == True:
         #   pass
        

def render(d_tablero,pantalla_juego):
    '''
    Dibuja todos los elementos del tablero en la superficie recibida como parametro
    Recibe como parametro el tablero
    '''
    lista_tarjetas = d_tablero["lista_tarjetas"]
    for tarjeta in lista_tarjetas:
        #print(tarjeta)
        if tarjeta["visible"] == True:
            pantalla_juego.blit(tarjeta["surface"],tarjeta["rect"])
        else:
            pantalla_juego.blit(tarjeta["surface_hide"],tarjeta["rect"])
        