import pygame
import personaje
import time

pygame.init()
ventana_principal = pygame.display.set_mode((1200, 900))
pygame.display.set_caption("Testeando la ventana") #COLOCANDO EL TITULO DE LA VENTANA
is_running = True
player = personaje.crear(400, 250, 125, 106)

while is_running:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            is_running = False
    ventana_principal.fill((200, 0, 0)) #CAMBIO EL COLOR DEL FONDO DE LA VENTANA  
    

    lista_teclas = pygame.key.get_pressed()
    if lista_teclas[pygame.K_DOWN]:
        personaje.update(player, 0, 1)
    if lista_teclas[pygame.K_UP]:
        personaje.update(player, 0, -0.3)
    if lista_teclas[pygame.K_LEFT]:
        personaje.update(player, -0.3, 0)
    if lista_teclas[pygame.K_RIGHT]:
        personaje.update(player, 1, 0)
        player["surface"] = pygame.transform.rotate(player["surface"], -0.20)
        #player["rect_pos"] = pygame.transform.rotate(player["rect_pos"], 0.20)
        #player["rect"] = pygame.transform.rotate(player["rect"], 0.20)

    

    personaje.actualizar_pantalla(player, ventana_principal)
    #time.sleep(0.4)

    pygame.display.flip()

pygame.quit()