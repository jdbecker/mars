import thing

class State():

    """Maintain the state of the game, handle the interactions of entities
    within the game, and include a method to return a mini-state object
    representing the state of the game as a single player can see it.
    """

    def __init__(self):
        self.things = []

    def update(self):
        """Calls the update method of every thing maintained in the state.
        Should be called once per frame to manage the internal flow of time.
        """
        for thing in self.things:
            thing.update()

    def view(self,player):
        """Return a list of things as seen by a player."""
        seeThings = []
        for thing in self.things:
            seeThing = player.sees(thing)
            if seeThing.onScreen():
                seeThings.append(seeThing)
        return seeThings
