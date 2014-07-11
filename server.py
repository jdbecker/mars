import sys
sys.path.append('server_lib/')
import cPickle as pickle
import PodSixNet.Channel
import PodSixNet.Server
from time import sleep
import thing,state,const,socket,pygame

class ClientChannel(PodSixNet.Channel.Channel):

    """Handle incoming actions from clients."""

    def Network(self, data):
        """Simply print data received. For debugging."""
        print data
        return


class MarsServer(PodSixNet.Server.Server):

    """Manage the state of the game world and mediate interactions between
    clients and the game world.
    """

    channelClass = ClientChannel

    def __init__(self, *args, **kwargs):
        """Call PodSixNet's server initialization method, then initialize the
        state of the game world.
        """
        PodSixNet.Server.Server.__init__(self, *args, **kwargs)
        self.clock = pygame.time.Clock()
        self.state = state.State()

    def Connected(self, channel, addr):
        """Handle incoming connections, including logging them in as a player
        with a distinct player.channel"""

    def update(self):
        """Call every frame to keep connection and game state updated."""
        self.clock.tick(const.FPS)
        self.state.update()
        self.Pump()

    def display(self):
        """Call every frame to keep connected clients updated"""
        for player in self.state.playersOn:
            package = pickle.dumps({'things':self.state.view(player)})
            data = {'action':'update','package':package}
            player.channel.Send(data)

print "STARTING SERVER ON LOCALHOST"
thisServer = MarsServer(localaddr = (socket.gethostname(), const.PORT) )
while True:
    thisServer.update()
    thisServer.display()
