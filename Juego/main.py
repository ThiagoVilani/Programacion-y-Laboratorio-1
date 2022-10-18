import pygame
import enemigos
import movimiento_player
import proyectil
import time


pygame.mixer.init()
pygame.mixer.music.set_volume(0.7)
pygame.init()
pygame.display.set_caption("Testeando la ventana") #COLOCANDO EL TITULO DE LA VENTANA

#::::::::::SONIDOS::::::::::
musica_fondo = pygame.mixer.Sound("Programacion-y-Laboratorio-1\Juego\Supremacy.mp3")
#musica_fondo.play(-1)
sonido_disparo = pygame.mixer.Sound("Programacion-y-Laboratorio-1\Juego\sonido_disparo.mp3")
sonido_zombie = pygame.mixer.Sound("Programacion-y-Laboratorio-1\Juego\sonido_zombie.mp3")

#::::::::::IMAGENES::::::::::
imagen_game_over = pygame.image.load("Programacion-y-Laboratorio-1\Juego\game_over_2.png")
imagen_game_over = pygame.transform.scale(imagen_game_over, (500, 500))
fondo = pygame.image.load(r"Programacion-y-Laboratorio-1\Juego\floor_4.png")
fondo = pygame.transform.scale(fondo, (900, 900))
imagen_sangre = pygame.image.load(r"Programacion-y-Laboratorio-1\Juego\blood.png")
imagen_sangre = pygame.transform.scale(imagen_sangre, (60, 60))

ventana_principal = pygame.display.set_mode((900, 600))
is_running = True
game_over = False
pos_player = [350, 450]
lista_balas_visibles = []
player = movimiento_player.crear_player(pos_player)
lista_enemigos = enemigos.crear_lista_zombies()
timer = pygame.USEREVENT + 0
pygame.time.set_timer(timer,100)



while is_running:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            is_running = False
        if evento.type == timer:
            #sonido_zombie.play()
            enemigos.update(lista_enemigos, pos_player) 
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if len(lista_balas_visibles) < 19:
                sonido_disparo.play()
                bala = proyectil.crear_bala(10, 10)
                lista_balas_visibles.append(proyectil.calcular_trayectoria(bala, player))

    ventana_principal.blit(fondo, [0, 0]) #CAMBIO EL COLOR DEL FONDO DE LA VENTANA  
    
    copia, player, pos_player = movimiento_player.movimiento(pos_player, player)
    
    ventana_principal.blit(copia, (pos_player))
    is_running = enemigos.actualizar_pantalla(lista_enemigos, player, ventana_principal, lista_balas_visibles, imagen_sangre)
    
       
    proyectil.update(lista_balas_visibles, ventana_principal)
    #time.sleep(4)
    pygame.display.flip()

pygame.quit()