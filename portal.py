
import pygame
from animaciones import *

class Portal (pygame.sprite.Sprite):
    def __init__(self, size, coordenate):
        super().__init__()
        self.size = size
        self.coordenate = coordenate
        self.indice=0
        self.animations=get_animations(self.size)
        self.imagen = self.animations[self.indice]
        self.rect = self.imagen.get_rect()
        self.rect.midbottom = coordenate
        self.velocidad = 10
        self.contador = 0

    def mueve(self):        
        self.indice+=1
        if self.indice==4:
            self.indice=0
        self.imagen = self.animations[self.indice]
        
    def mueve(self):
        self.contador += 1
        if self.contador >= self.velocidad:
            self.indice += 1
            if self.indice == 4:
                self.indice = 0
            self.imagen = self.animations[self.indice]
            self.contador = 0
