import pygame
import sys
from personaje import Personaje
from Enemigo import Enemi
from objeto import Objeto
from portal import Portal
from cantidad import Corazon
from score_alto import get_Highgest_Score

class Nivel:
    def __init__(self, pantalla, ALTO, ANCHO, FPS, size_capybara, score, plataforma_size):

        ROJO = (255, 0, 0)
        AZUL = (0, 0, 255)
        VERDE = (0, 255, 0)
        NEGRO= (0, 0, 0)
        BLANCO = (255, 255, 255)