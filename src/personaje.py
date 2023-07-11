import pygame
from laser import Laser


class Personaje(pygame.sprite.Sprite):
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

        self.velocidad_x = 0
        self.velocidad_y = 0
        self.GRAVEDAD = 1
        self.SALTAR_VELOCIDAD = -10
        self.en_suelo = False
        self.choca = False
        self.speed = 5

        self.salto = 0
        self.saltando = False

    def saltar2(self):
        if self.salto == 0:
            self.velocidad_y = self.SALTAR_VELOCIDAD
            self.salto = 1
        else:
            self.salto = 0

    def mover_izquierda(self):
        if self.rect.left > 0:
            self.velocidad_x = -self.speed

    def mover_derecha(self):
        if self.rect.right < 1000:
            self.velocidad_x = self.speed

    def detener(self):
        self.velocidad_x = 0
        self.velocidad_y = 0

    def update(self):
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        if not self.en_suelo:
            self.velocidad_y += self.GRAVEDAD

        if self.salto != 0:
            self.rect.y += self.velocidad_y
            self.velocidad_y += 1

            if self.rect.bottom >= 550-102:
                self.rect.bottom = 550-102
                self.saltando = False
                self.salto = 0

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 1000:
            self.rect.right = 1000

    def obtener_imagen(self):
        if self.velocidad_x < 0:
            return self.imagen_izq
        elif self.velocidad_x > 0:
            return self.imagen_der
        else:
            return self.imagen_der

    def caer(self, rect):
        if self.rect.colliderect(rect):
            if self.velocidad_y > 0:
                self.rect.bottom = rect.top
                self.saltando = False
            self.velocidad_y = 0
            self.en_suelo = True

    def chocar(self, rect):
        if self.rect.colliderect(rect):
            if self.velocidad_x > 0:
                self.rect.right = rect.left
            elif self.velocidad_x < 0:
                self.rect.left = rect.right
            self.velocidad_x = 0
            self.choca = True

    def disparar(self, speed, sprites, lasers, sonido, imagen_laser):
        laser = Laser(self.rect.center, imagen_laser, (10, 10), speed, "x")
        sonido.play()
        sprites.add(laser)
        lasers.add(laser)
