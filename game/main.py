from library import *
from model import *
from model2 import *
import configparser
import random
import sys
import json

def start(screen):
    end = False
    while not end:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        end = True

        font = pg.font.Font(None, 34)
        text = "LOS ALIADOS SE HAN VUELTO LOCOS, AL PARECER HAN SIDO INFECTADOS CON ALGÚN VIRUS," 
        text2 = "HAN TOMADO EL CONTROL DE LA NAVE Y AHORA QUIEREN CHOCARLA CONTRA LA TIERRA."
        text3 = "¡TENEMOS QUE DETENERLOS!"
        text4 = "PULSA ENTER PARA CONTINUAR..."
        img_text = font.render(text, True, RED)
        img_text2 = font.render(text2, True, RED)
        img_text3 = font.render(text3, True, RED)
        img_text4 = font.render(text4, True, GREEN)
        
        
        rectanguloTextoPresent = img_text.get_rect()
        rectanguloTextoPresent.centerx = screen.get_rect().centerx
        rectanguloTextoPresent.centery = 250
        screen.blit(img_text, rectanguloTextoPresent)

        rectanguloTextoPresent2 = img_text2.get_rect()
        rectanguloTextoPresent2.centerx = screen.get_rect().centerx
        rectanguloTextoPresent2.centery = 280
        screen.blit(img_text2, rectanguloTextoPresent2)

        rectanguloTextoPresent3 = img_text3.get_rect()
        rectanguloTextoPresent3.centerx = screen.get_rect().centerx
        rectanguloTextoPresent3.centery = 330
        screen.blit(img_text3, rectanguloTextoPresent3)

        rectanguloTextoPresent4 = img_text4.get_rect()
        rectanguloTextoPresent4.centerx = screen.get_rect().centerx
        rectanguloTextoPresent4.centery = 440
        screen.blit(img_text4, rectanguloTextoPresent4)

        pg.display.flip()

def intro(screen):
        font = pg.font.Font(None, 34)
        text = "BIENVENIDO A" 
        text2 = "CyberSpaceDungeon"
        text3 = ""
        text4 = ""
        img_text = font.render(text, True, RED)
        img_text2 = font.render(text2, True, RED)
        img_text3 = font.render(text3, True, RED)
        img_text4 = font.render(text4, True, GREEN)
        
        
        rectanguloTextoPresent = img_text.get_rect()
        rectanguloTextoPresent.centerx = screen.get_rect().centerx
        rectanguloTextoPresent.centery = 250
        screen.blit(img_text, rectanguloTextoPresent)

        rectanguloTextoPresent2 = img_text2.get_rect()
        rectanguloTextoPresent2.centerx = screen.get_rect().centerx
        rectanguloTextoPresent2.centery = 280
        screen.blit(img_text2, rectanguloTextoPresent2)

        rectanguloTextoPresent3 = img_text3.get_rect()
        rectanguloTextoPresent3.centerx = screen.get_rect().centerx
        rectanguloTextoPresent3.centery = 330
        screen.blit(img_text3, rectanguloTextoPresent3)

        rectanguloTextoPresent4 = img_text4.get_rect()
        rectanguloTextoPresent4.centerx = screen.get_rect().centerx
        rectanguloTextoPresent4.centery = 440
        screen.blit(img_text4, rectanguloTextoPresent4)

        pg.display.flip()

