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
pos_mouse = None
lista_tarjetas_visibles = []
indices_tarjetas_visibles = []

while running:
    
    tiempo_origen = pygame.time.get_ticks()
    #tiempito = tiempo_origen - tablero_juego["tiempo_click"]
    clock_fps.tick(60)
    # Se verifica si el usuario cerro la ventana
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN :
            #tablero.update(tablero_juego, event.pos, tiempo_origen)
            pos_mouse = event.pos
        if event.type == pygame.USEREVENT:
            if event.type == tick:
                #tablero.update(tablero_juego, event.pos)
                print("Ya paso un segundo") 
    pos_mouse, lista_tarjetas_visibles, indices_tarjetas_visibles = tablero.update(tablero_juego, pos_mouse, tiempo_origen, lista_tarjetas_visibles, indices_tarjetas_visibles)
    #if 0 < tablero_juego["tiempo_click"]:  
    #    tiempito = tiempo_origen - tablero_juego["tiempo_click"]    
    #    if 3000 < tiempito:
    #        print(tiempito)
    #        print("paso el 3000")
    #        tablero_juego["tiempo_click"] = 0
    #        for tarjeta in tablero_juego["lista_tarjetas"]:
    #            tarjeta["visible"] = False
    pantalla_juego.fill((255, 255, 255))
    tablero.render(tablero_juego,pantalla_juego)
    pygame.display.flip()


    
    #print(tiempito)
    #print(tablero_juego["tiempo_click"], "desde el click")
    #print(tiempo_origen, "origen")
# Done! Time to quit.
pygame.quit()