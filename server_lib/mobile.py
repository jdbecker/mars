import thing,velocity

class Mobile(Thing):

    """Any Thing that can move."""

    def __init__(self, newcoor, tile):
        thing.Thing.__init__(self, newcoor, tile)
        self.speed = 1
        self.vel = velocity.Velocity()

    def moveLeft(self):
        """If velocity is zero (meaning animation is not currently in progress)
        initiate velocity to the left."""
        if self.stopped():
            self.vel.x -= self.speed

    def moveRight(self):
        """If velocity is zero (meaning animation is not currently in progress)
        initiate velocity to the right."""
        if self.stopped():
            self.vel.x += self.speed

    def moveUp(self):
        """If velocity is zero (meaning animation is not currently in progress)
        initiate velocity to the up."""
        if self.stopped():
            self.vel.y -= self.speed

    def moveDown(self):
        """If velocity is zero (meaning animation is not currently in progress)
        initiate velocity to the down."""
        if self.stopped():
            self.vel.y += self.speed

    def stopped(self):
        """Call the 'stopped' method for self's velocity object. Return True if
        self is not moving."""
        return self.vel.stopped()

    def update(self):
        """Call once per frame to keep the position of self updated for its
        velocity. Stop at gridlines.
        """
        if self.coor.shiftSnapx(self.vel.x):
            self.vel.stopx()
        if self.coor.shiftSnapy(self.vel.y):
            self.vel.stopy()
        return
