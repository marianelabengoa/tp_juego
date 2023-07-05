import pygame
import sys
from Enemigo import Enemi
from objeto import Objeto
from personaje import Personaje
from clase_nivel_1 import *
from clase_nivel_2 import *
from clase_nivel_3 import *


class Game:
    def __init__(self, ALTO, ANCHO):
        pygame.init()
        pygame.mixer.init()
        self.display = pygame.display.set_mode((ALTO, ANCHO))
        self.fondo_inicio = pygame.image.load("./assets/imagen/fondo/estrellas_inicioo.jpg").convert()
        self.fondo_inicio = pygame.transform.scale(self.fondo_inicio, (ALTO, ANCHO))
        self.fondo_juego = pygame.image.load("./assets/imagen/fondo/fondo_luna.jpg").convert()
        self.fondo_juego = pygame.transform.scale(self.fondo_juego, (ALTO, ANCHO))
        self.caption = pygame.display.set_caption("capybara adventure")
        self.reloj = pygame.time.Clock()
        self.fuente_titulo = pygame.font.Font("./assets/imagen/personaje/Uncracked Free Trial-6d44.woff", 100)
        self.fuente_letra = pygame.font.Font("./assets/imagen/personaje/Uncracked Free Trial-6d44.woff", 40)
        self.sonido_laser = pygame.mixer.Sound("./assets/sonido/laser.mp3")
        self.musica_fondo = pygame.mixer.music.load("./assets/sonido/musica_inicio.mp3")

        self.enemigo_volteado = "./assets/imagen/personaje/enemigo_volteado.png"
        self.enemigo_no_volteado = "./assets/imagen/personaje/enemigo_no_volteado.png"
        self.volador = "./assets/imagen/personaje/volador.png"

        self.capi_volteado = "./assets/imagen/personaje/capybara_volteado.png"
        self.capi_no_volteado = "./assets/imagen/personaje/capi_no_volteado.png"
        self.capi = Personaje((200,200), (400, 530), self.capi_no_volteado, self.capi_volteado)

        self.capi_perder =Objeto((200, 200), (ANCHO//2, ALTO//2), "./assets/imagen/personaje/capi_perder.png")
        self.capi_ganar = "./assets/imagen/personaje/capi_ganar.png"

        self.portal = Objeto((60, 100), (ANCHO-35, ALTO - 102), "./assets/imagen/fondo/tercer_portal.png")

        self.score=0

        self.FPS=60

        self.tamaño_cap=(70,70)

        self.NEGRO=(0,0,0)
        self.BLANCO=(250,250,250)
        self.AZUL=(0,0,250)

        self.plataforma_size=(90,60)

    def definir_imagen_fondo(self, imagen: str, size: tuple):
        self.fondo = pygame.image.load(imagen).convert()
        self.fondo = pygame.transform.scale(self.fondo, size)

    def definir_sonido(self, sonido: str):
        self.sonido = pygame.mixer.Sound(sonido)

    def definir_musica_fondo(self, musica: str):
        self.musica = pygame.mixer.music.load(musica)


    def manejar_eventos_inicio(self): 
        self.musica_comenzar(self.musica_fondo)
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.musica_parar()
                    self.salir()

                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_n:  # niveles
                        self.pantalla_menu_niveles()
                        self.manejar_eventos_niveles()
                    if evento.key == pygame.K_ESCAPE:
                        self.salir()
                    

    def salir(self):
        pygame.quit()
        sys.exit()

    def comenzar_app(self):
            self.pantalla_inicio()
            self.manejar_eventos_inicio()


    def musica_comenzar(self, musica):
        musica = pygame.mixer.music.play(-1)

    def musica_parar(self):
        pygame.mixer.music.stop()


    def manejar_eventos_niveles(self):
        ALTO=550
        ANCHO=1000
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.musica_parar()
                    pygame.quit()
                    sys.exit()

                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_1 or evento.key == pygame.K_KP_1:
                        self.musica_parar()
                        nivel_1((ANCHO, ALTO), ALTO, ANCHO, self.FPS, self.tamaño_cap, self.score, self.plataforma_size)
                    elif evento.key == pygame.K_2 or evento.key == pygame.K_KP_2:
                        self.musica_parar()
                        nivel_2((ANCHO, ALTO), ALTO, ANCHO, self.FPS, self.tamaño_cap, self.score, self.plataforma_size)
                    elif evento.key == pygame.K_3 or evento.key == pygame.K_KP_3:
                        self.musica_parar()
                        nivel_3((ANCHO, ALTO), ALTO, ANCHO, self.FPS, self.tamaño_cap, self.score, self.plataforma_size)
                    elif evento.key == pygame.K_b:
                        self.pantalla_inicio()
                        self.manejar_eventos_inicio()


    def pantalla_menu_niveles(self):
        self.display.blit(self.fondo_inicio, (0,0))

        rectangulo=pygame.rect.Rect(290, 210, 70, 90)
        rectangulo2=pygame.rect.Rect(50, 210, 70, 90)
        rectangulo3=pygame.rect.Rect(170, 210, 70, 90)

        pygame.draw.rect(self.display, self.NEGRO, rectangulo)
        pygame.draw.rect(self.display, self.NEGRO, rectangulo2)
        pygame.draw.rect(self.display, self.NEGRO, rectangulo3)

        self.display.blit(self.fuente_titulo.render("NIVELES", True, self.BLANCO), (150, 70))
        self.display.blit(self.fuente_titulo.render("1", True, self.BLANCO), (75, 220))
        self.display.blit(self.fuente_titulo.render("2", True, self.BLANCO), (195, 220))
        self.display.blit(self.fuente_titulo.render("3", True, self.BLANCO), (315, 220))
        self.display.blit(self.fuente_letra.render("Presione 1 para jugar el primer nivel", True, self.BLANCO), (600, 200))
        self.display.blit(self.fuente_letra.render("Presione 2 para jugar el segundo nivel", True, self.BLANCO), (600, 250))
        self.display.blit(self.fuente_letra.render("Presione 3 para jugar el tercer nivel", True, self.BLANCO), (600, 300))
        pygame.display.flip()
    
    def pantalla_inicio(self):
        self.display.blit(self.fondo_inicio, (0,0))
        self.display.blit(self.capi.imagen_izq, self.capi.rect)
        self.display.blit(self.fuente_titulo.render("capybara adventure", True, self.BLANCO), (250, 70))
        self.display.blit(self.fuente_letra.render("Presione N para seleccionar nivel", True, self.BLANCO), (300, 200))
        self.display.blit(self.fuente_letra.render("Presione ESC para salir", True, self.BLANCO), (300, 250))
        pygame.display.flip()

    def game_over(self):
        while True:
            self.display.fill(self.NEGRO)
            self.display.blit(self.fuente_titulo.render("GAME OVER", True, self.AZUL), (50, 50))
            self.display.blit(self.capi_perder.imagen, self.capi_perder.rect)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.musica_parar()
                    pygame.quit()
                    sys.exit()
            pygame.display.flip()

    

        
juego=Game(1000, 550)

juego.comenzar_app()