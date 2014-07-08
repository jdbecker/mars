class Velocity():

    """Track velocity vector."""
    
    def __init__(self, (x,y)=(0,0) ):
        """Initialize as x and y components, with the understanding
        that negative values for either imply the opposite direction
        """
        self.x = x
        self.y = y

    def stop(self):
        """Reset vector to x=0, y=0"""
        self.stopx()
        self.stopy()

    def stopx(self):
        """Zero x vector."""
        self.x = 0

    def stopy(self):
        """Zero y vector."""
        self.y = 0

    def stopped(self):
        """Return True if velocity = 0 in every direction."""
        return (self.x == 0 and self.y == 0)
