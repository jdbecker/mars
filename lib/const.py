import pygame

# Constants
APPNAME = "Mars"
FPS = 30
TILESIZE = 32
TILESWIDE = 25
VIEWDIST = 11

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
