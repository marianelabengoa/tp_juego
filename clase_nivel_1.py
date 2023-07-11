import pygame
import sys
from personaje import Personaje
from Enemigo import Enemi
from objeto import Objeto
from portal import Portal
from cantidad import Corazon
from score_alto import get_Highgest_Score


class nivel_1():
    def __init__(self, pantalla, ALTO, ANCHO, FPS, size_capybara, score, plataforma_size, juego):

        pygame.init()
        pygame.mixer.init()

        self.juego = juego

        self.AZUL = (0, 0, 255)
        self.VERDE = (67, 135, 113)
        self.NEGRO = (0, 0, 0)
        self.BLANCO = (255, 255, 255)

        self.contador_vidas = 3
        self.time_cont = 60
        self.text_cont = "60"

        self.display = pygame.display.set_mode(pantalla)
        pygame.display.set_caption("capybara adventure")

        self.fondo = pygame.image.load(
            "./assets/imagen/fondo/fondo_luna.jpg").convert()
        self.fondo = pygame.transform.scale(self.fondo, pantalla)

        self.fondo_pausa = pygame.image.load(
            "./assets/imagen/fondo/pausa_fondo.png").convert()
        self.fondo_pausa = pygame.transform.scale(self.fondo_pausa, pantalla)

        self.sprites = pygame.sprite.Group()
        self.lasers = pygame.sprite.Group()
        self.lasers_enemigos = pygame.sprite.Group()
        self.enemigos = pygame.sprite.Group()
        self.corazones = pygame.sprite.Group()
        self.plataformas = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.keys = pygame.sprite.Group()

        self.capi_ganar = Objeto(
            (350, 350), (ANCHO//2, 500), "./assets/imagen/personaje/capi_ganar.png")
        self.capi_perder = Objeto(
            (350, 350), (ANCHO//2, 500), "./assets/imagen/personaje/capi_perder.jpg")
        self.plat = Objeto(plataforma_size, (200, ALTO - 102),
                           "./assets/imagen/fondo/ladrillo.png")
        self.coin = Objeto((20, 20), (200, ALTO - 172),
                           "./assets/imagen/coin/coin.png")
        self.vida_extra = Objeto(
            (20, 20), (500, ALTO - 112), "./assets/imagen/coin/cora.png")
        self.portal = Portal((60, 120), (ANCHO-35, ALTO - 92))

        self.Pkey = Objeto((40, 40), (70, 160), "./assets/imagen/coin/P.png")
        self.F1 = Objeto((40, 40), (70, 240), "./assets/imagen/coin/F1.png")
        self.F2 = Objeto((40, 40), (70, 320), "./assets/imagen/coin/F2.jpg")
        self.F3 = Objeto((40, 40), (70, 400), "./assets/imagen/coin/F3.png")
        self.F4 = Objeto((40, 40), (70, 480), "./assets/imagen/coin/F3.png")
        self.space = Objeto((160, 40), (700, 200),
                            "./assets/imagen/coin/space.png")
        self.flechas = Objeto((90, 70), (690, 400),
                              "./assets/imagen/coin/flechas.png")

        self.pomelo = pygame.surface.Surface((ANCHO, 100))
        self.pomelo.fill(self.AZUL)
        self.rect_pomelo = self.pomelo.get_rect()
        self.rect_pomelo.bottom = ALTO

        self.corazon = Corazon((70, 20), (ANCHO-70, 60), self.contador_vidas)

        self.capi_volteado = "./assets/imagen/personaje/capybara_volteado.png"
        self.capi_no_volteado = "./assets/imagen/personaje/capi_no_volteado.png"
        self.capi = Personaje(size_capybara, (0, ALTO - 110),
                              self.capi_no_volteado, self.capi_volteado)

        self.enemigo_volteado = "./assets/imagen/personaje/enemigo_volteado.png"
        self.enemigo_no_volteado = "./assets/imagen/personaje/enemigo_no_volteado.png"
        self.enemy = Enemi(size_capybara, (800, ALTO - 102),
                           self.enemigo_no_volteado, self.enemigo_volteado)

        self.volador = "./assets/imagen/personaje/volador.png"
        self.enemy_v = Enemi((50, 70), (800, ALTO - 300),
                             self.volador, self.volador)

        self.sprites.add(self.capi)
        self.corazones.add(self.vida_extra)
        self.coins.add(self.coin)
        self.enemigos.add(self.enemy)
        self.enemigos.add(self.enemy_v)
        self.plataformas.add(self.plat)
        self.keys.add(self.Pkey)
        self.keys.add(self.F1)
        self.keys.add(self.F2)
        self.keys.add(self.F3)
        self.keys.add(self.F4)
        self.keys.add(self.space)
        self.keys.add(self.flechas)

        pygame.mixer.music.load(
            "./assets/sonido/music-for-arcade-style-game-146875.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(1.0)

        self.sonido = pygame.mixer.Sound("./assets/sonido/laser.mp3")
        self.aplausos_ganar = pygame.mixer.Sound(
            "./assets/sonido/aplausos_ganar.mp3")
        self.coin_sonido = pygame.mixer.Sound(
            "./assets/sonido/coin_sonido.mp3")

        pygame.mixer.Sound.set_volume(self.aplausos_ganar, 0.3)
        pygame.mixer.Sound.set_volume(self.coin_sonido, 0.5)
        pygame.mixer.Sound.set_volume(self.sonido, 0.4)

        self.imagen_piso = pygame.image.load(
            "./assets/imagen/fondo/99.png").convert()
        self.tamanio_cuadrado = 100
        self.imagen_piso = pygame.transform.scale(
            self.imagen_piso, (self.tamanio_cuadrado, self.tamanio_cuadrado))
        self.superficie_piso = pygame.Surface((ANCHO, self.tamanio_cuadrado))

        self.fuente = pygame.font.Font(
            "./assets/imagen/personaje/Uncracked Free Trial-6d44.woff", 60)
        self.fuente_letra = pygame.font.Font(
            "./assets/imagen/personaje/Uncracked Free Trial-6d44.woff", 30)

        self.clock = pygame.time.Clock()
        pygame.time.set_timer(pygame.USEREVENT, 1000)

        try:
            self.score_mas_alto = int(get_Highgest_Score())
        except:
            self.score_mas_alto = 0

        def pause():
            paused = True
            self.display.blit(self.fondo_pausa, (0, 0))
            self.display.blit(self.fuente.render(
                "COMANDOS", True, self.BLANCO), (400, 50))
            self.display.blit(self.fuente_letra.render(
                "reanudar juego", True, self.BLANCO), (100, 130))
            self.display.blit(self.fuente_letra.render(
                "bajar volumen", True, self.BLANCO), (100, 210))
            self.display.blit(self.fuente_letra.render(
                "subir volumen", True, self.BLANCO), (100, 290))
            self.display.blit(self.fuente_letra.render(
                "silenciar musica", True, self.BLANCO), (100, 370))
            self.display.blit(self.fuente_letra.render(
                "silenciar sonidos", True, self.BLANCO), (100, 450))
            self.display.blit(self.fuente_letra.render(
                "disparar", True, self.BLANCO), (650, 140))
            self.display.blit(self.fuente_letra.render(
                "moverse y saltar", True, self.BLANCO), (630, 410))
            self.keys.draw(self.display)
            while paused:
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        self.juego.salir()

                    if evento.type == pygame.KEYDOWN:
                        if evento.key == pygame.K_p:
                            paused = False
                        elif evento.key == pygame.K_F1 and (pygame.mixer.music.get_volume() > 0):
                            pygame.mixer.music.set_volume(
                                pygame.mixer.music.get_volume()-0.1)
                        elif evento.key == pygame.K_F2 and (pygame.mixer.music.get_volume() == 0 or pygame.mixer.music.get_volume() < 1):
                            pygame.mixer.music.set_volume(
                                pygame.mixer.music.get_volume()+0.1)
                        elif evento.key == pygame.K_F3 and (pygame.mixer.music.get_volume() > 0 or pygame.mixer.music.get_volume() == 1):
                            pygame.mixer.music.set_volume(0.0)
                        elif evento.key == pygame.K_F3 and (pygame.mixer.music.get_volume() == 0 or pygame.mixer.music.get_volume() < 1):
                            pygame.mixer.music.set_volume(1.0)
                        elif evento.key == pygame.K_F4 and (pygame.mixer.Sound.get_volume(self.sonido) > 0) and (pygame.mixer.Sound.get_volume(self.aplausos_ganar) > 0) and (pygame.mixer.Sound.get_volume(self.coin_sonido) > 0):
                            pygame.mixer.Sound.set_volume(self.sonido, 0.0)
                            pygame.mixer.Sound.set_volume(
                                self.coin_sonido, 0.0)
                            pygame.mixer.Sound.set_volume(
                                self.aplausos_ganar, 0.0)
                        elif evento.key == pygame.K_F4 and (pygame.mixer.Sound.get_volume(self.sonido) == 0) and (pygame.mixer.Sound.get_volume(self.aplausos_ganar) == 0) and (pygame.mixer.Sound.get_volume(self.coin_sonido) == 0):
                            pygame.mixer.Sound.set_volume(self.sonido, 1.0)
                            pygame.mixer.Sound.set_volume(
                                self.coin_sonido, 1.0)
                            pygame.mixer.Sound.set_volume(
                                self.aplausos_ganar, 1.0)
                pygame.display.flip()

        while True:
            self.clock.tick(FPS)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    self.juego.musica_parar()
                    self.juego.salir()

                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_LEFT:
                        self.capi.mover_izquierda()
                    elif evento.key == pygame.K_RIGHT:
                        self.capi.mover_derecha()
                    elif evento.key == pygame.K_UP:
                        self.capi.saltar2()
                    elif evento.key == pygame.K_SPACE:
                        self.capi.disparar(
                            7, self.sprites, self.lasers, self.sonido, "./assets/imagen/personaje/660.png")
                    elif evento.key == pygame.K_F1 and (pygame.mixer.music.get_volume() > 0):
                        pygame.mixer.music.set_volume(
                            pygame.mixer.music.get_volume()-0.1)
                    elif evento.key == pygame.K_F2 and (pygame.mixer.music.get_volume() == 0 or pygame.mixer.music.get_volume() < 1):
                        pygame.mixer.music.set_volume(
                            pygame.mixer.music.get_volume()+0.1)
                    elif evento.key == pygame.K_F3 and (pygame.mixer.music.get_volume() > 0 or pygame.mixer.music.get_volume() == 1):
                        pygame.mixer.music.set_volume(0.0)
                    elif evento.key == pygame.K_F3 and (pygame.mixer.music.get_volume() == 0 or pygame.mixer.music.get_volume() < 1):
                        pygame.mixer.music.set_volume(1.0)
                    elif evento.key == pygame.K_F4 and (pygame.mixer.Sound.get_volume(self.sonido) > 0) and (pygame.mixer.Sound.get_volume(self.aplausos_ganar) > 0) and (pygame.mixer.Sound.get_volume(self.coin_sonido) > 0):
                        pygame.mixer.Sound.set_volume(self.sonido, 0.0)
                        pygame.mixer.Sound.set_volume(self.coin_sonido, 0.0)
                        pygame.mixer.Sound.set_volume(self.aplausos_ganar, 0.0)
                    elif evento.key == pygame.K_F4 and (pygame.mixer.Sound.get_volume(self.sonido) == 0) and (pygame.mixer.Sound.get_volume(self.aplausos_ganar) == 0) and (pygame.mixer.Sound.get_volume(self.coin_sonido) == 0):
                        pygame.mixer.Sound.set_volume(self.sonido, 1.0)
                        pygame.mixer.Sound.set_volume(self.coin_sonido, 1.0)
                        pygame.mixer.Sound.set_volume(self.aplausos_ganar, 1.0)
                    elif evento.key == pygame.K_p:
                        pause()

                if evento.type == pygame.KEYUP:
                    if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                        self.capi.detener()

                if evento.type == pygame.USEREVENT:
                    self.time_cont -= 1
                    if self.time_cont > 0:
                        self.text_cont = str(self.time_cont)

            self.capi.caer(self.rect_pomelo)
            self.capi.caer(self.plat.rect)
            self.capi.chocar(self.plat.rect)
            self.capi.update()

            self.segundos = pygame.time.get_ticks() // 1000

            self.enemy_v.disparar(7, self.sprites, self.lasers_enemigos,
                                  "./assets/imagen/personaje/660.png", self.segundos)

            if pygame.sprite.spritecollide(self.capi, self.lasers_enemigos, True) or pygame.sprite.spritecollideany(self.capi, self.enemigos):
                self.contador_vidas -= 1
                self.corazon.sacar()
                if score > 0:
                    score -= 100
                else:
                    score = 0

            if pygame.sprite.spritecollide(self.capi, self.coins, True):
                score += 500
                self.coin_sonido.play()

            if pygame.sprite.spritecollide(self.capi, self.corazones, True):
                if self.contador_vidas < 3:
                    self.corazon.agregar()
                    self.contador_vidas += 1
                else:
                    self.contador_vidas = 3
                    score += 1000

            pygame.sprite.groupcollide(self.enemigos, self.lasers, True, True)
            pygame.sprite.groupcollide(
                self.lasers_enemigos, self.plataformas, True, False)
            pygame.sprite.spritecollide(self.plat, self.lasers, True)

            for laser in self.lasers_enemigos:
                if laser.rect.bottom >= ALTO:
                    laser.kill()

            self.sprites.update()
            self.enemy.update(self.plat.rect)
            self.enemy_v.update(self.plat.rect)
            self.lasers.update()
            self.lasers_enemigos.update()
            self.corazon.update()

            if score > self.score_mas_alto:
                self.score_mas_alto = score
            with open("score_mas_alto.txt", "w") as file:
                file.write(str(self.score_mas_alto))

            self.display.blit(self.fondo, (0, 0))
            self.lasers_enemigos.draw(self.display)
            self.lasers.draw(self.display)
            self.enemigos.draw(self.display)
            self.display.blit(self.pomelo, self.rect_pomelo)
            self.plataformas.draw(self.display)
            self.corazones.draw(self.display)
            self.coins.draw(self.display)

            for x in range(0, ANCHO, self.tamanio_cuadrado):
                self.superficie_piso.blit(self.imagen_piso, (x, 0))

            self.display.blit(self.superficie_piso,
                              (0, ALTO - self.tamanio_cuadrado))

            self.display.blit(self.portal.imagen, self.portal.rect)
            self.portal.mueve()

            self.display.blit(self.corazon.imagen, self.corazon.rect)

            self.display.blit(self.fuente.render(
                "Score " + str(score), True, self.BLANCO), (50, 50))
            self.display.blit(self.fuente.render(
                "Time left " + self.text_cont, True, self.BLANCO), (200, 48))

            self.display.blit(self.capi.obtener_imagen(), self.capi.rect)

            if self.contador_vidas == 0:
                self.juego.game_over()

            if self.capi.rect.colliderect(self.portal.rect):
                self.juego.ganar()

            pygame.display.flip()


