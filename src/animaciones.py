import pygame


def get_animations(size):
    animaciones = [pygame.transform.scale(pygame.image.load("src/assets/imagen/fondo/primer_portal.png").convert_alpha(), size), pygame.transform.scale(pygame.image.load("src/assets/imagen/fondo/segundo_portal.png").convert_alpha(
    ), size), pygame.transform.scale(pygame.image.load("src/assets/imagen/fondo/tercer_portal.png").convert_alpha(), size), pygame.transform.scale(pygame.image.load("src/assets/imagen/fondo/segundo_portal.png").convert_alpha(), size)]
    return animaciones
