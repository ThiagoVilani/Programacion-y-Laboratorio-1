import pygame
import random

def crear_zombie(x,y,ancho,alto):
    # Leer una imagen
    imagen_zombie = pygame.image.load("Programacion-y-Laboratorio-1\Juego\zombie_2.png")
    imagen_zombie = pygame.transform.scale(imagen_zombie,(ancho,alto))
    rect_zombie = imagen_zombie.get_rect()
    rect_zombie.x = x
    rect_zombie.y = y
    dict_zombie = {}
    dict_zombie["surface"] = imagen_zombie
    dict_zombie["rect"] = rect_zombie
    dict_zombie["visible"] = True
    dict_zombie["speed"] = random.randrange (10,20,1)
    return dict_zombie

def crear_lista_zombies():
    lista_zombies = []
    for i in range(5):
        y = random.randrange (-1000,0,60)
        x = random.randrange (0,740,60)
        lista_zombies.append(crear_zombie(x,y,60,60))
    return lista_zombies

def update(lista_zombies):
    for zombie in lista_zombies:
        rect_zombie = zombie["rect"]
        rect_zombie.y = rect_zombie.y + zombie["speed"]