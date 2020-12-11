import pygame
import colorsys
import random

def palette_swap(surf, old_c, new_c):
    # Copy the old surface to a new one
    img_copy = pygame.Surface(surf.get_size())
    # Fill the new surface with the new color
    img_copy.fill(new_c)
    # Set the surface's transparency color to the old color
    surf.set_colorkey(old_c)
    # Blit the new image onto the old one
    img_copy.blit(surf, (0, 0))
    return img_copy

def generate_palette(N = 4):
    HSV_tuples = [(x * 1.0 / N, 0.5, 0.5) for x in range(N)]
    RGB_tuples = map(lambda x: colorsys.hsv_to_rgb(*x), HSV_tuples)
    normalized_tuples = []
    for rgb in list(RGB_tuples):
        rgb = (int(random.random() * 255 * rgb[0] + 20), int(random.random() * 255 * rgb[1] + 20), int(random.random() * 255 * rgb[2] + 20))
        for val in rgb:
            if val > 255:
                val = 255
        normalized_tuples.append(rgb)
    return normalized_tuples


class Swatch(object):

    def __init__(self, scale):
        self.scale = scale
        self.swatchbase = pygame.image.load("res/ui/v2/coloricon.png")
        self.theme_primary = (188, 46, 60)
        self.theme_secondary = (76, 73, 158)
        self.theme_tertiary = (83, 84, 92)
        self.theme_bg = (134, 135, 141)


    def randomize(self):
        palette = generate_palette(4)
        self.replaceColor(self.theme_primary, palette[0])
        self.theme_primary = palette[0]
        self.replaceColor(self.theme_secondary, palette[1])
        self.theme_secondary = palette[1]
        self.replaceColor(self.theme_tertiary, palette[2])
        self.theme_tertiary = palette[2]
        self.replaceColor(self.theme_bg, palette[3])
        self.theme_tertiary = palette[3]

    def replaceColor(self, oldColor, newColor):
        self.swatchbase = palette_swap(self.swatchbase, oldColor, newColor)

    def draw(self, screen, x, y):
        scaled = pygame.transform.scale(self.swatchbase, (int(self.scale * self.swatchbase.get_width()),
                                                   int(self.scale * self.swatchbase.get_height())))
        screen.blit(scaled, (x, y))