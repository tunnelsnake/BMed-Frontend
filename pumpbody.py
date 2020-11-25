
import pygame
from screen import Screen
from button import *

BODY_SCALE = 0.35
CAP_SCALE = 0.35
THREADS_SCALE = 0.4

SCREEN_X = 235
SCREEN_Y = 522
SCREEN_SCALE = 2.0

CAP_X = 815
CAP_Y = -240

THREAD_X = CAP_X - 50
THREAD_Y = CAP_Y - 55

MAX_DISTANCE_CAP_ASY = 500


class Pump(object):

    def __init__(self, x, y, scale=BODY_SCALE):
        self.position = Coordinate(x, y)
        # Load all the assets and scale them according to what's given as an argument
        self.scale = scale
        self.body = pygame.image.load("res/body.png")
        self.threads = pygame.image.load("res/threads.png")
        self.cap = pygame.image.load("res/cap_no_threads.png")

        # Keep track of the transform of the cartridge and opacity of cap
        # Internally store an interpolation range, user settable
        self.cartridge_transform = 0
        self.cartridge_interp_range = (0, 100)

        # Keep track of the screen and its transform
        self.Screen = Screen(self.position.x + self.scale * SCREEN_X, self.position.y + self.scale * SCREEN_Y, self.scale * SCREEN_SCALE)
        self.Screen.loadImage("res/warning.png")

        # Make an array of buttons:
        self.Buttons = []
        for n in range(0, 5):
            self.Buttons.append(Button(self.position.x + self.scale * 790, self.position.y + self.scale * 596 + self.scale * 115 * n, self.scale*50, n))


    def drawBody(self, screen):
        scaled = pygame.transform.scale(self.body, (int(self.scale * self.body.get_width()), int(self.scale * self.body.get_height())))
        screen.blit(scaled, (self.position.x, self.position.y))

    def drawThread(self, screen, offsetx=0, offsety=0):
        scaled = pygame.transform.scale(self.threads, (int(THREADS_SCALE * self.scale * self.body.get_width()),
                                                       int(THREADS_SCALE * self.scale * self.body.get_height())))
        screen.blit(scaled, (self.position.x + offsetx + self.scale * THREAD_X, self.position.y + offsety + self.scale * THREAD_Y))

    def drawCap(self, screen, offsetx=0, offsety=0):
        scaled = pygame.transform.scale(self.cap, (int(CAP_SCALE * self.scale * self.body.get_width()),
                                                   int(CAP_SCALE * self.scale * self.body.get_height())))
        screen.blit(scaled, (self.position.x + offsetx + self.scale * CAP_X, self.position.y + offsety + self.scale * CAP_Y))

    def drawCapThreadRelative(self, screen, n=0, interp_range=(0, 100)):
        self.cartridge_interp_range = interp_range
        yoffset = self.scale * (n * MAX_DISTANCE_CAP_ASY) / max(interp_range)
        self.drawCap(screen, 0, -yoffset)
        self.drawThread(screen, 0, -yoffset)