def level_1(screen):
    # Loop de música de fondo
    pg.mixer.music.load("sounds/music.ogg")
    pg.mixer.music.play(-1)

    # Efectos de sonido
    cry = pg.mixer.Sound("sounds/cry.ogg")
    shot = pg.mixer.Sound("sounds/blaster.ogg")
    empty = pg.mixer.Sound("sounds/empty.ogg")
    glass = pg.mixer.Sound("sounds/glass.ogg")
    mario = pg.mixer.Sound("sounds/mario.ogg")
    metal = pg.mixer.Sound("sounds/metal.ogg")
    power = pg.mixer.Sound("sounds/power.ogg")
    reload = pg.mixer.Sound("sounds/reload.ogg")
    damage = pg.mixer.Sound("sounds/uh.ogg")
    lose = pg.mixer.Sound("sounds/lose.ogg")
    win = pg.mixer.Sound("sounds/win.ogg")
    fire = pg.mixer.Sound("sounds/fire.ogg")
    explosion = pg.mixer.Sound("sounds/explosion.ogg")

    # Recortar texturas
    sprite = pg.image.load("textures/player.png")
    matriz_player = []
    for row in range(26):
        for column in range(8):
                matriz_player.append([])
                frame = sprite.subsurface(96*column, 96*row, 96, 96)
                frame2 = frame.subsurface(12, 12, 72, 72)
                matriz_player[row].append(frame2)

    sprite = pg.image.load("textures/enemys.png")
    matriz_enemys = []
    for row in range(26):
        for column in range(8):
                matriz_enemys.append([])
                frame = sprite.subsurface(96*column, 96*row, 96, 96)
                frame2 = frame.subsurface(12, 12, 68, 72)
                matriz_enemys[row].append(frame2)

    matriz_ui = Cut("textures/ui.png", [11,5])
    matriz_bullets = Cut("textures/bullets.png", [2,1])
    matriz_modifiers = Cut("textures/modifiers.png", [4,1])
    matriz_generators = Cut("textures/generators.png", [5,1])
    matriz_ui_boss = Cut("textures/ui_boss.png", [1,16])
    matriz_boss = Cut("textures/boss.png", [6,6])

    # Contruir grupos
    blocks = pg.sprite.Group()
    players = pg.sprite.Group()
    modifiers = pg.sprite.Group()
    enemys = pg.sprite.Group()
    bullets = pg.sprite.Group()
    enemy_bullets = pg.sprite.Group()
    generators = pg.sprite.Group()
    bosses = pg.sprite.Group()

    # Crear jugador
    player = Player(matriz_player)
    players.add(player)



    # Crear Generadores
    g1 = Generator([1850,1000], matriz_generators)
    generators.add(g1)
    g2 = Generator([920,1600], matriz_generators)
    generators.add(g2)
    g3 = Generator([385,1600], matriz_generators)
    generators.add(g3)
    g4 = Generator([2045,1600], matriz_generators)
    generators.add(g4)

    # Crear enemigos / Enemy(pos, liminf, limsup, limizq, limder)
    enemy1 = Enemy([1210,265], 295, 450, 0, 0, matriz_enemys, 'left')
    enemys.add(enemy1)
    enemy2 = Enemy([2120,360], 360, 630, 0, 0, matriz_enemys, 'left')
    enemys.add(enemy2)
    enemy3 = Enemy([2700,380], 0, 0, 2700, 3180, matriz_enemys, 'left')
    enemys.add(enemy3)
    enemy4 = Enemy([575,1050], 1050, 1320, 0, 0, matriz_enemys, 'right')
    enemys.add(enemy4)
    enemy5 = Enemy([1750,1350], 1350, 1590, 0, 0, matriz_enemys, 'left')
    enemys.add(enemy5)

    eg1 = Enemy([-500,-500], 265, 1020, 0, 0, matriz_enemys, 'left')
    enemys.add(eg1)
    eg2 = Enemy([-500,-500], 840, 1580, 0, 0, matriz_enemys, 'left')
    enemys.add(eg2)
    eg3 = Enemy([-500,-500], 870, 1590, 0, 0, matriz_enemys, 'left')
    enemys.add(eg3)
    eg4 = Enemy([-500,-500], 1350, 1590, 0, 0, matriz_enemys, 'left')
    enemys.add(eg4)

    boss = Boss([3360, 1345], [3350, 1345], matriz_boss, 'left')
    bosses.add(boss)

    # Cargar fondo y determinar sus limites
    background = pg.image.load("map/map.png")
    info = background.get_rect()
    background_witdh = info[2]
    background_lenght = info[3]
    bk_limit_x = WITDH - background_witdh
    bk_limit_y = LENGHT - background_lenght
    bk_pos_x = 0
    bk_pos_y = 0
    bk_vel_x = -15
    bk_vel_y = -15
    limit_right = 900
    limit_left = 300
    limit_bottom = 400
    limit_top = 200

    # Contruir bloques y modificadores en el terreno
    fnt_map = configparser.ConfigParser()
    fnt_map.read("map/map.map")
    map = fnt_map.get("general", "map")
    rows = map.split("\n")
    j = 0
    for row in rows:
        i = 0
        for object in row:
            if object == "e": # Bloque
                block = Block(pg.Surface([96,96]), [96*i, 96*j])
                blocks.add(block)

            elif object == "f": # Acido
                acid = Block(pg.Surface([30,36]), [96*i+36, 96*j+12], True)
                blocks.add(acid)

            elif object == "t": # Mesa
                table = Block(pg.Surface([96,72]), [96*i, 96*j])
                blocks.add(table)

            elif object == "h": # Cofre
                chest = Block(pg.Surface([144,60]), [96*i, 96*j])
                blocks.add(chest)

            elif object == "j": # Tablero
                board = Block(pg.Surface([144,60]), [96*i, 96*j])
                blocks.add(board)

            elif object == ".": # Vacio
                dado = random.randrange(0, 100)
                if 0 < dado < 3:
                    m = Modifier(matriz_modifiers[0][2], [96*i+36, 96*j+36], "heal")
                    modifiers.add(m)
                elif 3 < dado < 9:
                    m = Modifier(matriz_modifiers[0][1], [96*i+36, 96*j+36], "ammo")
                    modifiers.add(m)
                elif 9 < dado < 12:
                    m = Modifier(matriz_modifiers[0][0], [96*i+36, 96*j+36], "upgrade")
                    modifiers.add(m)
            i += 1
        j += 1

    player.blocks = blocks

    m = Modifier(matriz_modifiers[0][0], [96*30+36, 96*2+36], "upgrade")
    modifiers.add(m)
    m = Modifier(matriz_modifiers[0][0], [96*35, 96*2+36], "upgrade")
    modifiers.add(m)
    m = Modifier(matriz_modifiers[0][0], [96*23+36, 96*14+36], "upgrade")
    modifiers.add(m)
    m = Modifier(matriz_modifiers[0][0], [96*22+36, 96*11+36], "upgrade")
    modifiers.add(m)
    m = Modifier(matriz_modifiers[0][0], [96*5+36, 96*12+36], "upgrade")
    modifiers.add(m)
    m = Modifier(matriz_modifiers[0][0], [96*34+36, 96*11+36], "upgrade")
    modifiers.add(m)
    m = Modifier(matriz_modifiers[0][0], [96*34+36, 96*17+36], "upgrade")
    modifiers.add(m)

    m = Modifier(matriz_modifiers[0][1], [96*32+36, 96*11+36], "ammo")
    modifiers.add(m)
    m = Modifier(matriz_modifiers[0][1], [96*32+36, 96*11+36], "ammo")
    modifiers.add(m)
    m = Modifier(matriz_modifiers[0][1], [96*36+36, 96*17+36], "ammo")
    modifiers.add(m)
    m = Modifier(matriz_modifiers[0][1], [96*36+36, 96*17+36], "ammo")
    modifiers.add(m)

    # Ciclo principal
    clock = pg.time.Clock()
    pause = False
    end = False
    end_game = False
    while (not end) and (not end_game):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pause = not pause

                if (not pause) and (not player.death):
                    player.velx = 0
                    player.vely = 0

                    if event.key == pg.K_d:
                        player.look = "right"
                        player.row = 3
                        player.velx = 15

                    if event.key == pg.K_a:
                        player.look = "left"
                        player.row = 16
                        player.velx = -15

                    if event.key == pg.K_w:
                        if player.look == "right":
                            player.row = 3
                        elif player.look == "left":
                            player.row = 16
                        player.vely = -15

                    if event.key == pg.K_s:
                        if player.look == "right":
                            player.row = 3
                        elif player.look == "left":
                            player.row = 16
                        player.vely = 15

                    if event.key == pg.K_LEFT:
                        if player.ammo > 0:
                            player.ammo -= 1
                            player.look = "left"
                            player.row = 17
                            bullet = Bullet(matriz_bullets[0][0], player.rect.midleft, [0,0], True)
                            bullet.velx = -20
                            bullet.vely = 0
                            bullets.add(bullet)
                            shot.play()
                        else:
                            empty.play()

                    if event.key == pg.K_RIGHT:
                        if player.ammo > 0:
                            player.ammo -= 1
                            player.look = "right"
                            player.row = 4
                            bullet = Bullet(matriz_bullets[0][0], player.rect.midright, [0,0], True)
                            bullet.velx = 20
                            bullet.vely = 0
                            bullets.add(bullet)
                            shot.play()
                        else:
                            empty.play()

                    if event.key == pg.K_UP:
                        if player.ammo > 0:
                            player.ammo -= 1
                            if player.look == "right":
                                player.row = 4
                            elif player.look == "left":
                                player.row = 17
                            bullet = Bullet(matriz_bullets[0][0], player.rect.midtop, [0,0], True)
                            shot.play()
                            bullet.velx = 0
                            bullet.vely = -20
                            bullets.add(bullet)
                            shot.play()
                        else:
                            empty.play()

                    if event.key == pg.K_DOWN:
                        if player.ammo > 0:
                            player.ammo -= 1
                            if player.look == "right":
                                player.row = 4
                            elif player.look == "left":
                                player.row = 17
                            bullet = Bullet(matriz_bullets[0][0], player.rect.midbottom, [0,0], True)
                            bullet.velx = 0
                            bullet.vely = 20
                            bullets.add(bullet)
                            shot.play()
                        else:
                            empty.play()

            if (not pause) and (not player.death):
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if player.ammo > 0:
                            player.ammo -= 1
                            pi = player.rect.center
                            pf = event.pos
                            bullet = Bullet(matriz_bullets[0][0], pi, pf, False)
                            bullets.add(bullet)
                            if bullet.diff_x > 0:
                                player.look = "right"
                                player.row = 4
                            elif bullet.diff_x <= 0:
                                player.look = "left"
                                player.row = 17
                            shot.play()
                        else:
                            empty.play()

                if event.type == pg.KEYUP:
                    player.velx = 0
                    player.vely = 0
                    if player.look == "right":
                        player.row = 0
                        player.column = 0
                    elif player.look == "left":
                        player.row = 13
                        player.column = 0

        if not pause:
            # Colisión con modificadores
            ls_col_m = pg.sprite.spritecollide(player, modifiers, False)
            for m in ls_col_m:
                # De vida
                if m.type == "heal":
                    if player.heal < 9:
                        power.play()
                        player.heal = 9
                        modifiers.remove(m)
                # De munición
                elif m.type == "ammo":
                    if player.ammo < 9:
                        reload.play()
                        player.ammo = 9
                        modifiers.remove(m)
                # De mejora temporal
                elif m.type == "upgrade":
                    mario.play()
                    player.upgrade = 100
                    modifiers.remove(m)

            # Colisión de balas del jugador
            for b in bullets:
                # Con bloques
                ls_col_b = pg.sprite.spritecollide(b, blocks, False)
                if len(ls_col_b) > 0:
                    if ls_col_b[0].attack == False:
                        metal.play()
                        bullets.remove(b)
                # Con generadores
                ls_col_g = pg.sprite.spritecollide(b, generators, False)
                if len(ls_col_g) > 0:
                    bullets.remove(b)
                    for g in ls_col_g:
                        g.heal -= 1
                # Con enemigos
                ls_col_e = pg.sprite.spritecollide(b, enemys, False)
                if len(ls_col_e) > 0:
                    bullets.remove(b)
                    for e in ls_col_e:
                        e.heal -= 1
                # Con Boss
                ls_col_e = pg.sprite.spritecollide(b, bosses, False)
                if len(ls_col_e) > 0:
                    bullets.remove(b)
                    for e in ls_col_e:
                        metal.play()
                        e.heal -= 1

            # Colisión de balas del enemigo
            for b in enemy_bullets:
                # Con bloques
                ls_col_b = pg.sprite.spritecollide(b, blocks, False)
                if len(ls_col_b) > 0:
                    if ls_col_b[0].attack == False:
                        enemy_bullets.remove(b)
                # Con player
                ls_col_p = pg.sprite.spritecollide(b, players, False)
                if len(ls_col_p) > 0:
                    damage.play()
                    player.heal -=1
                    enemy_bullets.remove(b)

            # Distancia entre el jugador y el enemigo
            for e in enemys: 
                diff_x_e = player.rect.x - e.rect.x
                diff_y_e = player.rect.y - e.rect.y
                if (-350 < diff_x_e < 350) and (-350 < diff_y_e < 350) and (e.death == False) and (e.temp2 < 0):
                    if diff_x_e > 0:
                        e.look = "right"
                        e.row = 4
                    elif diff_x_e <= 0:
                        e.look = "left"
                        e.row = 17
                    e.temp2 = 25 # Cadencia de Disparo
                    pi = e.rect.center
                    pf = player.rect.center
                    b = Bullet(matriz_bullets[0][1], pi, pf, False)
                    enemy_bullets.add(b)

            # Distancia entre el jugador y el boss
            diff_x_b = player.rect.x - boss.rect.x
            diff_y_b = player.rect.y - boss.rect.y
            if (-400 < diff_x_b < 400) and (-400 < diff_y_b < 400):
                if diff_x_b <= 0:
                    boss.look = "left"
                elif diff_x_b > 0:
                    boss.look = "right"
                boss.follow = True
                boss.pf = [player.rect.x-50, player.rect.y-60]
                ls_col_bs = pg.sprite.spritecollide(player, bosses, False)
                if (len(ls_col_bs) > 0) and (boss.temp <= 0):
                    if boss.look == "right":
                        boss.row = 1
                    elif boss.look == "left":
                        boss.row = 4
                    fire.play()
                    damage.play()
                    player.heal -= 1
                    boss.temp = 20
            else:
                boss.follow = False

            # Generadores de enemigos
            if g1.cant == 0 and g1.death == False:
                e1 = Enemy(g1.rect.center, eg1.liminf, eg1.limsup, 0, 0, matriz_enemys, 'left')
                if g1.temp < 0:
                    enemys.add(e1)
                    g1.temp = 100
                    g1.cant = 1
            if e1.death == True:
                g1.cant = 0

            if g2.cant == 0 and g2.death == False:
                e2 = Enemy(g2.rect.center, eg2.liminf, eg2.limsup, 0, 0, matriz_enemys, 'right')
                if g2.temp < 0:
                    enemys.add(e2)
                    g2.temp = 100
                    g2.cant = 1
            if e2.death == True:
                g2.cant = 0

            if g3.cant == 0 and g3.death == False:
                e3 = Enemy(g3.rect.center, eg3.liminf, eg3.limsup, 0, 0, matriz_enemys, 'right')
                if g3.temp < 0:
                    enemys.add(e3)
                    g3.temp = 100
                    g3.cant = 1
            if e3.death == True:
                g3.cant = 0

            if g4.cant == 0 and g4.death == False:
                e4 = Enemy(g4.rect.center, eg4.liminf, eg4.limsup, 0, 0, matriz_enemys, 'left')
                if g4.temp < 0:
                    enemys.add(e4)
                    g4.temp = 100
                    g4.cant = 1
            if e4.death == True:
                g4.cant = 0

            # Destruccion de los generadores
            for g in generators:
                if (g.death == True):
                    glass.play()
                    m = Modifier(matriz_modifiers[0][2], g.rect.center, "heal")
                    modifiers.add(m)
                    generators.remove(g)

            # Muerte de los enemigos
            for e in enemys:
                if (e.death == True) and (e.temp < 0):
                    cry.play()
                    m = Modifier(matriz_modifiers[0][1], e.rect.center, "ammo")
                    modifiers.add(m)
                    enemys.remove(e)
            
            #Muerte del boss
            if (boss.death == True) and (boss.temp2 < 0):
                explosion.play()
                bosses.remove(boss)

            # Muerte del jugador
            if (player.death == True) and (player.temp < 0):
                players.remove(player)

            # Condicion de victoria
            if len(bosses) == 0:
                win.play()
                end_game = True
                text = "VICTORIA!"
                color_text = GREEN

            # Condicion de derrota
            if len(players) == 0:
                lose.play()
                end_game = True
                text = " DERROTA "
                color_text = RED

            # Desplazar escenario
            if player.velx > 0:
                if player.rect.right > limit_right:
                    if bk_pos_x > bk_limit_x:
                        player.rect.right = limit_right
                        bk_pos_x += bk_vel_x
                        #Enemigos seteados en el mapa
                        enemy1.modify('right')
                        enemy2.modify('right')
                        enemy3.modify('right')
                        enemy4.modify('right')
                        enemy5.modify('right')
                        #Enemigos generados
                        eg1.modify('right')
                        eg2.modify('right')
                        eg3.modify('right')
                        eg4.modify('right')
                        e1.modify('right')
                        e2.modify('right')
                        e3.modify('right')
                        e4.modify('right')
                        for b in blocks:
                            b.rect.x += bk_vel_x
                        for b in bullets:
                            b.rect.x += bk_vel_x
                        for b in enemy_bullets:
                            b.rect.x += bk_vel_x
                        for m in modifiers:
                            m.rect.x += bk_vel_x
                        for b in enemys:
                            b.rect.x += bk_vel_x
                        for b in generators:
                            b.rect.x += bk_vel_x
                        for b in bosses:
                            b.rect.x += bk_vel_x

            elif player.velx < 0:
                if player.rect.left < limit_left:
                    if bk_pos_x < 0:
                        player.rect.left = limit_left
                        bk_pos_x -= bk_vel_x
                        #Enemigos seteados en el mapa
                        enemy1.modify('left')
                        enemy2.modify('left')
                        enemy3.modify('left')
                        enemy4.modify('left')
                        enemy5.modify('left')
                        #Enemigos generados
                        eg1.modify('left') 
                        eg2.modify('left') 
                        eg3.modify('left') 
                        eg4.modify('left') 
                        e1.modify('left')
                        e2.modify('left')
                        e3.modify('left')
                        e4.modify('left')
                        for b in blocks:
                            b.rect.x -= bk_vel_x
                        for b in bullets:
                            b.rect.x -= bk_vel_x
                        for b in enemy_bullets:
                            b.rect.x -= bk_vel_x
                        for m in modifiers:
                            m.rect.x -= bk_vel_x
                        for b in enemys:
                            b.rect.x -= bk_vel_x
                        for b in generators:
                            b.rect.x -= bk_vel_x
                        for b in bosses:
                            b.rect.x -= bk_vel_x

            elif player.vely > 0:
                if player.rect.bottom > limit_bottom:
                    if bk_pos_y > bk_limit_y:
                        player.rect.bottom = limit_bottom
                        bk_pos_y += bk_vel_y
                        #Enemigos seteados en el mapa
                        enemy1.modify('bottom')
                        enemy2.modify('bottom')
                        enemy3.modify('bottom')
                        enemy4.modify('bottom')
                        enemy5.modify('bottom')
                        #Enemigos generados
                        eg1.modify('bottom')
                        eg2.modify('bottom')
                        eg3.modify('bottom')
                        eg4.modify('bottom')
                        e1.modify('bottom')
                        e2.modify('bottom')
                        e3.modify('bottom')
                        e4.modify('bottom')
                        for b in blocks:
                            b.rect.y += bk_vel_y
                        for b in bullets:
                            b.rect.y += bk_vel_y
                        for b in enemy_bullets:
                            b.rect.y += bk_vel_y
                        for m in modifiers:
                            m.rect.y += bk_vel_y
                        for b in enemys:
                            b.rect.y += bk_vel_y
                        for b in generators:
                            b.rect.y += bk_vel_y
                        for b in bosses:
                            b.rect.y += bk_vel_y

            elif player.vely < 0:
                if player.rect.top < limit_top:
                    if bk_pos_y < 0:
                        player.rect.top = limit_top
                        bk_pos_y -= bk_vel_y
                        #Enemigos seteados en el mapa
                        enemy1.modify('top')
                        enemy2.modify('top')
                        enemy3.modify('top')
                        enemy4.modify('top')
                        enemy5.modify('top')
                        #Enemigos generados
                        eg1.modify('top')
                        eg2.modify('top')
                        eg3.modify('top')
                        eg4.modify('top')
                        e1.modify('top')
                        e2.modify('top')
                        e3.modify('top')
                        e4.modify('top')
                        for b in blocks:
                            b.rect.y -= bk_vel_y
                        for b in bullets:
                            b.rect.y -= bk_vel_y
                        for b in enemy_bullets:
                            b.rect.y -= bk_vel_y
                        for m in modifiers:
                            m.rect.y -= bk_vel_y
                        for b in enemys:
                            b.rect.y -= bk_vel_y
                        for b in generators:
                            b.rect.y -= bk_vel_y
                        for b in bosses:
                            b.rect.y -= bk_vel_y

            # Actualizar e imprimir objetos
            players.update()
            enemys.update()
            bullets.update()
            enemy_bullets.update()
            generators.update()
            bosses.update()

            screen.fill(BLACK)

            blocks.draw(screen)
            screen.blit(background,[bk_pos_x,bk_pos_y])
            modifiers.draw(screen)
            players.draw(screen)
            enemys.draw(screen)
            bullets.draw(screen)
            enemy_bullets.draw(screen)
            generators.draw(screen)
            bosses.draw(screen)

            sprite_heal = matriz_ui[0][player.heal]
            screen.blit(sprite_heal, [20,-5])

            sprite_ammo = matriz_ui[1][player.ammo]
            screen.blit(sprite_ammo, [20,25])

            if player.upgrade > 0:
                sprite_up = matriz_ui[2][(player.upgrade//10)+1]
                screen.blit(sprite_up, [player.rect.x-10, player.rect.y-65])

            if boss.follow and not boss.death:
                sprite_boss = matriz_ui_boss[boss.heal-1][0]
                screen.blit(sprite_boss, [400,50])

            for e in enemys:
                sprite_h_e = matriz_ui[3][e.heal]
                screen.blit(sprite_h_e, [e.rect.x-10, e.rect.y-65])

            for g in generators:
                sprite_h_e = matriz_ui[4][g.heal]
                screen.blit(sprite_h_e, [g.rect.x-14, g.rect.y-55])

        else:
            text = "  PAUSA  "
            font = pg.font.Font(None, 100)
            img_text = font.render(text, True, YELLOW)
            screen.blit(img_text, [WITDH/2-175, LENGHT/2-50])

        pg.display.flip()
        clock.tick(20)

    # Fin de nivel
    if end == True or boss.death == True:
        font = pg.font.Font(None, 100)
        img_text = font.render(text, True, color_text)
        screen.blit(img_text, [WITDH/2-175, LENGHT/2-50])
        fade(WITDH,LENGHT)

def fade(width, height): 
    fade = pg.Surface((width, height))
    fade.fill((0,0,0))
    for alpha in range(0, 50):
        fade.set_alpha(alpha)
        screen.blit(fade, (0,0))
        pg.display.update()
        pg.time.delay(70)

def fade2(width, height): 
    fade = pg.Surface((width, height))
    fade.fill((0,0,0))
    for alpha in range(50, 0):
        fade.set_alpha(alpha)
        screen.blit(fade, (0,0))
        pg.display.update()
        pg.time.delay(70)

def next(scree):
        font = pg.font.Font(None, 36)
        text = "¡EXCELENTE!, ACABAMOS CON LOS ENEMIGOS DE LA NAVE," 
        text2 = "PERO AL PARECER LOS PILOTOS SE DIERON CUENTA Y DECIDIERON ATERRRIZARLA"
        text3 = "EN UN LUGAR MUY EXTRAÑO, SE ESCUCHAN SONIDOS RAROS, ECHEMOS UN VISTAZO"
        text4 = "RECUERDA, NUESTROS ALIADOS SE HAN VUELTO LOCOS, TEN CUIDADO."
        img_text = font.render(text, True, RED)
        img_text2 = font.render(text2, True, RED)
        img_text3 = font.render(text3, True, RED)
        img_text4 = font.render(text4, True, RED)

        rectanguloTextoPresent = img_text.get_rect()
        rectanguloTextoPresent.centerx = screen.get_rect().centerx
        rectanguloTextoPresent.centery = 250
        screen.blit(img_text, rectanguloTextoPresent)

        rectanguloTextoPresent2 = img_text2.get_rect()
        rectanguloTextoPresent2.centerx = screen.get_rect().centerx
        rectanguloTextoPresent2.centery = 280
        screen.blit(img_text2, rectanguloTextoPresent2)

        rectanguloTextoPresent3 = img_text3.get_rect()
        rectanguloTextoPresent3.centerx = screen.get_rect().centerx
        rectanguloTextoPresent3.centery = 310
        screen.blit(img_text3, rectanguloTextoPresent3)

        rectanguloTextoPresent4 = img_text4.get_rect()
        rectanguloTextoPresent4.centerx = screen.get_rect().centerx
        rectanguloTextoPresent4.centery = 340
        screen.blit(img_text4, rectanguloTextoPresent4)

        pg.display.flip()


#######################


def level_2(screen):
    # Loop de música de fondo
    pg.mixer.music.load("sounds/music.ogg")
    pg.mixer.music.play(-1)

    # Efectos de sonido
    cry = pg.mixer.Sound("sounds/cry.ogg")
    shot = pg.mixer.Sound("sounds/blaster.ogg")
    empty = pg.mixer.Sound("sounds/empty.ogg")
    glass = pg.mixer.Sound("sounds/glass.ogg")
    mario = pg.mixer.Sound("sounds/mario.ogg")
    metal = pg.mixer.Sound("sounds/metal.ogg")
    power = pg.mixer.Sound("sounds/power.ogg")
    reload = pg.mixer.Sound("sounds/reload.ogg")
    damage = pg.mixer.Sound("sounds/uh.ogg")
    lose = pg.mixer.Sound("sounds/lose.ogg")
    win = pg.mixer.Sound("sounds/win.ogg")
    fire = pg.mixer.Sound("sounds/fire.ogg")
    explosion = pg.mixer.Sound("sounds/explosion.ogg")

    # Recortar texturas
    sprite = pg.image.load("textures/player.png")
    matriz_player = []
    for row in range(26):
        for column in range(8):
                matriz_player.append([])
                frame = sprite.subsurface(96*column, 96*row, 96, 96)
                frame2 = frame.subsurface(12, 12, 72, 72)
                matriz_player[row].append(frame2)

    sprite = pg.image.load("textures/enemys.png")
    matriz_enemys = []
    for row in range(26):
        for column in range(8):
                matriz_enemys.append([])
                frame = sprite.subsurface(96*column, 96*row, 96, 96)
                frame2 = frame.subsurface(12, 12, 68, 72)
                matriz_enemys[row].append(frame2)

    matriz_ui = Cut("textures/ui.png", [11,5])
    matriz_bullets = Cut("textures/bullets.png", [2,1])
    matriz_ui_boss = Cut("textures/ui_boss.png", [1,16])
    matriz_boss = Cut("textures/boss.png", [6,6])

    # Grupos
    players = pg.sprite.Group()
    blocks = pg.sprite.Group()
    enemys = pg.sprite.Group()
    bullets = pg.sprite.Group()
    enemy_bullets = pg.sprite.Group()
    bosses = pg.sprite.Group()

    # Crear jugador
    player = Player2(matriz_player)
    players.add(player)


    # Crear enemigos / Enemy(pos, liminf, limsup, limizq, limder)
    enemy1 = Enemy([700,258], 0, 0, 0, 0, matriz_enemys, 'right')
    enemys.add(enemy1)

    enemy2 = Enemy([3120,360], 0, 0, 3120, 3320, matriz_enemys, 'left')
    enemys.add(enemy2)  

    enemy3 = Enemy([2460,1160], 0, 0, 2460, 2660, matriz_enemys, 'left')
    enemys.add(enemy3)

    enemy4 = Enemy([1715,1160], 0, 0, 1715, 1900, matriz_enemys, 'left')
    enemys.add(enemy4)

    enemy5 = Enemy([560,960], 0, 0, 0, 0, matriz_enemys, 'left')
    enemys.add(enemy5)

    enemy6 = Enemy([980,1670], 0, 0, 0, 0, matriz_enemys, 'left')
    enemys.add(enemy6)




    boss = Boss([3640, 1580], [990, 258], matriz_boss, 'left')
    bosses.add(boss)

    # Cargar fondo y determinar sus limites
    background = pg.image.load("map_2/map.png")
    info = background.get_rect()
    background_witdh = info[2]
    background_lenght = info[3]
    bk_limit_x = WITDH - background_witdh
    bk_limit_y = LENGHT - background_lenght
    bk_pos_x = 0
    bk_pos_y = 0
    bk_vel_x = -15
    bk_vel_y = -15
    limit_right = 900
    limit_left = 300
    limit_bottom = 400
    limit_top = 200

    # Contruir bloques y modificadores en el terreno
    with open("map_2/map.json") as file:
        data = json.load(file)

    layers = data["layers"]
    plts = layers[1]["data"]
    limit = layers[1]["width"]

    cont = 0
    posx = 0
    posy = 0
    for e in plts:
        if e != 0:
            b = Block2([32,32], [posx*32,posy*32], False)
            blocks.add(b)
        cont += 1
        posx += 1
        if cont >= limit:
            cont = 0
            posx = 0
            posy += 1

    player.blocks = blocks

    # Ciclo principal
    clock = pg.time.Clock()
    pause = False
    end = False
    end_game = False
    while (not end) and (not end_game):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pause = not pause

                if (not pause) and (not player.death):
                    player.velx = 0
                    player.vely = 0

                    if event.key == pg.K_d:
                        player.velx = 15

                    if event.key == pg.K_a:
                        player.velx = -15

                    if event.key == pg.K_w:
                        player.vely = -25
                        player.floor = False

                    '''if event.key == pg.K_s:
                        player.vely = 15'''

            if (not pause) and (not player.death):
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if player.ammo > 0:
                            #player.ammo -= 1
                            pi = player.rect.center
                            pf = event.pos
                            bullet = Bullet(matriz_bullets[0][0], pi, pf, False)
                            bullets.add(bullet)
                            if bullet.diff_x > 0:
                                player.look = "right"
                                player.row = 4
                            elif bullet.diff_x <= 0:
                                player.look = "left"
                                player.row = 17
                            shot.play()
                        else:
                            empty.play()

                if event.type == pg.KEYUP:
                    player.velx = 0
                    player.vely = 0
                    if player.look == "right":
                        player.row = 0
                        player.column = 0
                    elif player.look == "left":
                        player.row = 13
                        player.column = 0

        if not pause:
            # Colisión de balas del jugador
            for b in bullets:
                # Con bloques
                ls_col_b = pg.sprite.spritecollide(b, blocks, False)
                if len(ls_col_b) > 0:
                    if ls_col_b[0].attack == False:
                        metal.play()
                        bullets.remove(b)
                # Con enemigos
                ls_col_e = pg.sprite.spritecollide(b, enemys, False)
                if len(ls_col_e) > 0:
                    bullets.remove(b)
                    for e in ls_col_e:
                        e.heal -= 1
                # Con Boss
                ls_col_e = pg.sprite.spritecollide(b, bosses, False)
                if len(ls_col_e) > 0:
                    bullets.remove(b)
                    for e in ls_col_e:
                        metal.play()
                        e.heal -= 1

             # Colisión de balas del enemigo
            for b in enemy_bullets:
                # Con bloques
                ls_col_b = pg.sprite.spritecollide(b, blocks, False)
                if len(ls_col_b) > 0:
                    if ls_col_b[0].attack == False:
                        enemy_bullets.remove(b)
                # Con player
                ls_col_p = pg.sprite.spritecollide(b, players, False)
                if len(ls_col_p) > 0:
                    damage.play()
                    player.heal -=1
                    enemy_bullets.remove(b)    

            # Distancia entre el jugador y el enemigo
            for e in enemys: 
                diff_x_e = player.rect.x - e.rect.x
                diff_y_e = player.rect.y - e.rect.y
                if (-350 < diff_x_e < 350) and (-350 < diff_y_e < 350) and (e.death == False) and (e.temp2 < 0):
                    if diff_x_e > 0:
                        e.look = "right"
                        e.row = 4
                    elif diff_x_e <= 0:
                        e.look = "left"
                        e.row = 17
                    e.temp2 = 25 # Cadencia de Disparo
                    pi = e.rect.center
                    pf = player.rect.center
                    b = Bullet(matriz_bullets[0][1], pi, pf, False)
                    enemy_bullets.add(b)        

            # Distancia entre el jugador y el boss
            diff_x_b = player.rect.x - boss.rect.x
            diff_y_b = player.rect.y - boss.rect.y
            if (-400 < diff_x_b < 400) and (-400 < diff_y_b < 400):
                if diff_x_b <= 0:
                    boss.look = "left"
                elif diff_x_b > 0:
                    boss.look = "right"
                boss.follow = True
                boss.pf = [player.rect.x-50, player.rect.y-60]
                ls_col_bs = pg.sprite.spritecollide(player, bosses, False)
                if (len(ls_col_bs) > 0) and (boss.temp <= 0):
                    if boss.look == "right":
                        boss.row = 1
                    elif boss.look == "left":
                        boss.row = 4
                    fire.play()
                    damage.play()
                    player.heal -= 1
                    boss.temp = 20
            else:
                boss.follow = False      

            # Muerte de los enemigos
            for e in enemys:
                if (e.death == True) and (e.temp < 0):
                    cry.play()
                    enemys.remove(e)
            
            #Muerte del boss
            if (boss.death == True) and (boss.temp2 < 0):
                explosion.play()
                bosses.remove(boss)
            
            # Muerte del jugador
            if (player.death == True) and (player.temp < 0):
                players.remove(player)

            # Condicion de victoria
            if len(bosses) == 0:
                win.play()
                end_game = True
                text = "VICTORIA!"
                color_text = GREEN

            # Condicion de derrota
            if len(players) == 0:
                lose.play()
                end_game = True
                text = " DERROTA "
                color_text = RED


            '''#Colision 2 del jugador con bloques
            for tile in blocks:
                if tile[1].colliderect(player.rect.x, player.rect.y + dy,)'''

            # Colision del jugador con bloques
            ls_col = pg.sprite.spritecollide(player, blocks, False)
            for plataform in ls_col:

                if player.vely < 0:
                    if player.rect.top < plataform.rect.bottom:
                        player.rect.top = plataform.rect.bottom
                        player.vely = 0
                else:
                    if player.rect.bottom > plataform.rect.top:
                        player.rect.bottom = plataform.rect.top
                        player.vely = 0
                        player.floor = True

            # Desplazar escenario
            if player.velx > 0:
                if player.rect.right > limit_right:
                    if bk_pos_x > bk_limit_x:
                        player.rect.right = limit_right
                        bk_pos_x += bk_vel_x
                        enemy1.modify('right')
                        enemy2.modify('right')
                        enemy3.modify('right')
                        enemy4.modify('right')
                        enemy5.modify('right')
                        enemy6.modify('right')
                        for b in blocks:
                            b.rect.x += bk_vel_x
                        for b in bullets:
                            b.rect.x += bk_vel_x
                        for b in enemy_bullets:
                            b.rect.x += bk_vel_x
                        for b in enemys:
                            b.rect.x += bk_vel_x
                        for b in bosses:
                            b.rect.x += bk_vel_x

            elif player.velx < 0:
                if player.rect.left < limit_left:
                    if bk_pos_x < 0:
                        player.rect.left = limit_left
                        bk_pos_x -= bk_vel_x
                        enemy1.modify('left')
                        enemy2.modify('left')
                        enemy3.modify('left')
                        enemy4.modify('left')
                        enemy5.modify('left')
                        enemy6.modify('left')
                        for b in blocks:
                            b.rect.x -= bk_vel_x
                        for b in bullets:
                            b.rect.x -= bk_vel_x
                        for b in enemy_bullets:
                            b.rect.x -= bk_vel_x
                        for b in enemys:
                            b.rect.x -= bk_vel_x
                        for b in bosses:
                            b.rect.x -= bk_vel_x

            elif player.vely > 0:
                if player.rect.bottom > limit_bottom:
                    if bk_pos_y > bk_limit_y:
                        player.rect.bottom = limit_bottom
                        bk_pos_y += bk_vel_y
                        enemy1.modify('bottom')
                        enemy2.modify('bottom')
                        enemy3.modify('bottom')
                        enemy4.modify('bottom')
                        enemy5.modify('bottom')
                        enemy6.modify('bottom')
                        for b in blocks:
                            b.rect.y += bk_vel_y
                        for b in bullets:
                            b.rect.y += bk_vel_y
                        for b in enemy_bullets:
                            b.rect.y += bk_vel_y
                        for b in enemys:
                            b.rect.y += bk_vel_y
                        for b in bosses:
                            b.rect.y += bk_vel_y

            elif player.vely < 0:
                if player.rect.top < limit_top:
                    if bk_pos_y < 0:
                        player.rect.top = limit_top
                        bk_pos_y -= bk_vel_y
                        enemy1.modify('top')
                        enemy2.modify('top')
                        enemy3.modify('top')
                        enemy4.modify('top')
                        enemy5.modify('top')
                        enemy6.modify('top')
                        for b in blocks:
                            b.rect.y -= bk_vel_y
                        for b in bullets:
                            b.rect.y -= bk_vel_y
                        for b in enemy_bullets:
                            b.rect.y -= bk_vel_y
                        for b in enemys:
                            b.rect.y -= bk_vel_y
                        for b in bosses:
                            b.rect.y -= bk_vel_y

            # Actualizar e imprimir objetos
            players.update()
            enemys.update()
            bullets.update()
            enemy_bullets.update()
            bosses.update()
            screen.fill(BLACK)

            blocks.draw(screen)
            screen.blit(background,[bk_pos_x,bk_pos_y])
            players.draw(screen)
            enemys.draw(screen)
            bullets.draw(screen)
            enemy_bullets.draw(screen)
            bosses.draw(screen)

            sprite_heal = matriz_ui[0][player.heal]
            screen.blit(sprite_heal, [20,-5])

            sprite_ammo = matriz_ui[1][player.ammo]
            screen.blit(sprite_ammo, [20,25])

            if player.upgrade > 0:
                sprite_up = matriz_ui[2][(player.upgrade//10)+1]
                screen.blit(sprite_up, [player.rect.x-10, player.rect.y-65])

            if boss.follow and not boss.death:
                sprite_boss = matriz_ui_boss[boss.heal-1][0]
                screen.blit(sprite_boss, [400,50])

            for e in enemys:
                sprite_h_e = matriz_ui[3][e.heal]
                screen.blit(sprite_h_e, [e.rect.x-10, e.rect.y-65])

        else:
            text = "  PAUSA  "
            font = pg.font.Font(None, 100)
            img_text = font.render(text, True, YELLOW)
            screen.blit(img_text, [WITDH/2-175, LENGHT/2-50])

        pg.display.flip()
        clock.tick(20)

    # Fin de nivel
    if end == True or boss.death == True:
        font = pg.font.Font(None, 100)
        img_text = font.render(text, True, color_text)
        screen.blit(img_text, [WITDH/2-175, LENGHT/2-50])
        fade(WITDH,LENGHT)
        
def outro(screen):
    pass

if __name__ == "__main__":
    pg.init()
    screen = pg.display.set_mode([WITDH, LENGHT])
    intro(screen)
    pg.time.delay(3000)
    fade(WITDH,LENGHT)
    start(screen)
    level_1(screen)
    next(screen)
    pg.time.delay(9000)
    fade(WITDH,LENGHT)
    level_2(screen)
    outro(screen)
    pg.quit()