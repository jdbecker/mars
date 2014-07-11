import pygame
import random

# Server Constants
APPNAME = "Mars Server"
FPS = 30
TILESIZE = 32
TILESWIDE = 25
VIEWDIST = 11
PORT = 4001

# TileNums
def Sand():
    """Aquire the tileNum for a random bit of empty sand."""
    return random.choice([5,6,7,8,18,19,20,21,31,32,33,34,44,45,46,47])
