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
pygame.time.set_timer(tick,1000)
clock_fps = pygame.time.Clock()

tablero_juego = tablero.init()
while running:
    tiempo_origen = pygame.time.get_ticks()
    print(tiempo_origen)
    clock_fps.tick(60)
    # Se verifica si el usuario cerro la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN :
            tablero.update(tablero_juego, event.pos)
        if event.type == pygame.USEREVENT:
            if event.type == tick:
                #tablero.update(tablero_juego, event.pos)
                print("Ya paso un segundo")       
    pantalla_juego.fill((255, 255, 255))
    tablero.render(tablero_juego,pantalla_juego)
    pygame.display.flip()
    
# Done! Time to quit.
pygame.quit()