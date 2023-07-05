import pygame
import sys
from personaje import Personaje
from Enemigo import Enemi
from objeto import Objeto
from portal import Portal
from cantidad import Corazon
from score_alto import get_Highgest_Score

class nivel_1:
    def __init__(self, pantalla, ALTO, ANCHO, FPS, size_capybara, score, plataforma_size):

        AZUL = (0, 0, 255)
        VERDE = (67, 135, 113)
        NEGRO= (0, 0, 0)
        BLANCO = (255, 255, 255)

        pygame.init()
        pygame.mixer.init()

        contador_vidas=3

        display = pygame.display.set_mode(pantalla)
        pygame.display.set_caption("capybara adventure")

        fondo = pygame.image.load("./assets/imagen/fondo/fondo_luna.jpg").convert()
        fondo = pygame.transform.scale(fondo, pantalla)

        sprites = pygame.sprite.Group()
        lasers = pygame.sprite.Group()
        lasers_enemigos = pygame.sprite.Group()
        enemigos = pygame.sprite.Group()
        corazones = pygame.sprite.Group()
        plataformas = pygame.sprite.Group()
        coins = pygame.sprite.Group()


        plat = Objeto(plataforma_size, (200, ALTO - 102), "./assets/imagen/fondo/ladrillo.png")
        coin = Objeto((20,20), (200, ALTO - 172), "./assets/imagen/coin/coin.png")
        vida_extra = Objeto((20,20), (500, ALTO - 112), "./assets/imagen/coin/cora.png")
        portal = Portal((60,120), (ANCHO-35, ALTO - 92))

        pomelo = pygame.surface.Surface((ANCHO, 100))
        pomelo.fill(AZUL)
        rect_pomelo = pomelo.get_rect()
        rect_pomelo.bottom = ALTO

        corazon = Corazon((70, 20), (ANCHO-70, 60), contador_vidas)

        capi_volteado = "./assets/imagen/personaje/capybara_volteado.png"
        capi_no_volteado = "./assets/imagen/personaje/capi_no_volteado.png"
        capi = Personaje(size_capybara, (0, ALTO - 110), capi_no_volteado, capi_volteado)

        enemigo_volteado = "./assets/imagen/personaje/enemigo_volteado.png"
        enemigo_no_volteado = "./assets/imagen/personaje/enemigo_no_volteado.png"
        enemy = Enemi(size_capybara, (800, ALTO - 102), enemigo_no_volteado, enemigo_volteado)
 
        volador = "./assets/imagen/personaje/volador.png"
        enemy_v = Enemi((50, 70), (800, ALTO - 300), volador, volador)


        sprites.add(capi)
        corazones.add(vida_extra)
        coins.add(coin)
        enemigos.add(enemy)
        enemigos.add(enemy_v)
        plataformas.add(plat)


        pygame.mixer.music.load("./assets/sonido/music-for-arcade-style-game-146875.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(1.0)
        
        sonido = pygame.mixer.Sound("./assets/sonido/laser.mp3")


        imagen_piso = pygame.image.load("./assets/imagen/fondo/99.png").convert()
        tamanio_cuadrado = 100
        imagen_piso = pygame.transform.scale(imagen_piso, (tamanio_cuadrado, tamanio_cuadrado))
        superficie_piso = pygame.Surface((ANCHO, tamanio_cuadrado))

        fuente = pygame.font.Font("./assets/imagen/personaje/Uncracked Free Trial-6d44.woff", 60)

        clock = pygame.time.Clock()

        contador = 0

        try:
            score_mas_alto=int(get_Highgest_Score())
        except:
            score_mas_alto=0

        while True:
            clock.tick(FPS)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.mixer.music.stop()
                    pygame.quit()
                    sys.exit()

                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_LEFT:
                        capi.mover_izquierda()
                    elif evento.key == pygame.K_RIGHT:
                        capi.mover_derecha()
                    elif evento.key == pygame.K_UP:
                        capi.saltar2()
                    elif evento.key == pygame.K_SPACE:
                        capi.disparar(7, sprites, lasers, sonido, "./assets/imagen/personaje/660.png")
                    elif evento.key == pygame.K_F1 and (pygame.mixer.music.get_volume()>0):
                        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume()-0.1)
                    elif evento.key == pygame.K_F2 and (pygame.mixer.music.get_volume()==0 or pygame.mixer.music.get_volume()<1):
                        pygame.mixer.music.set_volume(pygame.mixer.music.get_volume()+0.1)
                    elif evento.key == pygame.K_F3 and (pygame.mixer.music.get_volume()>0):
                        pygame.mixer.music.set_volume(0.0)
                    elif evento.key == pygame.K_F3 and (pygame.mixer.music.get_volume()==0 or pygame.mixer.music.get_volume()<1):
                        pygame.mixer.music.set_volume(1.0)

                if evento.type == pygame.KEYUP:
                    if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                        capi.detener()

            capi.caer(rect_pomelo)
            capi.caer(plat.rect)
            capi.chocar(plat.rect)
            capi.update()


            segundos = pygame.time.get_ticks() // 1000

            enemy_v.disparar(7, sprites, lasers_enemigos, "./assets/imagen/personaje/660.png", segundos)
            
            if pygame.sprite.spritecollide(capi, lasers_enemigos, True) or pygame.sprite.spritecollideany(capi, enemigos):
                contador_vidas-=1
                corazon.sacar()
                if score > 0:
                    score-=100
                else:
                    score=0

            if pygame.sprite.spritecollide(capi, coins, True):
                score+=500

            if pygame.sprite.spritecollide(capi, corazones, True):
                corazon.agregar()
            
            pygame.sprite.groupcollide(enemigos, lasers, True, True)
                

            pygame.sprite.groupcollide(lasers_enemigos, plataformas, True, False)
            pygame.sprite.spritecollide(plat, lasers, True)


            for laser in lasers_enemigos:
                    if laser.rect.bottom >= ALTO:
                        laser.kill()


            sprites.update()

            enemy.update(plat.rect)
            enemy_v.update(plat.rect)
            lasers.update()
            lasers_enemigos.update()
            corazon.update()

            if score>score_mas_alto:
                score_mas_alto=score
            with open("score_mas_alto.txt", "w") as file:
                file.write(str(score_mas_alto))


            minutos = contador
            if segundos % 60 == 0:
                contador += 1
                segundos=0
            

            display.blit(fondo, (0, 0))
            lasers_enemigos.draw(display)
            lasers.draw(display)
            enemigos.draw(display)
            display.blit(pomelo, rect_pomelo)
            plataformas.draw(display)
            corazones.draw(display)
            coins.draw(display)

            for x in range(0, ANCHO, tamanio_cuadrado):
                superficie_piso.blit(imagen_piso, (x, 0))

            display.blit(superficie_piso, (0, ALTO - tamanio_cuadrado))

            display.blit(portal.imagen, portal.rect)
            portal.mueve()

            display.blit(corazon.imagen, corazon.rect)

            display.blit(fuente.render("Score " + str(score), True, BLANCO), (50, 50))
            display.blit(fuente.render("Time " + str(minutos) + " " + str(segundos), True, BLANCO), (200, 50))
            display.blit(fuente.render("mas alto " + str(score_mas_alto), True, BLANCO), (400, 50))
            
            display.blit(capi.obtener_imagen(), capi.rect)

            if contador_vidas==0:
                display.fill(NEGRO)
                display.blit(fuente.render("GAME OVER", True, AZUL), (50, 50))
                # display.blit(capi_perder.imagen, capi_perder.rect)
            
            if capi.rect.colliderect(portal.rect):
                display.fill(NEGRO)
                display.blit(fuente.render("GANASTE", True, VERDE), (100, 50))

                if score>score_mas_alto:
                    display.blit(fuente.render(f"registraste el score mas alto, con una puntuacion de {score}", True, VERDE), (50, 100))
                else:
                    display.blit(fuente.render(f"score mas alto {score_mas_alto}", True, VERDE), (50, 100))
                    display.blit(fuente.render(f"tu score {score}", True, VERDE), (50, 150))

            pygame.display.flip()

