import pygame
import enemigos
import movimiento_player
import proyectil

pygame.init()
ventana_principal = pygame.display.set_mode((900, 600))
pygame.display.set_caption("Testeando la ventana") #COLOCANDO EL TITULO DE LA VENTANA
is_running = True
fondo = pygame.image.load(r"Programacion-y-Laboratorio-1\Juego\floor_3.jpg")
fondo = pygame.transform.scale(fondo, (1259, 1167))
pos_player = [350, 450]
player = movimiento_player.crear_player(pos_player)
lista_enemigos = enemigos.crear_lista_zombies()
timer = pygame.USEREVENT + 0
pygame.time.set_timer(timer,100)
#lista_balas = proyectil.crear_lista_balas(pos_player)
lista_balas_visibles = []

"""
Cada vez que presione el mouse se crea un bala desde la pos del jugador
se hace la cuenta para ver cuanto tendria que moverse por X e Y 
"""

while is_running:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            is_running = False
        if evento.type == timer:
            enemigos.update(lista_enemigos) 
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if len(lista_balas_visibles) < 19:
                bala = proyectil.crear_bala(10, 10)
                lista_balas_visibles.append(proyectil.calcular_trayectoria(bala, player))

    ventana_principal.blit(fondo, [0, 0]) #CAMBIO EL COLOR DEL FONDO DE LA VENTANA  
    
    copia, player, pos_player = movimiento_player.movimiento(pos_player, player)
    
    ventana_principal.blit(copia, (pos_player))
    enemigos.actualizar_pantalla(lista_enemigos, player, ventana_principal, lista_balas_visibles)
    proyectil.update(lista_balas_visibles, ventana_principal)
    #time.sleep(4)
    pygame.display.flip()

pygame.quit()