import pygame
from constantes import *
import tablero

pygame.init() #Se inicializa pygame
pantalla_juego = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA+100))
pygame.display.set_caption('The Simpsons Memotest')

running = True
#cuadrado = pygame.Rect(30, 30, 60, 60)
#set tick timer 
tick = pygame.USEREVENT
tiempo = pygame.time.set_timer(tick,1000)

tablero_juego = tablero.init(4, 2)
while running:

    # Se verifica si el usuario cerro la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN :
            indice_tarjeta = tablero.colicion(tablero_juego,event.pos)
        if event.type == pygame.USEREVENT:
            if event.type == tick:
                print("Ya paso un segundo")
        
    pantalla_juego.fill((255, 255, 255))
    
    #tablero.update(tablero_juego, tiempo)
    tablero.render(tablero_juego,pantalla_juego)
    pygame.display.flip()
    for i in range(len(tablero_juego["lista_tarjetas"])):
        print(tablero_juego["lista_tarjetas"][i])


# Done! Time to quit.
pygame.quit()