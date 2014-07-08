from PodSixNet.Connection import ConnectionListener, connection
from time import sleep
import pygame
import cPickle as pickle
import screen,thing,const
import socket

class Client(ConnectionListener):

    """Instance of this class runs on each user's machine. Manages communication
    with the server and relays data to the screen object.
    """

    def __init__(self):
        self.userid = None
        self.player = None
        self.things = []
        host = raw_input("Connect to IP?[default:'localhost']\n")
        if host == '':
            host = socket.gethostname()
        self.Pump()
        self.Connect((host,4001))
        sleep(0.01)
        while self.userid == None:
            self.Pump()
            connection.Pump()
        name = raw_input("What is your player name?\n")
        self.Send({'action':'login','name':name,'userid':self.userid})
        while self.player == None:
            self.Pump()
            connection.Pump()
        self.clock = pygame.time.Clock()
        self.screen = screen.Screen()

    def Network(self, data):
        pass
#        print data

    def Network_getuserid(self, data):
        self.userid = data['userid']
        print "connected with userid: "+str(self.userid)

    def Network_getplayer(self, data):
        print "Data received..."
        player = pickle.loads(data['package'])
        print "player %s received"%(player.name)
        self.player = player

    def Network_recThings(self, data):
        self.player = pickle.loads(data['package'])['player']
        self.things = pickle.loads(data['package'])['things']

    def update(self):
        self.clock.tick(const.FPS)
        self.Send({'action':'seeThings','userid':self.userid})
        connection.Pump()
        self.Pump()
        for event in self.screen.draw(self.things):
            if event.type == pygame.QUIT:
                self.screen.close()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.moveLeft()
                    self.Send({'action':'moveLeft','userid':self.userid})
                if event.key == pygame.K_RIGHT:
                    self.player.moveRight()
                    self.Send({'action':'moveRight','userid':self.userid})
                if event.key == pygame.K_UP:
                    self.player.moveUp()
                    self.Send({'action':'moveUp','userid':self.userid})
                if event.key == pygame.K_DOWN:
                    self.player.moveDown()
                    self.Send({'action':'moveDown','userid':self.userid})


c = Client()
while c.screen.run:
    pass
    c.update()
