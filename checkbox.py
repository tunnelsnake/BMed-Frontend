import pygame
import math

class Checkbox(object):

    def __init__(self, x, y, scale, state=False):
        self.position = (x, y)
        self.scale = scale
        self.state = state

        self.checkbox_pos = pygame.image.load("res/checkbox_pos.png")
        self.checkbox_neg = pygame.image.load("res/checkbox_neg.png")

        self.sidelen = int(self.scale * self.checkbox_pos.get_width())



    def isClicked(self):
        mouse = pygame.mouse.get_pos()
        if self.position[0] < mouse[0] < self.position[0] + self.sidelen and self.position[1] < mouse[1] < self.position[1] + self.sidelen:
            return True
        else:
            return False


    def drawCheckbox(self, screen):
        if self.state:
            scaled = pygame.transform.scale(self.checkbox_pos,
                    (int(self.scale * self.checkbox_pos.get_width()),
                    int(self.scale * self.checkbox_pos.get_height())))
            screen.blit(scaled, self.position)
        else:
            scaled = pygame.transform.scale(self.checkbox_neg,
                    (int(self.scale * self.checkbox_neg.get_width()),
                     int(self.scale * self.checkbox_neg.get_height())))
            screen.blit(scaled, self.position)