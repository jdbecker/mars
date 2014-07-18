import mobile

class Player(mobile.Mobile):

    """Special Thing for handling player information, such as channel and user
    id.
    """

    def __init__(self, name, newcoor, tile=("desert",311)):
        mobile.Mobile.__init__(self, newcoor, tile)
        self.name = name
        self.channel = None

    def setChannel(self, channel):
        """Set self.channel to channel."""
        self.channel = channel
