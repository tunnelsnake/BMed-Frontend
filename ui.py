import pygame



FLYWHEEL_CENTER_X = 0
FLYWHEEL_CENTER_Y = 0
FLYWHEEL_CENTER = (FLYWHEEL_CENTER_X, FLYWHEEL_CENTER_Y)
FLYWHEEL_X_REL = 940
FLYWHEEL_Y_REL = 940


class UI(object):

    def __init__(self):
        self.flywheel = pygame.image.load("res/stator_recentered.png")
        self.pump = pygame.image.load("res/pump.png")
        self.panel = pygame.image.load("res/UI_Panel.png")


    def rot_center(self, image, rect, angle):
        """rotate an image while keeping its center"""
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = rot_image.get_rect(center=rect.center)
        return rot_image, rot_rect

    def drawRotateFlywheel(self, screen, x, y, scale, angle, angle_interp=[0, 3600]):
        scaled = pygame.transform.scale(self.flywheel, (int(scale * self.flywheel.get_width()),
                                                   int(scale * self.flywheel.get_height())))
        rotatedImg, rect = self.rot_center(scaled, scaled.get_rect(center=(x, y)), angle/10)
        screen.blit(rotatedImg, rect)

    def drawRotateAssembly(self, screen, x, y, scale, angle, angle_interp=[0, 3600]):
        scaled = pygame.transform.scale(self.pump, (int(scale * self.pump.get_width()),
                                                   int(scale * self.pump.get_height())))
        screen.blit(scaled, (x, y))
        self.drawRotateFlywheel(screen, x + FLYWHEEL_X_REL * scale, y + FLYWHEEL_Y_REL * scale,scale, angle)
