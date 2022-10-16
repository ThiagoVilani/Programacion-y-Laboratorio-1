import pygame

pygame.init()
ventana_principal = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Testeando la ventana") #COLOCANDO EL TITULO DE LA VENTANA
is_running = True
pos_circulo = [20,30]

while is_running:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            is_running = False
    ventana_principal.fill((200, 0, 0)) #CAMBIO EL COLOR DEL FONDO DE LA VENTANA        
    pygame.draw.circle(ventana_principal, (255, 0, 0), pos_circulo, 50)

    lista_teclas = pygame.key.get_pressed()
    if lista_teclas[pygame.K_DOWN]:
        pos_circulo[1] = pos_circulo[1] + 0.3
    if lista_teclas[pygame.K_UP]:
        pos_circulo[1] = pos_circulo[1] - 0.3
    if lista_teclas[pygame.K_LEFT]:
        pos_circulo[0] = pos_circulo[0] - 0.3
    if lista_teclas[pygame.K_RIGHT]:
        pos_circulo[0] = pos_circulo[0] + 0.3

    

    pygame.display.flip()

pygame.quit()