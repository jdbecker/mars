import const
import pygame
import random

class Tile():

    """Handle drawing of tiles, and give tiles nice names for
    importing into other classes.
    """

    def __init__(self, x, y, tileset, num):
        """Identify and store tileset and tilenum. Tileset should be entered
        as a string.
        """
        self.x = x
        self.y = y
        self.num = num
        self.tileset = tileset
        self.src = const.TILESETS[self.tileset][0]
        self.rec = const.TILESETS[self.tileset][1][self.num]

    def draw(self, surface):
        """Draws self onto surface at coor."""
        surface.blit( self.src, [self.x,self.y], self.rec )

class Sand(Tile):

    """Creates a default empty sand tile."""

    def __init__(self):
        emptyTiles = [5,6,7,8,18,19,20,21,31,32,33,34,44,45,46,47]
        Tile.__init__(self, "desert", random.choice(emptyTiles))
