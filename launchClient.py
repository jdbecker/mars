import sys
sys.path.append('lib/')
import client

localClient = client.Client()
while localClient.screen.run:
    localClient.update()
