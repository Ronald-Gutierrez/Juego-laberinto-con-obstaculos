import pygame,sys
from pygame.locals import *

pygame.init()
ventana = pygame.display.set_mode((400,300))
pygame.display.set_caption("Laberinto")

Fuente= pygame.font.SysFont("Arial",30)
aux=1
while True:
    ventana.fill(0)
    Tiempo = pygame.time.get_ticks()/1000
    if aux == Tiempo:
        aux+=1
        

    for event in pygame.event.get():
        if event.type ==QUIT:
            pygame.quit()
            sys.exit()
    
    contador = Fuente.render("tiempo : "+str(Tiempo),0,(120,70,0))
    ventana.blit(contador,(100,100))
    pygame.display.update()