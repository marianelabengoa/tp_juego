import pygame


def imagen_por_cantidad(size):
    animaciones = [pygame.transform.scale(pygame.image.load("src/assets/imagen/coin/tres_corazones.jpg").convert_alpha(), size), pygame.transform.scale(pygame.image.load("src/assets/imagen/coin/dos_corazones.jpg").convert_alpha(
    ), size), pygame.transform.scale(pygame.image.load("src/assets/imagen/coin/un_corazon.jpg").convert_alpha(), size), pygame.transform.scale(pygame.image.load("src/assets/imagen/coin/corazon_vacio.jpg").convert_alpha(), size)]
    return animaciones


class Corazon():
    def __init__(self, size, coordenate, contador):
        super().__init__()
        self.size = size
        self.coordenate = coordenate
        self.indice = 0
        self.cantidad = imagen_por_cantidad(size)
        self.imagen = self.cantidad[self.indice]
        self.rect = self.imagen.get_rect()
        self.rect.midbottom = coordenate
        self.contador = contador

    def agregar(self):
        self.contador += 1

    def sacar(self):
        self.contador -= 1

    def update(self):
        if self.contador == 3:
            self.indice = 0
        elif self.contador == 2:
            self.indice = 1
        elif self.contador == 1:
            self.indice = 2
        elif self.contador == 0:
            self.indice = 3
        self.imagen = self.cantidad[self.indice]
