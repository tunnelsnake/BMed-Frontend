import pygame
from checkbox import Checkbox as CB



FLYWHEEL_CENTER_X = 0
FLYWHEEL_CENTER_Y = 0
FLYWHEEL_CENTER = (FLYWHEEL_CENTER_X, FLYWHEEL_CENTER_Y)
FLYWHEEL_X_REL = 940
FLYWHEEL_Y_REL = 940


class UI(object):

    def __init__(self, x, y, scale=1.0):

        self.scale = scale
        self.x = x
        self.y = y
        self.position = (x, y)

        self.flywheel = pygame.image.load("res/stator_newest-01.png")
        self.pump = pygame.image.load("res/pump.png")
        self.panel = pygame.image.load("res/UI_Panel.png")

        self.pumpUICase_pos = pygame.image.load("res/Pump_UI-01.png")
        self.pumpUICase_neg = pygame.image.load("res/Pump_UI-02.png")

        self.flywheelAnimCTR = 0
        self.flywheelSpeedModifier = 2.0
        self.flywheelAnimInterpRange = [0, 360]


        self.checkboxes = []
        self.checkboxes.append(CB(x + int(scale * 270), y + int(scale * 90), self.scale, False))
        self.checkboxes.append(CB(x + int(scale * 270), y + int(scale * 400), self.scale, False))
        self.checkboxes.append(CB(x + int(scale * 1650), y + int(scale * 90), self.scale, False))
        self.checkboxes.append(CB(x + int(scale * 1650), y + int(scale * 400), self.scale, False))
        self.checkboxes.append(CB(x + int(scale * 3500), y + int(scale * 90), self.scale, False))
        self.checkboxes.append(CB(x + int(scale * 3500), y + int(scale * 400), self.scale, False))


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



    def drawUIPanel(self, screen, PumpState=True):
        scaled = pygame.transform.scale(self.panel,
                        (int(self.scale * self.panel.get_width()),
                         int(self.scale * self.panel.get_height())))
        screen.blit(scaled, self.position)

        if PumpState:
            pumpUICase = self.pumpUICase_pos
        else:
            pumpUICase = self.pumpUICase_neg

        pumpUICaseScale = .602 * self.scale
        offsetx = 5000
        offsety = -5

        pumpUICasePos = (self.x + int(self.scale * offsetx), self.y + int(self.scale * offsety))
        scaled = pygame.transform.scale(pumpUICase,
                                        (int(pumpUICaseScale * pumpUICase.get_width()),
                                         int(pumpUICaseScale * pumpUICase.get_height())))

        # Calculate the offset for the pumpCaseUI element

        screen.blit(scaled, pumpUICasePos)

        if PumpState:
            self.flywheelAnimCTR += int(self.flywheelSpeedModifier)

        rotorScale = .2
        rotorOffsetX = 5415
        rotorOffsetY = 395

        self.drawRotateFlywheel(screen, self.x + int(self.scale * rotorOffsetX),
                                self.y + int(self.scale * rotorOffsetY),
                                self.scale * rotorScale, self.flywheelAnimCTR,
                                angle_interp=self.flywheelAnimInterpRange)

        for checkbox in self.checkboxes:
            checkbox.drawCheckbox(screen)




