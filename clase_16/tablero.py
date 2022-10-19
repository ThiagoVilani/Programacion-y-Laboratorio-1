import pygame
import math
import random
from constantes import CANTIDAD_TARJETAS_H, CANTIDAD_TARJETAS_V
import tarjeta
import pygame

'''
ANCHO_PANTALLA = 500
ALTO_PANTALLA = 550
ALTO_TEXTO = 50
CANTIDAD_TARJETAS_H = 2
CANTIDAD_TARJETAS_V = 2
'''
def init():
    '''
    Crea una lista de tarjetas
    Recibe como parametro la cantidad de tarjetas
    Retorna un dict tablero
    '''
    dic_tablero = {}
    lista_tarjetas = []
    contador_imagen = 0
    for i in range(CANTIDAD_TARJETAS_H * CANTIDAD_TARJETAS_V):
        nombre_imagen = "0{}.png".format(contador_imagen)
        lista_tarjetas.append(tarjeta.init(nombre_imagen, ))
        contador_imagen += 1 
    dic_tablero["lista_tarjetas"] = lista_tarjetas
    return dic_tablero

def colicion(d_tablero,pos_xy):
    '''
    verifica si existe una colicion alguna tarjetas del tablero y la coordenada recivida como parametro
    Recibe como parametro el tablero y una tupla (X,Y)
    Retorna el indice de la tarjeta que colisiono con la coordenada
    '''
    indice_tarjeta = None
    for i in range(len(d_tablero["l_tarjetas"])):
        if d_tablero["l_tarjetas"][i]["rect"].collidepoint(pos_xy):
            indice_tarjeta = i
    return indice_tarjeta    

def update(d_tablero, tiempo):
    '''
    verifica si es necesario actualizar el estado de alguna tarjeta, 
    en funcion de su propio estado y el de las otras
    Recibe como parametro el tablero y el tiempo transcurrido desde el ultimo llamado
    '''
    lista_tarjetas = d_tablero["lista_tarjetas"]
    #for i in range(len("lisa_tarjetas")):
    for i in range(2):
        print(lista_tarjetas)
        #if lista_tarjetas[i]["visible"] == True:
         #   pass
        

def render(d_tablero,pantalla_juego):
    '''
    Dibuja todos los elementos del tablero en la superficie recibida como parametro
    Recibe como parametro el tablero
    '''
    lista_tarjetas = d_tablero["lista_tarjetas"]
    for tarjeta in lista_tarjetas:
        print(tarjeta)
        if tarjeta["visible"] == True:
            pantalla_juego.blit(tarjeta["surface"],tarjeta["rect"])
        else:
            pantalla_juego.blit(tarjeta["surface_hide"],tarjeta["rect"])
     