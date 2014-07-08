import coor,velocity,const
import copy
import pygame

class Thing():
    
    """High-level (and therefore inheritable) class to act as the framework for
    positional relation of... things."""
    
    def __init__(self, coords, name="something"):
        """Accept either a tuple of (x,y) or a coor object for coords."""
        if isinstance(coords, coor.Coor):
            newcoords = coords
        else:
            x = coords[0]
            y = coords[1]
            newcoords = coor.Coor(x,y)
        self.coords = newcoords
        self.name = name
        self.speed = 1
        self.vel = velocity.Velocity()

    def sees(self, thing2):
        """Use the sees method of self and thing2 coors to find their relative
        positions, then return a copy of thing2 with new coords.
        """
        seenThing = copy.deepcopy(thing2)
        seenThing.coords = self.coords.sees(thing2.coords)
        return seenThing


    def setSpeed(self, speed):
        """Modify movement speed."""
        self.speed = speed

    def update(self):
        """Call once per frame to keep the position of self updated for its
        velocity. Stop at gridlines.
        """
        if self.coords.shiftSnapx(self.vel.x):
            self.vel.stopx()
        if self.coords.shiftSnapy(self.vel.y):
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
        """Return true if both self is onScreen."""
        return self.coords.onScreen()

    def draw(self, surface):
        """Draw self onto surface using pygame."""
        x = self.coords.getPix()[0]
        y = self.coords.getPix()[1]
        rec = (x,y,const.TILESIZE,const.TILESIZE)
        pygame.draw.rect(surface, pygame.Color('black'), rec, 0)
