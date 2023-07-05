import pygame
from laser import Laser


class Enemi(pygame.sprite.Sprite):
    def __init__(self, size, coordenate, path_imagen_izq, path_imagen_der):
        super().__init__()

        self.size = size
        self.coordenate = coordenate
        self.imagen_izq = pygame.transform.scale(
            pygame.image.load(path_imagen_izq).convert_alpha(), size)
        self.imagen_der = pygame.transform.scale(
            pygame.image.load(path_imagen_der).convert_alpha(), size)
        self.rect = self.imagen_izq.get_rect()
        self.rect.bottomleft = coordenate

        self.velocidad_x = 3
        self.direccion = 1
        self.disparo = False
        self.tiempo_ultimo_disparo = 0
        self.image = self.imagen_der

    def update(self, plataforma):
        self.rect.x += self.velocidad_x * self.direccion

        if self.rect.left < 0 or self.rect.right > 1000 or self.rect.colliderect(plataforma):
            self.direccion *= -1

            if self.direccion == 1:
                self.image = self.imagen_der
            else:
                self.image = self.imagen_izq

    def disparar(self, speed, sprites, lasers, path_imagen, segundos):
        segundos = pygame.time.get_ticks()

        if not self.disparo and segundos - self.tiempo_ultimo_disparo >= 3000:
            laser = Laser(self.rect.center, path_imagen, (5, 5), speed, "y")
            sprites.add(laser)
            lasers.add(laser)
            self.disparo = True
            self.tiempo_ultimo_disparo = segundos

        if self.disparo and segundos - self.tiempo_ultimo_disparo >= 3000:
            self.disparo = False
