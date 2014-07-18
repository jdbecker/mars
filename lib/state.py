import thing,player

class State():

    """Maintain the state of the game, handle the interactions of entities
    within the game, and include a method to return a mini-state object
    representing the state of the game as a single player can see it.
    """

    def __init__(self):
        self.things = []
        self.playersOn = {}
        self.playersOff = []
        for x in [i-12 for i in range(25)]:
            for y in [i-12 for i in range(25)]:
                self.things.append(thing.Thing((x,y)))

    def update(self):
        """Calls the update method of every thing maintained in the state.
        Should be called once per frame to manage the internal flow of time.
        """
        for thing in self.things:
            thing.update()
        for channel in self.playersOn:
            self.playersOn[channel].update()

    def logoff(self, channel):
        """Move the player associated with channel to playersOff."""
        self.playersOff.append(self.playersOn[channel])
        del self.playersOn[channel]

    def login(self, channel, name):
        """Parse existing players on and off, search for one that has a name
        matching login name. If the player exists and is off, move them to on
        and update their channel information. If the player doesn't exist,
        create them. If the player is already on, fail. Return True if
        successful.
        """
        if self.alreadyConnected(channel):
            return (True, "Resuming session as "+self.playersOn[channel].name)

        activePlayer = self.activePlayer(name)
        if activePlayer:
            return (False, activePlayer.name+" is already being used.")

        playerOffline = self.playerOffline(name)
        if playerOffline:
            self.playersOn[channel] = playerOffline
            self.playersOff.remove(playerOffline)
            return (True, "Logged in as "+playerOffline.name)

        playerNew = self.playerNew(name)
        if playerNew:
            self.playersOn[channel] = playerNew
            return (True, "Created player "+playerNew.name+" and logged in")

        return (False, "Failed to log in: Internal Server Error.")

    def alreadyConnected(self, channel):
        """Check to see if the given channel is already connected to a player."""
        if channel in self.playersOn:
            return True
        else:
            return False

    def activePlayer(self, name):
        """Given a name, check the logged on players' names and return a player
        with the name given if is already in use.
        """
        for channel in self.playersOn:
            if name == self.playersOn[channel].name:
                return self.playersOn[channel]
        return False

    def playerOffline(self, name):
        """Given a name, check the logged off players' names and return a player
        with the name given if exists.
        """
        for player in self.playersOff:
            if name == player.name:
                return player
        return False

    def playerNew(self, name):
        """Create a new player given a desired name, and return it."""
        newPlayer = player.Player(name, (0,0))
        print "Created new player",newPlayer.name
        return newPlayer

    def view(self,player):
        """Return a list of things as seen by a player as a nested tuple in the
        form: ( (x, y), (tileType, tileNum) )"""
        seeThings = []
        for thing in self.things:
            seeThing = player.sees(thing)
            if seeThing.visible():
                seeThings.append(seeThing.view())
        for channel in self.playersOn:
            seeThing = player.sees(self.playersOn[channel])
            if seeThing.visible():
                seeThings.append(seeThing.view())
        return seeThings
