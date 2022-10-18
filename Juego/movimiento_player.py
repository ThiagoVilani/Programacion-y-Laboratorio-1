import pygame

def crear_player(pos_player):
    imagen_player = pygame.image.load("Programacion-y-Laboratorio-1\Juego\player.png")
    imagen_player = pygame.transform.scale(imagen_player, (125, 106))
    rect_player = imagen_player.get_rect()
    rect_player.x = pos_player[0]
    rect_player.y = pos_player[1]
    dic_player = {}
    dic_player["surface"] = imagen_player
    dic_player["rect"] = rect_player
    return dic_player

def movimiento(pos_player, player):
    lista_teclas = pygame.key.get_pressed()
    if lista_teclas[pygame.K_a]:
        if pos_player[0] < 0:
            pos_player[0] = pos_player[0]
        else:    
            pos_player[0] = pos_player[0] - 1
            player["rect"][0] = player["rect"][0] -1
        
    if lista_teclas[pygame.K_d]:
        if pos_player[0] > 770:
            pos_player[0] = pos_player[0]
        else:    
            pos_player[0] = pos_player[0] + 1
            player["rect"][0] = player["rect"][0] +1

    x, y = pygame.mouse.get_pos()
    x = x/5
    angulo = 180 - x
    copia = pygame.transform.rotate(player["surface"], angulo)
    return copia, player, pos_player