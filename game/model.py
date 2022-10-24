from library import *

# -------------------------------------------------------------------------
# Jugador / LV1
# -------------------------------------------------------------------------
class Player(pg.sprite.Sprite):
    def __init__(self, matriz):
        pg.sprite.Sprite.__init__(self)
        self.matriz = matriz
        self.limit = [0,1,4,3,3,6,0,0,1,4,3,3,6,0,1,4,3,3,6,0,0,1,4,3,3,6]
        self.row = 0
        self.column = 0
        self.image = self.matriz[self.row][self.column]
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 300
        self.velx = 0
        self.vely = 0
        self.blocks = pg.sprite.Group()
        self.look = "right"
        self.heal = 9
        self.ammo = 9
        self.upgrade = 0
        self.death = False
        self.temp = 6 #Temp para animacion de muerte

    def update(self):
        # Cambios temporales a causa del modificador upgrade
        if self.upgrade > 0:
            self.heal = 10
            self.ammo = 10
            if (0 <= self.row <= 5) or (13 <= self.row <= 18):
                self.row += 7
            if self.upgrade == 1:
                self.row -= 7
                self.heal -= 1
                self.ammo -= 1
            self.upgrade -= 1

        # Animación
        self.image = self.matriz[self.row][self.column]
        if self.column < self.limit[self.row]:
            self.column += 1
        else:
            if self.velx == self.vely:
                if self.look == "right":
                    self.row = 0
                elif self.look == "left":
                    self.row = 13
            elif self.velx > 0:
                self.look = "right"
                self.row = 3
            elif self.velx < 0:
                self.look = "left"
                self.row = 16
            self.column = 0

        # Colision con limites del mapa
        self.rect.x += self.velx
        if self.rect.right > WITDH:
            self.rect.right = WITDH
            self.velx = 0

        if self.rect.left < 0:
            self.rect.left = 0
            self.velx = 0

        self.rect.y += self.vely
        if self.rect.bottom > LENGHT:
            self.rect.bottom = LENGHT
            self.vely = 0

        if self.rect.top < 0:
            self.rect.top = 0
            self.vely = 0

        # Colision con bloques
        ls_col = pg.sprite.spritecollide(self, self.blocks, False)
        for b in ls_col:
            if b.attack:
                self.heal = 0
            else:
                if self.velx > 0:
                    if self.rect.right > b.rect.left:
                        self.rect.right = b.rect.left
                elif self.velx < 0:
                    if self.rect.left < b.rect.right:
                        self.rect.left = b.rect.right
                elif self.vely > 0:
                    if self.rect.bottom > b.rect.top:
                        self.rect.bottom = b.rect.top
                elif self.vely < 0:
                    if self.rect.top < b.rect.bottom:
                        self.rect.top = b.rect.bottom

        if self.heal <= 0:
            self.death = True

        if self.death == True:
            self.temp -= 1
            if self.look == "right":
                self.row = 5
            elif self.look == "left":
                self.row = 18

# -------------------------------------------------------------------------
# Enemigo / LV1
# -------------------------------------------------------------------------
class Enemy(pg.sprite.Sprite):
    def __init__(self, pos, liminf, limsup, limizq, limder, matriz, side):
        pg.sprite.Sprite.__init__(self)
        self.matriz = matriz
        self.limit = [0,1,4,3,3,6,0,0,1,4,3,3,6,0,1,4,3,3,6,0,0,1,4,3,3,6]
        self.row = 0
        self.column = 0
        self.image = self.matriz[self.row][self.column]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.limder = limder
        self.limizq = limizq
        self.limsup = limsup
        self.liminf = liminf
        self.velx = 5
        self.vely = 5
        self.look = side # side=lado
        self.mov = None
        self.heal = 3
        self.death = False
        self.temp = 4 # Temp para animacion de muerte
        self.temp2 = 25 # Temp para determinar la cadencia de disparo enemigo
        #self.shoot = False

    def update(self):
        self.temp2 -= 1

        self.image = self.matriz[self.row][self.column]
        if self.column < self.limit[self.row]:
            self.column += 1
        else:
            if self.velx == self.vely:
                if self.look == "right":
                    self.row = 0
                elif self.look == "left":
                    self.row = 13
            self.column = 0

        if self.limsup == 0 or self.liminf == 0:
            self.mov = 'h' # h = Horizontal
        if self.limizq == 0 or self.limder == 0:
            self.mov = 'v' # v = Vertical
        if self.limizq == 0 and self.limder == 0 and self.limsup == 0 and self.liminf == 0:
            self.mov = 'e' # e = Estático 

        if self.mov == 'h':
            self.rect.x += self.velx
            if self.rect.right > self.limder:
                self.velx = -10
                self.look = "left"
                self.row = 16

            if self.rect.left < self.limizq:
                self.look = "right"
                self.row = 3
                self.velx = 10

        if self.mov == 'v':
            self.rect.y += self.vely
            if self.look == "right":
                self.row = 3
            elif self.look == "left":
                self.row = 16
            if self.rect.top > self.limsup:
                self.vely = -10
            if self.rect.bottom < self.liminf:
                self.vely = 10

        if self.mov == 'e':
            self.velx = 0
            self.vely = 0

        if self.heal <= 0:
            self.death = True

        if self.death == True:
            self.temp -= 1
            if self.look == "right":
                self.row = 5
            elif self.look == "left":
                self.row = 18

    def modify(self, dir):
        if self.mov=='v':
            if dir == "top":
                self.limsup += 15
                self.liminf += 15
            if dir == "bottom":
                self.limsup -= 15
                self.liminf -= 15

        if self.mov=='h':
            if dir == "left":
                self.limizq += 15 
                self.limder += 15
            if dir == "right":
                self.limizq -= 15
                self.limder -= 15

