import pygame
import math

BTN_OUTLINE = (35, 35, 35)
BTN_OUTLINE_WIDTH = 2
BTN_BG = (200, 200, 200)
BTN_FG = (51, 51, 51)

class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Button(object):

    def __init__(self, x, y, radius, id):
        self.position = Coordinate(x, y)
        self.radius = radius
        self.id = id

    def isClicked(self):
        mouse = pygame.mouse.get_pos()
        if (math.sqrt(((mouse[0] - self.position.x)**2)+((mouse[1] - self.position.y)**2))) < self.radius:
            return True
        else:
            return False

    def getCenter(self):
        return self.position.x, self.position.y

    def draw(self, screen):
        #circle(surface, color, center, radius) -> Rect
        #pygame.draw.rect(screen, [red, blue, green], [left, top, width, height], filled)
        #rect(surface, color, rect) -> Rect

        pygame.draw.circle(screen, (255, 0, 0), self.getCenter(), self.radius)


