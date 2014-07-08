import axis

class Coor():

    """Handle the grouping of axis pars into a 2 dimensional coordinate."""

    def __init__(self, x, y):
        """X and Y can be initialized using axis objects or ints."""
        self.x = axis.Axis(x)
        self.y = axis.Axis(y)

    def display(self):
        """Return printable string of coordinates for debugging."""
        return "(%s, %s)"%( self.x.display(), self.y.display() )

    def sees(self, coor2):
        """Return Coor object representing the relative location of
        coor2 from the perspective of Self.
        """
        assert isinstance(coor2, Coor), "object used as 'coor2' is no Coor object"
        return Coor( (self.x.sees(coor2.x)), (self.y.sees(coor2.y)) )

    def intersects(self, coor2):
        """Return True if a tile with coor=Self intersects with a tile with
        coor=coor2.
        """
        assert isinstance(coor2, Coor)
        return bool( self.x.intersects(coor2.x) and self.y.intersects(coor2.y) )

    def shiftx(self, deltax):
        """Adjust coordinates 'deltax' left(-) or right(+)."""
        self.x.shift(deltax)
        return

    def shifty(self, deltay):
        """Adjust coordinates 'deltax' up(-) or down(+)."""
        self.y.shift(deltay)
        return

    def shiftSnapx(self, deltax):
        """Adjust coordinates 'deltax' left or right, snapping to any passed
        gridlines. Return True if on a gridline, False otherwise."""
        return self.x.shiftSnap(deltax)

    def shiftSnapy(self, deltay):
        """Adjust coordinates 'deltax' left or right, snapping to any passed
        gridlines. Return True if on a gridline, False otherwise."""
        return self.y.shiftSnap(deltay)

    def snap(self):
        """Snap to gridlines. Call the snap method for both x and y and
        return True if successful for both. False if either fails."""
        return self.x.snap() and self.y.snap()

    def onScreen(self):
        """Return true if both x and y axis values are onScreen."""
        return self.x.onScreen() and self.y.onScreen()

    def getPix(self):
        """Return tuple of pixel values of x and y axis."""
        return (self.x.getPix(), self.y.getPix())