# -------------------------------------------------------------------------
# Boss / LV1
# -------------------------------------------------------------------------
class Boss(pg.sprite.Sprite):
    def __init__(self, pi, pf, matriz, side):
        pg.sprite.Sprite.__init__(self)
        self.matriz = matriz
        self.limit = [0,5,2,0,5,2]
        self.row = 3
        self.column = 0
        self.image = self.matriz[self.row][self.column]
        self.rect = self.image.get_rect()
        self.rect.x = pi[0]
        self.rect.y = pi[1]
        self.pf = pf
        self.follow = False
        self.vect = list(Bresenham(pi[0], pi[1], pf[0], pf[1]))
        self.heal = 16
        self.look = side
        self.death = False
        self.temp = 20
        self.temp2 = 5 # Para animación de muerte.

    def update(self):
        self.temp -= 1

        self.image = self.matriz[self.row][self.column]
        if self.column < self.limit[self.row]:
            self.column += 1
        else:
            if self.look == "right":
                self.row = 0
            elif self.look == "left":
                self.row = 3
            self.column = 0

        if self.follow == True:
            self.vect = list(Bresenham(self.rect.x, self.rect.y, self.pf[0], self.pf[1]))
            if len(self.vect) > 10:
                self.rect.x = self.vect[10][0]
                self.rect.y = self.vect[10][1]

        if self.heal <= 0:
            self.death = True

        if self.death == True:
            self.temp2 -= 1
            if self.look == "right":
                self.row = 2
            if self.look == "left":
                self.row = 5

# -------------------------------------------------------------------------
# Bala / LV1
# -------------------------------------------------------------------------
class Bullet(pg.sprite.Sprite):
    def __init__(self, img, pi, pf, key):
        pg.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = pi[0]
        self.rect.y = pi[1]
        self.velx = 0
        self.vely = 0
        self.vect = list(Bresenham(pi[0], pi[1], pf[0], pf[1]))
        self.key = key
        '''self.cont = 0
        self.remove = False
        self.velBullet = 20'''
        if len(self.vect) > 20:
            self.diff_x = self.vect[20][0] - self.vect[0][0]
            self.diff_y = self.vect[20][1] - self.vect[0][1]
        else:
            self.diff_x = -20
            self.diff_y = 0

    def update(self):
        if self.key == True:
            self.rect.x += self.velx
            self.rect.y += self.vely
        elif self.key == False:
            self.rect.x += self.diff_x
            self.rect.y += self.diff_y
            '''self.rect.x = self.vect[self.cont][0]
            self.rect.y = self.vect[self.cont][1]
            if self.cont < len(self.vect)-self.velBullet:
                self.cont += self.velBullet
            if self.cont >= len(self.vect)-self.velBullet:
                self.remove = True'''

# -------------------------------------------------------------------------
# Modificadores / LV1
# -------------------------------------------------------------------------
class Modifier(pg.sprite.Sprite):
    def __init__(self, img, pos, type):
        pg.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.type = type

# -------------------------------------------------------------------------
# Bloques / LV1
# -------------------------------------------------------------------------
class Block(pg.sprite.Sprite):
    def __init__(self, img, pos, attack=False):
        pg.sprite.Sprite.__init__(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.attack = attack

# -------------------------------------------------------------------------
# Generador / LV1
# -------------------------------------------------------------------------
class Generator(pg.sprite.Sprite):
    def __init__(self, pos, matriz):
        pg.sprite.Sprite.__init__(self)
        self.matriz = matriz
        self.limit = [4]
        self.row = 0
        self.column = 0
        self.image = self.matriz[self.row][self.column]
        self.rect = self.image.get_rect()
        self.rect.x= pos[0]
        self.rect.y= pos[1]
        self.cant = 0
        self.heal = 5
        self.death = False
        self.temp = 100

    def update(self):
        self.temp -= 1

        self.image = self.matriz[self.row][self.column]
        if self.column < self.limit[self.row]:
            self.column += 1
        else:
            self.column = 0

        if self.heal <= 0:
            self.death = True