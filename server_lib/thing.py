import coor,velocity,const
import copy
import pygame

class Thing():
    
    """High-level (and therefore inheritable) class to act as the framework for
    positional relation of... things."""
    
    def __init__(self, newcoor, tile=None ):
        """Accept either a tuple of (x,y) or a coor object for coor. Use a tuple
        for newtile = (tileType,tileNum)"""
        if isinstance(newcoor, coor.Coor):
            self.coor = newcoor
        else:
            x = newcoor[0]
            y = newcoor[1]
            self.coor = coor.Coor(x,y)
        if not tile:
            tile = ( "desert", const.Sand() )
        self.tile = tile

    def sees(self, thing2):
        """Use the sees method of self and thing2 coors to find their relative
        positions, then return a copy of thing2 with new coor.
        """
        seenThing = copy.deepcopy(thing2)
        seenThing.coor = self.coor.sees(thing2.coor)
        return seenThing

    def update(self):
        """Does nothing for non-mobile things, unless specifically extended."""
        pass

    def visible(self):
        """Return true if self is visible to a viewer at 0,0"""
        return self.coor.onScreen()

    def view(self):
        """Return self as a nested tuple in the form ( (x, y), (tileType,
        tileNum) )"""
        x,y = self.coor.getPix()
        tileset,num = self.tile
        return ( (x,y), (tileset,num) )
