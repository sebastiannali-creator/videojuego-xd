import pygame

carro_i=pygame.image.load("carro_izquierda.png")
carro_d=pygame.image.load("carro_derecha.png")
class Personaje:
    def __init__(self, x, y, imagen):
        self.ancho = 30
        self.alto = 50
        self.x = x
        self.y = y
        self.imagen = imagen
        self.rect = pygame.Rect(x, y, self.ancho, self.alto)
    
    def actualizar_posicion(self): 
        self.rect.x = self.x
        self.rect.y = self.y
    
    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, (self.x, self.y))

    
    def mover(self, dx, dy):
        self.x += dx
        self.y += dy
        self.actualizar_posicion()
    
    def colisiona_con(self, otro_personaje):
        return self.rect.colliderect(otro_personaje.rect)

class Enemigo:
    def __init__(self, x, y,imagen,direcion):
        self.x = x
        self.y = y
        self.imagen = imagen
        self.velocidad = 1
        self.direcion = direcion
        
        self.direcion = direcion
    def actualizar_posicion(self):
        self.x = self.x + self.velocidad*self.direcion

        if self.direction == 1:    
            if self.x >= 640:
                self.x = 0

        elif self.direction == -1:  
            if self.x + 32 <= 0:
                self.x = 640        

        self.rect = pygame.Rect(self.x, self.y, 32,32)        

    def dibujar(self, pantalla):

        if self.direction == -1:
            pantalla.blit(carro_i, (self.x,self.y))
        elif self.direction == 1:
            pantalla.blit(carro_d, (self.x,self.y))

    
    def mover(self, dx, dy):
        self.x += dx
        self.y += dy
        self.actualizar_posicion()     