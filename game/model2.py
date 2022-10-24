from library import *

# -------------------------------------------------------------------------
# Jugador / LV2
# -------------------------------------------------------------------------
class Player2(pg.sprite.Sprite):
    def __init__(self, matriz):
        pg.sprite.Sprite.__init__(self)
        self.matriz = matriz
        self.limit = [0,1,4,3,3,6,0,0,1,4,3,3,6,0,1,4,3,3,6,0,0,1,4,3,3,6]
        self.row = 0
        self.column = 0
        self.image = self.matriz[self.row][self.column]
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 0
        self.velx = 0
        self.vely = 0
        self.blocks = pg.sprite.Group()
        self.look = "right"
        self.heal = 9
        self.ammo = 9
        self.upgrade = 0
        self.floor = False
        self.death = False
        self.temp = 6 #Temp para animacion de muerte
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def update(self):
        dx = 0
        dy = 0
        # Animación
        self.image = self.matriz[self.row][self.column]
        if self.column < self.limit[self.row]:
            self.column += 1
        else:
            if self.velx == 0:
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

        self.rect.x += self.velx
        if self.rect.right > WITDH:
            self.rect.right = WITDH
            self.velx = 0

        if self.rect.left < 0:
            self.rect.left = 0
            self.velx = 0

        if not self.floor:
            aceleration = 1.5
            self.vely += aceleration

        self.rect.y += self.vely
        if self.rect.bottom > LENGHT:
            self.rect.bottom = LENGHT
            self.vely = 0
            self.floor = True
        else:
            self.floor = False

        if self.rect.top < 0:
            self.rect.top = 0
            self.vely = 0
            self.floor = False

# -------------------------------------------------------------------------
# Bloque / LV2
# -------------------------------------------------------------------------
class Block2(pg.sprite.Sprite):
    def __init__(self, dim, pos, attack=False):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface(dim)
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.attack = attack