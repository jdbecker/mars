import sys
sys.path.append('client_lib/')

from PodSixNet.Connection import ConnectionListener, connection
from time import sleep
import pygame
import cPickle as pickle
import screen,tile,const
import socket

class Client(ConnectionListener):

    """Instance of this class runs on each user's machine. Manages communication
    with the server and relays data to the screen object.
    """

    def __init__(self):
        self.connected = False
        self.logged = False
        host = raw_input("Connect to IP?[default:'localhost']\n")
        if host == '':
            host = socket.gethostname()
        self.Connect((host,4001))
        while not self.connected:
            sleep(0.01)
            self.Pump()
            connection.Pump()
        self.login()
        self.clock = pygame.time.Clock()
        self.screen = screen.Screen()
        self.localThings = []

    def Network(self, data):
        pass
        #print data

    def Network_connected(self, data):
        self.connected = True
        print data

    def Network_message(self, data):
        print data['message']
        self.response = True

    def Network_logStatus(self, data):
        self.logged = data['logStatus']

    def Network_response(self, data):
        self.response = True

    def Network_update(self, data):
        seenThings = pickle.loads(data['package'])['things']
        updatedLocalThings = []
        for thing in seenThings:
            x, y = thing[0]
            tileset, num = thing[1]
            updatedLocalThings.append(tile.Tile(x,y,tileset,num))
        self.localThings = updatedLocalThings

    def login(self):
        while not self.logged:
            name = raw_input("What is your player name?\n")
            self.Send({'action':'login','name':name})
            self.response = False
            print self.response
            while not self.response:
                print "waiting for response"
                sleep(0.1)
                self.Pump()
                connection.Pump()

    def update(self):
        self.clock.tick(const.FPS)
        connection.Pump()
        self.Pump()
        for event in self.screen.draw(self.localThings):
            if event.type == pygame.QUIT:
                self.screen.close()
                self.Send({'action':'disconnected','data':None})
                self.Pump()
                connection.Pump()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.Send({'action':'button','button':'LEFT'})
                if event.key == pygame.K_RIGHT:
                    self.Send({'action':'button','button':'RIGHT'})
                if event.key == pygame.K_UP:
                    self.Send({'action':'button','button':'UP'})
                if event.key == pygame.K_DOWN:
                    self.Send({'action':'button','button':'DOWN'})


c = Client()
while c.screen.run:
    c.update()
c.Send({'action':'disconnected','data':None})
c.Pump()
