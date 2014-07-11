import pygame

# Client Constants
APPNAME = "Mars Client"
FPS = 30

TILESET = {}

# Build Desert Tileset
tiles = []
for tilenum in range(312):
    y = 0
    while tilenum >=13:
        y += 1
        tilenum -= 13
    x = tilenum
    x = x * TILESIZE
    y = y * TILESIZE
    tiles.append( pygame.Rect( x, y, TILESIZE, TILESIZE ) )
TILESET["desert"] = (pygame.image.load("lib\desert_tileset32.png"),tiles)
