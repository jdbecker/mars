import const

class Axis():
    
    """Track a 1 dimensional coordinate in both tile coordinates and
    fraction of a tile.
    """
    
    def __init__(self, x, xsmal=0):
        """Can initialize with another Axis object to make a copy. Automatically
        call update method.
        """
        if isinstance(x, Axis):
            newx = x.x
            newxsmal = x.xsmal
        else:
            newx = x
            newxsmal = xsmal
        self.x = newx
        self.xsmal = newxsmal
        self.update()

    def update(self):
        """Ensure that if fractional component is less than 0 or greater than
        the number of pixels across a tile, adjust tile and fractional component
        appropriately (recursively).
        """
        if self.xsmal < 0:
            self.decx()
            self.update()
        if self.xsmal >= const.TILESIZE:
            self.incx()
            self.update()
        return self

    def decx(self):
        """Dec tile component and adjust fractional."""
        self.x -= 1
        self.xsmal += const.TILESIZE
        return

    def incx(self):
        """Inc tile component and adjust fractional."""
        self.x += 1
        self.xsmal -= const.TILESIZE
        return

    def sees(self, axis2):
        """Return axis object representing the relative location of axis2 from
        the perspective of Self.
        """
        assert isinstance(axis2, Axis), "object used as 'axis2' is no Axis object"
        return Axis( (axis2.x-self.x),(axis2.xsmal-self.xsmal) ).update()

    def display(self):
        """Return printable string of values for debugging."""
        return "%d+%d/%d"%(self.x, self.xsmal, const.TILESIZE)

    def intersects(self, axis2):
        """Return True when a line with length TILESIZE whose left point is at
        Self intersects another whose line starts at point axis2.
        """
        return bool( self.sees(axis2).x == 0 or axis2.sees(self).x == 0 )

    def shift(self, deltax):
        """Adjust xsmal such that self moves deltax pixels and updates"""
        self.xsmal += deltax
        self.update()
        return

    def snap(self):
        """Snap to gridlines. Round to nearest tile component and reset
        fractional to 0. Return True if successful. Return False if
        halfway in-between 2 gridpoints
        """
        half = (const.TILESIZE*1.0)/2
        if self.xsmal == 0:
            return True
        if self.xsmal < half:
            self.xsmal = 0
            return True
        if self.xsmal > half:
            self.xsmal = 0
            self.x +=1
            return True
        return False

    def shiftSnap(self, deltax):
        """Adjust xsmal such that self moves the lesser of deltax pixels or
        to the nearest gridline, then updates. Returns True if at gridline."""
        if (deltax < 0 and -1*deltax > const.TILESIZE) or (deltax > 0 and deltax > const.TILESIZE):
            deltax = const.TILESIZE
        if self.xsmal != 0:
            if deltax < 0 and -1*deltax >= self.xsmal:
                self.xsmal = 0
                self.update()
                return True
            if deltax > 0 and deltax >= (const.TILESIZE-self.xsmal):
                self.xsmal = const.TILESIZE
                self.update()
                return True
        self.shift(deltax)
        if self.xsmal == 0:
            return True
        else:
            return False

    def onScreen(self):
        """Return True if self within VIEWDIST of 0."""
        dist = self.x * const.TILESIZE + self.xsmal
        viewdist = (const.VIEWDIST+1) * const.TILESIZE
        return ( dist > -1*viewdist and dist < viewdist )

    def getPix(self):
        """Return pixel value conversion of axis value, including shift to
        screen center via TILESWIDE/2 component."""
        return (self.x + const.TILESWIDE/2)*const.TILESIZE + self.xsmal
