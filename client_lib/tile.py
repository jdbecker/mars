import const
import pygame
import random

class Tile():

    """Handle drawing of tiles, and give tiles nice names for
    importing into other classes.
    """

    def __init__(self, tileset, num=311):
        """Identify and store tileset and tilenum. Tileset should be entered
        as a string.
        """
        self.num = num
        self.tileset = tileset
        self.rec = const.TILESET[self.tileset][1][self.num]

    def draw(self, surface, coor):
        """Draws self onto surface at coor."""
        x = coor.getPix()[0]
        y = coor.getPix()[1]
        src = const.TILESET[self.tileset][0]
        surface.blit( src, [x,y], self.rec )

class Sand(Tile):

    """Creates a default empty sand tile."""

    def __init__(self):
        emptyTiles = [5,6,7,8,18,19,20,21,31,32,33,34,44,45,46,47]
        Tile.__init__(self, "desert", random.choice(emptyTiles))
