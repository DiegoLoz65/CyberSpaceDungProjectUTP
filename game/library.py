import pygame as pg

GREEN = [0,255,0]
RED = [255,0,0]
BLUE = [0,0,255]
PURPLE = [240,0,255]
WHITE = [255,255,255]
BLACK = [0,0,0]
YELLOW = [255,255,0]
ORANGE = [255,100,10]

WITDH = 1200
LENGHT = 600

def Bresenham(x0, y0, x1, y1):
    dx = x1 - x0
    dy = y1 - y0

    xsign = 1 if dx > 0 else -1
    ysign = 1 if dy > 0 else -1

    dx = abs(dx)
    dy = abs(dy)

    if dx > dy:
        xx, xy, yx, yy = xsign, 0, 0, ysign
    else:
        dx, dy = dy, dx
        xx, xy, yx, yy = 0, ysign, xsign, 0

    D = 2*dy - dx
    y = 0

    for x in range(dx + 1):
        yield x0 + x*xx + y*yx, y0 + x*xy + y*yy
        if D >= 0:
            y += 1
            D -= 2*dx
        D += 2*dy

def Cut(img, dimensions):
    sprite = pg.image.load(img)
    info = sprite.get_rect()
    sprite_witdh = info[2]
    sprite_lenght = info[3]

    columns = dimensions[0]
    rows = dimensions[1]

    despl_x = sprite_witdh//columns
    despl_y = sprite_lenght//rows

    matriz = []
    for row in range(rows):
        for column in range(columns):
                matriz.append([])
                frame = sprite.subsurface(despl_x*column, despl_y*row, despl_x, despl_y)
                matriz[row].append(frame)
    return matriz
