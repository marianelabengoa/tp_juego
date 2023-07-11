import pygame
import sys
from Enemigo import Enemi
from objeto import Objeto
from personaje import Personaje
from clase_nivel_1 import *
from clase_nivel_2 import *
from clase_nivel_3 import *
from score_alto import get_Highgest_Score


class Game:
    def __init__(self, ALTO, ANCHO):
        pygame.init()
        pygame.mixer.init()
        self.display = pygame.display.set_mode((ALTO, ANCHO))
        self.fondo_inicio = pygame.image.load(
            "src/assets/imagen/fondo/estrellas_inicioo.jpg").convert()
        self.fondo_inicio = pygame.transform.scale(
            self.fondo_inicio, (ALTO, ANCHO))
        self.fondo_pausa = pygame.image.load("src/assets/imagen/fondo/pausa_fondo.png").convert()
        self.fondo_pausa = pygame.transform.scale(self.fondo_pausa, (ANCHO,ALTO))
        self.fondo_juego = pygame.image.load(
            "src/assets/imagen/fondo/fondo_luna.jpg").convert()
        self.fondo_juego = pygame.transform.scale(
            self.fondo_juego, (ALTO, ANCHO))
        self.caption = pygame.display.set_caption("capybara adventure")
        self.reloj = pygame.time.Clock()
        self.fuente_titulo = pygame.font.Font(
            "src/assets/imagen/personaje/Uncracked Free Trial-6d44.woff", 100)
        self.fuente_letra = pygame.font.Font(
            "src/assets/imagen/personaje/Uncracked Free Trial-6d44.woff", 40)
        self.sonido_laser = pygame.mixer.Sound("src/assets/sonido/laser.mp3")
        self.musica_fondo = pygame.mixer.music.load(
            "src/assets/sonido/musica_inicio.mp3")

        self.enemigo_volteado = "src/assets/imagen/personaje/enemigo_volteado.png"
        self.enemigo_no_volteado = "src/assets/imagen/personaje/enemigo_no_volteado.png"
        self.volador = "src/assets/imagen/personaje/volador.png"

        self.capi_volteado = "src/assets/imagen/personaje/capybara_volteado.png"
        self.capi_no_volteado = "src/assets/imagen/personaje/capi_no_volteado.png"
        self.capi = Personaje((200, 200), (400, 530),
                              self.capi_no_volteado, self.capi_volteado)

        self.capi_ganar = Objeto(
            (350, 350), (ANCHO//2+55, 500), "src/assets/imagen/personaje/capi_ganar.png")
        self.capi_perder = Objeto(
            (400, 350), (ANCHO//2+200, 500), "src/assets/imagen/personaje/capi_perder.jpg")

        self.portal = Objeto((60, 100), (ANCHO-35, ALTO - 102),
                             "src/assets/imagen/fondo/tercer_portal.png")

        self.aplausos_ganar = pygame.mixer.Sound(
            "src/assets/sonido/aplausos_ganar.mp3")

        self.score = 0

        self.FPS = 60

        self.tamaño_cap = (70, 70)

        self.AZUL = (0, 0, 255)
        self.VERDE = (67, 135, 113)
        self.NEGRO = (0, 0, 0)
        self.BLANCO = (255, 255, 255)

        self.contador_vidas = 3
        self.time_cont = 60
        self.text_cont = "60"

        self.plataforma_size = (90, 60)

        try:
            self.score_mas_alto = int(get_Highgest_Score())
        except:
            self.score_mas_alto = 0
            
    def definir_musica_fondo(self, musica: str):
        self.musica = pygame.mixer.music.load(musica)

    def manejar_eventos_inicio(self):
        self.musica_comenzar()
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

    def musica_comenzar(self):
        pygame.mixer.music.play(-1)

    def musica_parar(self):
        pygame.mixer.music.stop()

    def manejar_eventos_niveles(self):
        ALTO = 550
        ANCHO = 1000
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.musica_parar()
                    self.salir()

                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_1 or evento.key == pygame.K_KP_1:
                        self.musica_parar()
                        nivel_1((ANCHO, ALTO), ALTO, ANCHO, self.FPS,
                                self.tamaño_cap, self.plataforma_size, self)
                    elif evento.key == pygame.K_2 or evento.key == pygame.K_KP_2:
                        self.musica_parar()
                        nivel_2((ANCHO, ALTO), ALTO, ANCHO, self.FPS,
                                self.tamaño_cap, self.plataforma_size, self)
                    elif evento.key == pygame.K_3 or evento.key == pygame.K_KP_3:
                        self.musica_parar()
                        nivel_3((ANCHO, ALTO), ALTO, ANCHO, self.FPS,
                                self.tamaño_cap, self.plataforma_size, self)
                    elif evento.key == pygame.K_b:
                        self.pantalla_inicio()
                        self.manejar_eventos_inicio()

    def pantalla_menu_niveles(self):
        self.display.blit(self.fondo_inicio, (0, 0))

        rectangulo = pygame.rect.Rect(290, 210, 70, 90)
        rectangulo2 = pygame.rect.Rect(50, 210, 70, 90)
        rectangulo3 = pygame.rect.Rect(170, 210, 70, 90)

        pygame.draw.rect(self.display, self.NEGRO, rectangulo)
        pygame.draw.rect(self.display, self.NEGRO, rectangulo2)
        pygame.draw.rect(self.display, self.NEGRO, rectangulo3)

        self.display.blit(self.fuente_titulo.render(
            "NIVELES", True, self.BLANCO), (150, 70))
        self.display.blit(self.fuente_titulo.render(
            "1", True, self.BLANCO), (75, 220))
        self.display.blit(self.fuente_titulo.render(
            "2", True, self.BLANCO), (195, 220))
        self.display.blit(self.fuente_titulo.render(
            "3", True, self.BLANCO), (315, 220))
        self.display.blit(self.fuente_letra.render(
            "Presione 1 para jugar el primer nivel", True, self.BLANCO), (600, 200))
        self.display.blit(self.fuente_letra.render(
            "Presione 2 para jugar el segundo nivel", True, self.BLANCO), (600, 250))
        self.display.blit(self.fuente_letra.render(
            "Presione 3 para jugar el tercer nivel", True, self.BLANCO), (600, 300))
        pygame.display.flip()

    def pantalla_inicio(self):
        self.display.blit(self.fondo_inicio, (0, 0))
        self.display.blit(self.capi.imagen_izq, self.capi.rect)
        self.display.blit(self.fuente_titulo.render(
            "capybara adventure", True, self.BLANCO), (250, 70))
        self.display.blit(self.fuente_letra.render(
            "Presione N para seleccionar nivel", True, self.BLANCO), (300, 200))
        self.display.blit(self.fuente_letra.render(
            "Presione ESC para salir", True, self.BLANCO), (300, 250))
        pygame.display.flip()

    def game_over(self):
        while True:
            self.display.fill(self.NEGRO)
            self.display.blit(self.fuente_titulo.render(
                "GAME OVER", True, self.AZUL), (50, 50))
            self.display.blit(self.capi_perder.image, self.capi_perder.rect)
            pygame.mixer.music.stop()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.musica_parar()
                    self.salir()

                if evento.type == pygame.KEYDOWN:
                    if not evento.key == pygame.K_RIGHT:
                    # if evento.key == pygame.K_LEFT or evento.key == pygame.K_UP or evento.key == pygame.K_DOWN:
                        self.comenzar_app()
                pygame.display.flip()

    def ganar(self, score, score_mas_alto):
        while True:
            self.display.fill(self.NEGRO)
            self.display.blit(self.fuente_titulo.render(
                "GANASTE", True, self.VERDE), (100, 50))
            self.display.blit(self.capi_ganar.image, self.capi_ganar.rect)
            self.aplausos_ganar.play()
            pygame.mixer.music.stop()

            if self.score > self.score_mas_alto:
                self.display.blit(self.fuente_letra.render(
                    f"registraste el score mas alto, con una puntuacion de {score}", True, self.VERDE), (50, 100))
            else:
                self.display.blit(self.fuente_letra.render(
                    f"score mas alto {score_mas_alto}", True, self.VERDE), (50, 100))
                self.display.blit(self.fuente_letra.render(
                    f"tu score {score}", True, self.VERDE), (50, 150))

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.musica_parar()
                    self.salir()

                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_LEFT or evento.key == pygame.K_UP or evento.key == pygame.K_DOWN:
                        pygame.mixer.music.stop()
                        pygame.mixer.Sound.stop(self.aplausos_ganar)
                        self.comenzar_app()
                pygame.display.flip()


juego = Game(1000, 550)

juego.comenzar_app()
