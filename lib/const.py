import pygame
import random


# Shared Constants
FPS = 30
TILESIZE = 32
TILESWIDE = 25
VIEWDIST = 11
PORT = 4001

TILESETS = {}

# TileNums
def Sand():
    """Aquire the tileNum for a random bit of empty sand."""
    return random.choice([5,6,7,8,18,19,20,21,31,32,33,34,44,45,46,47])


# Client Specific Constants
APPNAME = "Mars Client"

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
TILESETS["desert"] = (pygame.image.load("lib\imgs\desert_tileset32.png"),tiles)

