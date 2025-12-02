import pygame
from personajes import Personaje

pygame.init()

#medidas pantalla
ancho_pantalla = 600
alto_pantalla = 600

#medidas del juego
pantalla = pygame.display.set_mode((ancho_pantalla,alto_pantalla))
pygame.display.set_caption("Videojuego Andino")


#imagenes cargadas
personaje = pygame.image.load("personaje_1.png")
pantalla1 =("pantalla_1.jpeg")


#palabras
grande = pygame.font.SysFont('Arial', 70)
mediana = pygame.font.SysFont('Arial', 36)


estado_juego=["Menu","Parte 1","Parte 2","Parte 3 ","Parte 4","Game Over"]
estado=0
chekpoint=0
choca_estrella=False


run = True
while run == True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pantalla.fill((0,0,0))        
    

    
    pygame.display.flip()

pygame.quit()            