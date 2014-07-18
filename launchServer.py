import sys
sys.path.append('lib/')
import server,socket

PORT = 4001
thisServer = server.MarsServer(localaddr = (socket.gethostname(), PORT) )
while 1:
    thisServer.update()
    thisServer.display()
