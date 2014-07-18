import pygame
import const

class Screen():

    """Run the display and interface."""

    def __init__(self):
        """Initialize the pygame window."""
        pygame.init()
        width  = const.TILESIZE*const.TILESWIDE
        height = const.TILESIZE*const.TILESWIDE
        self.surface = pygame.display.set_mode((width,height))
        pygame.display.set_caption(const.APPNAME)
        self.run = True

    def draw(self, tiles):
        """Update loop, called once per frame, and draws each tile object
        in list tiles.
        """
        self.surface.fill(pygame.Color('white'))
        for tile in tiles:
            tile.draw(self.surface)
        pygame.display.flip()
        return pygame.event.get()

    def close(self):
        self.run = False
        pygame.display.quit()
