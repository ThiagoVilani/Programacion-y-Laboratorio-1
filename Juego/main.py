import pygame
import personaje
import time
import movimiento_player

pygame.init()
ventana_principal = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Testeando la ventana") #COLOCANDO EL TITULO DE LA VENTANA
is_running = True
pos_player = [350, 450]
#player = pygame.image.load("Programacion-y-Laboratorio-1\Juego\player.png")
#player = pygame.transform.scale(player, (125, 106))
player = movimiento_player.crear_player(pos_player)

while is_running:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            is_running = False
    ventana_principal.fill((200, 0, 0)) #CAMBIO EL COLOR DEL FONDO DE LA VENTANA  
    
    copia, player, pos_player = movimiento_player.movimiento(pos_player, player)
    ventana_principal.blit(copia, (pos_player))
    #time.sleep(4)
    pygame.display.flip()

pygame.quit()