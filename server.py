import sys
sys.path.append('lib/')
import cPickle as pickle
import PodSixNet.Channel
import PodSixNet.Server
from time import sleep
import thing,state,const,socket,pygame

class ClientChannel(PodSixNet.Channel.Channel):

    """Handle incoming actions from clients."""

    def Network(self, data):
        """Simply print data received. For debugging."""
        pass
        #print data

    def Network_login(self, data):
        """Relay the name string contained in data to the server login method."""
        print data['name'],"received"
        self._server.login(self, data['name'])

    def Network_disconnected(self, data):
        """Relay the channel to the server's disconnect method."""
        self._server.disconnect(self)

    def Network_button(self, data):
        """Call the server's button push method."""
        self._server.button(self, data['button'])


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
        print "New connection:", channel, addr

    def disconnect(self, channel):
        """Pass the channel to the logoff method of the game state, to log
        out the current player.
        """
        self.state.logoff(channel)

    def login(self, channel, name):
        """Call the login method of the game state."""
        print "login method started"
        logStatus,message = self.state.login(channel, name)
        data = {'action':'message','message':message}
        channel.Send(data)
        if logStatus:
            data = {'action':'logStatus','logStatus':logStatus}
            channel.Send(data)

    def button(self, channel, button):
        """Relay the button push to the appropriate method."""
        if button == 'LEFT':
            self.state.playersOn[channel].moveLeft()
        if button == 'RIGHT':
            self.state.playersOn[channel].moveRight()
        if button == 'UP':
            self.state.playersOn[channel].moveUp()
        if button == 'DOWN':
            self.state.playersOn[channel].moveDown()

    def update(self):
        """Call every frame to keep connection and game state updated."""
        self.state.update()
        self.Pump()

    def display(self):
        """Call every frame to keep connected clients updated"""
        players = self.state.playersOn
        for channel in players:
            package = pickle.dumps({'things':self.state.view(players[channel])})
            data = {'action':'update','package':package}
            channel.Send(data)

print "STARTING SERVER ON LOCALHOST"
thisServer = MarsServer(localaddr = (socket.gethostname(), const.PORT) )
while True:
    thisServer.clock.tick(const.FPS)
    thisServer.update()
    thisServer.display()
