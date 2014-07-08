import sys
sys.path.append('lib/')

#"""
import PodSixNet.Channel
import PodSixNet.Server
from time import sleep

class ClientChannel(PodSixNet.Channel.Channel):
    def __init__(self, *args, **kwargs):
        PodSixNet.Channel.Channel.__init__(self, *args, **kwargs)
        self.state = State()
        self.users = []
    def Network(self,data):
        print data
    def Network_login(self):
        for thing in self.state.things:

class BoxesServer(PodSixNet.Server.Server):
    def __init__(self, *args, **kwargs):
        PodSixNet.Server.Server.__init__(self, *args, **kwargs)
    channelClass = ClientChannel
    def Connected(self,channel,addr):
        self.users.append(channel)
        print 'new connection:', channel

class State():
    def __init__(self):
        self.things = []

print "STARTING SERVER ON LOCALHOST"
boxesServe=BoxesServer()
while True:
    boxesServe.Pump()
    sleep(0.01)
    for user in boxesServe.users:
        pass
#"""

"""
import thing
import screen
p = thing.Thing((0,0))
p.setSpeed(10)
things = [p]
for x in range(-12,13):
    for y in range(-12,13):
        if (x+y)%2 == 1:
            things.append(thing.Thing((x,y)))
s = screen.Screen(p)
while s.run:
    s.update(things)
"""

"""
import axis
x = axis.Axis(0)
print x.display()
y = axis.Axis(0,34)
print y.display()
z = axis.Axis(0,32)
print z.display()
w = axis.Axis(0,-1)
print w.display()
u = axis.Axis(w)
print u.display()
print y.sees(x).display()
print x.intersects(y)
print y.intersects(x)
print y.sees(z).display()
print y.intersects(z)
print z.sees(y).display()
print z.intersects(y)
i = axis.Axis(3)
print i.display()
j = axis.Axis(4)
print j.display()
print i.intersects(j)
print j.intersects(i)
i.xsmal += 1
i.update()
print i.intersects(j)
print j.intersects(i)
"""

"""
import coor,axis
p1 = coor.Coor(0,5)
print p1.display()
x2 = axis.Axis(2)
y2 = axis.Axis(-3)
p2 = coor.Coor(x2,y2)
print p2.display()
print p2.sees(p1).display()
x3 = axis.Axis(x2)
y3 = axis.Axis(y2)
x3.xsmal += 31
x3.update()
p3 = coor.Coor(x3,y3)
print p2.display()
print p3.display()
print p3.intersects(p2)
print p2.intersects(p3)
x3.xsmal += 1
x3.update()
p3 = coor.Coor(x3,y3)
print p3.display()
print p3.intersects(p2)
print p2.intersects(p3)
p1.shiftx(3)
p2.shifty(-5)
p3.shiftx(100)
p1.snap()
p2.snap()
p3.snap()
print p1.display()
print p2.display()
print p3.display()
print p3.shiftSnapx(5), p3.display()
print p3.shiftSnapx(100), p3.display()
print p3.shiftSnapx(100), p3.display()
print p2.shiftSnapy(-32), p2.display()
print p2.shiftSnapy(-16), p2.display()
print p2.shiftSnapy(-16), p2.display()
"""

"""
import thing

t = thing.Thing( (0,0) )
p = thing.Thing( (3,3), "Player" )
print p.sees(t)
"""
