import pygame
from button import Coordinate

SCREEN_OUTLINE_COLOR = (35, 35, 35)
SCREEN_OUTLINE_WIDTH = 4
SCALE = 1.0

class Screen(object):

    def __init__(self, x, y, scale=SCALE):
        self.position = Coordinate(x, y)
        self.width = 240
        self.height = 320
        self.scale = scale
        self.currentImage = None

    def loadAllAssets(self):
        pass

    def loadImage(self, imagePath):
        self.currentImage = pygame.image.load(imagePath)


    def draw(self, screen):
        if self.currentImage is None:
            print("Tried to draw Screen with no image selected!")
            exit(-1)

        scaled = pygame.transform.scale(self.currentImage, (int(self.scale * self.width), int(self.scale * self.height)))
        screen.blit(scaled, (self.position.x, self.position.y))
