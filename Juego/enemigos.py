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
    dict_zombie["trayectoria"] = [0, 0]
    dict_zombie["speed"] = random.randrange (5, 10, 1)
    return dict_zombie

def crear_lista_zombies():
    lista_zombies = []
    for i in range(5):
        y = random.randrange (-200, -50)
        x = random.randrange (0, 800)
        lista_zombies.append(crear_zombie(x,y,60,60))
    return lista_zombies

def calcular_trayectoria(zombie, pos_player):
    x, y = pos_player
    rx = (x-zombie["rect"][0]) / 100
    ry = (y-zombie["rect"][1]) / 100
    zombie["trayectoria"] = [rx, ry]
   # zombie["rect"][0] = player["rect"][0] + 50
   # zombie["rect"][1] = player["rect"][1] + 50
    return zombie

def update(lista_zombies, pos_player):
    for zombie in lista_zombies:
        rect_zombie = zombie["rect"]
        rect_zombie.y = rect_zombie.y + zombie["speed"]
        zombie = calcular_trayectoria(zombie, pos_player)
        zombie["rect"][0] = zombie["rect"][0] + zombie["trayectoria"][0]
        zombie["rect"][1] = zombie["rect"][1] + zombie["trayectoria"][1]
        
def actualizar_pantalla(lista_zombies, player, ventana_principal, lista_balas_visibles, imagen_sangre):
    game_over = False
    lista_balas_restantes = lista_balas_visibles.copy()
    for zombie in lista_zombies:
        if zombie["rect"].colliderect(player["rect"]):
            game_over = True
        for i in range(len(lista_balas_visibles)):
            #try:
                if(lista_balas_visibles[i]["rect"].colliderect(zombie["rect"])):
                    lista_balas_restantes.pop(i)
                    ventana_principal.blit(imagen_sangre,  (zombie["rect"][0], zombie["rect"][1]))
                    zombie["rect"][0] = random.randrange (0, 800)
                    zombie["rect"][1] = random.randrange (-200, -50)
            #except:
            #    print("ERROR")
            #    pass

                #personaje["score"] = personaje["score"] + 100
                #restar_zombie(zombie)
        ventana_principal.blit(zombie["surface"], (zombie["rect"][0], zombie["rect"][1]))
        if(zombie["rect"].y > 620):
            game_over = True
    return game_over, lista_balas_restantes