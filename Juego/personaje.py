import pygame
import random


def crear(x, y, ancho, alto):
    imagen_player =  pygame.image.load("Programacion-y-Laboratorio-1\Juego\player.png")
    dict_personaje = {}
    dict_personaje["surface"] = imagen_player
    dict_personaje["surface"] = pygame.transform.scale( dict_personaje["surface"],(ancho,alto))
    dict_personaje["rect_pos"] = pygame.Rect(x,y,200,200)
    dict_personaje["rect"] = imagen_player.get_rect()
    dict_personaje["score"] = 0
    return dict_personaje

def update(personaje, incremento_x, incremento_y):
    nueva_x = personaje["rect_pos"].x + incremento_x
    nueva_y = personaje["rect_pos"].y + incremento_y
    if(nueva_x > 0 and nueva_x < 900):
        print("se actualizo la x {}".format(nueva_x))
        personaje["rect_pos"].x = personaje["rect_pos"].x + incremento_x
        personaje["rect"].x = personaje["rect"].x + incremento_x
    if(nueva_y > 0 and nueva_y < 600):
        print("se actualizo la y {}".format(nueva_y))
        personaje["rect_pos"].y = personaje["rect_pos"].y + incremento_y
        personaje["rect"].y = personaje["rect"].y + incremento_y

    #x, y = pygame.mouse.get_pos()
    #y = y/5
    #angulo = 180 - y
    #copia = pygame.transform.rotate(personaje["surface"], angulo)
    
    #personaje["surface"] = pygame.transform.rotate(personaje["surface"], angulo)

def actualizar_pantalla(personaje,ventana_principal):
    ventana_principal.blit(personaje["surface"], personaje["rect_pos"])
