import pygame


class Laser(pygame.sprite.Sprite):
    def __init__(self, center: tuple, path_imagen, size, speed, eje):
        super().__init__()

        self.imagen = pygame.transform.scale(
            pygame.image.load(path_imagen).convert_alpha(), size)
        self.image = self.imagen

        self.rect = self.imagen.get_rect()
        self.rect.center = center

        self.velocidad_x = speed
        self.velocidad_y = speed
        self.eje = eje

    def update(self):
        if self.eje == "x":
            self.rect.x += self.velocidad_x
        elif self.eje == "y":
            self.rect.y += self.velocidad_y
