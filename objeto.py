import pygame

class Objeto (pygame.sprite.Sprite):
    def __init__(self, size, coordenate, path_imagen):
        super().__init__()
        self.size = size
        self.coordenate = coordenate
        self.image = pygame.transform.scale(pygame.image.load(path_imagen).convert_alpha(), size)
        self.rect = self.image.get_rect()
        self.rect.midbottom = coordenate
 
