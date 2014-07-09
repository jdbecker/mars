import coor,velocity,const,tile
import copy
import pygame

class Thing():
    
    """High-level (and therefore inheritable) class to act as the framework for
    positional relation of... things."""
    
    def __init__(self, newcoor, name="something"):
        """Accept either a tuple of (x,y) or a coor object for coor."""
        if isinstance(newcoor, coor.Coor):
            self.coor = newcoor
        else:
            x = newcoor[0]
            y = newcoor[1]
            self.coor = coor.Coor(x,y)
        self.name = name
        self.tile = tile.Tile("desert")
        self.speed = 1
        self.vel = velocity.Velocity()

    def sees(self, thing2):
        """Use the sees method of self and thing2 coors to find their relative
        positions, then return a copy of thing2 with new coor.
        """
        seenThing = copy.deepcopy(thing2)
        seenThing.coor = self.coor.sees(thing2.coor)
        return seenThing

    def setTile(self, tile):
        self.tile = tile

    def setSpeed(self, speed):
        """Modify movement speed."""
        self.speed = speed

    def update(self):
        """Call once per frame to keep the position of self updated for its
        velocity. Stop at gridlines.
        """
        if self.coor.shiftSnapx(self.vel.x):
            self.vel.stopx()
        if self.coor.shiftSnapy(self.vel.y):
            self.vel.stopy()
        return

    def moveLeft(self):
        """If velocity is zero (meaning animation is not currently in progress)
        initiate velocity to the left."""
        if self.vel.stopped():
            self.vel.x -= self.speed

    def moveRight(self):
        """If velocity is zero (meaning animation is not currently in progress)
        initiate velocity to the right."""
        if self.vel.stopped():
            self.vel.x += self.speed

    def moveUp(self):
        """If velocity is zero (meaning animation is not currently in progress)
        initiate velocity to the up."""
        if self.vel.stopped():
            self.vel.y -= self.speed

    def moveDown(self):
        """If velocity is zero (meaning animation is not currently in progress)
        initiate velocity to the down."""
        if self.vel.stopped():
            self.vel.y += self.speed

    def stopped(self):
        """Call the 'stopped' method for self's velocity object. Return True if
        self is not moving."""
        return self.vel.stopped()

    def onScreen(self):
        """Return true if self is onScreen."""
        return self.coor.onScreen()

    def draw(self, surface):
        """Draw self's tile onto surface."""
        self.tile.draw(surface, self.coor)
