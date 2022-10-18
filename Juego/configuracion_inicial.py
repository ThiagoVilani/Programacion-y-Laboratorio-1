import pygame
import movimiento_player
import enemigos

def configurar():
    pygame.mixer.music.set_volume(0.7)
    musica_fondo = pygame.mixer.Sound("Programacion-y-Laboratorio-1\Juego\Supremacy.mp3")
    musica_fondo.play(-1)
    sonido_disparo = pygame.mixer.Sound("Programacion-y-Laboratorio-1\Juego\sonido_disparo.mp3")
    pygame.init()
    ventana_principal = pygame.display.set_mode((900, 600))
    pygame.display.set_caption("Testeando la ventana") #COLOCANDO EL TITULO DE LA VENTANA
    is_running = True
    game_over = False
    imagen_game_over = pygame.image.load("Programacion-y-Laboratorio-1\Juego\game_over_2.png")
    imagen_game_over = pygame.transform.scale(imagen_game_over, (500, 500))
    fondo = pygame.image.load(r"Programacion-y-Laboratorio-1\Juego\floor_3.jpg")
    fondo = pygame.transform.scale(fondo, (1259, 1167))
    pos_player = [350, 450]
    player = movimiento_player.crear_player(pos_player)
    lista_enemigos = enemigos.crear_lista_zombies()
    timer = pygame.USEREVENT + 0
    pygame.time.set_timer(timer,100)
    #lista_balas = proyectil.crear_lista_balas(pos_player)
    lista_balas_visibles = []