
from enum import Enum
import pygame
from swatch import Swatch
import time

class MenuState(Enum):
    boot = 0
    locked = 1
    unlock = 2
    menu_main = 3
    feed = 4
    settings = 5
    feed_in_progress = 6
    colors = 7
    change_pin = 8
    rate = 9
    rate_low = 10
    rate_mid = 11
    rate_high = 12
    volume = 13
    volume_bottom = 14
    volume_top = 15
    transfuse_paused = 16
    transfuse = 17
    color_confirm = 18
    change_pin_auth = 19
    change_pin_entry = 20
    change_pin_verify = 21
    alert_battery = 22
    alert_clog_empty = 23
    alert_tube_disconnect = 24
    alert_cart_disconnect = 25



Checkboxes = {
    "childlock" : 0,
    "clog" : 1,
    "removecartridge" : 2,
    "removeoutlet" : 3,
    "feedempty" : 4,
    "other" : 5
}




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


class MenuFSM(object):

    def __init__(self, Pump, UI, screen):
        self.Pump = Pump
        self.UI = UI
        self.pygameScreen = screen
        self.screen = Pump.Screen
        self.state = MenuState.locked

        self.anim_cartridge = False
        self.anim_hose = False
        self.anim_transfusion = True
        self.anim_cart_direction = False # True means outward / False means inward
        self.anim_hose_direction = False
        self.anim_cart_timer = 0
        self.anim_hose_timer = 0
        self.anim_transfusion_timer = 0
        self.anim_cartridge_interp = [0, 3600]
        self.anim_hose_interp = [0, 3600]
        self.anim_transfusion_timer_interp = [0, 500]
        self.anim_cartridge_delta = 100
        self.anim_hose_delta = 100
        self.anim_transfusion_delta = 0
        self.anim_transfusion_state = 0


        # To be keyed out on load (Theme colors)
        self.theme_primary = (188, 46, 60)
        self.theme_secondary = (76, 73, 158)
        self.theme_tertiary = (83, 84, 92)
        self.theme_bg = (134, 135, 141)

        # User stored theme
        self.theme_primary_user = self.theme_primary
        self.theme_secondary_user = self.theme_secondary
        self.theme_tertiary_user = self.theme_tertiary
        self.theme_bg_user = self.theme_bg

        # Create a swatch for the color selection screen
        self.swatch = Swatch(.125)
        self.swatch.randomize()

        # Load all the screens
        self.loadThemeAssets()

        # Prestored values in the pump
        self.rate = 60 # mL/hr
        self.volume = 25
        self.passcode_stored = "1111"
        self.passcode_entered = "1"
        self.passcode_change = "1"


    def applyTheme(self, img):
        if self.theme_primary != self.theme_primary_user:
            img = palette_swap(img, self.theme_primary, self.theme_primary_user)
        if self.theme_secondary != self.theme_secondary_user:
            img = palette_swap(img, self.theme_secondary, self.theme_secondary_user)
        if self.theme_tertiary != self.theme_tertiary_user:
            img = palette_swap(img, self.theme_bg, self.theme_bg_user)
        return img

    def loadThemeAssets(self):
        self.screen_locked = self.applyTheme(pygame.image.load("res/ui/v2/locked.png"))
        self.screen_unlock = self.applyTheme(pygame.image.load("res/ui/v2/unlock.png"))
        self.screen_palette = self.applyTheme(pygame.image.load("res/ui/v2/palette.png"))
        self.screen_main_menu = self.applyTheme(pygame.image.load("res/ui/v2/main_menu.png"))
        self.screen_feed = self.applyTheme(pygame.image.load("res/ui/v2/feed.png"))
        self.screen_settings = self.applyTheme(pygame.image.load("res/ui/v2/settings.png"))
        self.screen_rate = self.applyTheme(pygame.image.load("res/ui/v2/rate.png"))
        self.screen_rate_low = self.applyTheme(pygame.image.load("res/ui/v2/rate_low.png"))
        self.screen_rate_mid = self.applyTheme(pygame.image.load("res/ui/v2/rate_mid.png"))
        self.screen_rate_high = self.applyTheme(pygame.image.load("res/ui/v2/rate_top.png"))
        self.screen_volume = self.applyTheme(pygame.image.load("res/ui/v2/volume.png"))
        self.screen_volume_bottom = self.applyTheme(pygame.image.load("res/ui/v2/volume_bottom.png"))
        self.screen_volume_top = self.applyTheme(pygame.image.load("res/ui/v2/volume_top.png"))
        self.screen_color = self.applyTheme(pygame.image.load("res/ui/v2/color.png"))
        self.screen_transfuse = self.applyTheme(pygame.image.load("res/ui/v2/transfuse_play.png"))
        self.screen_transfuse_paused = self.applyTheme(pygame.image.load("res/ui/v2/transfuse_paused.png"))
        self.screen_color_confirm = self.applyTheme(pygame.image.load("res/ui/v2/color_confirm.png"))
        self.screen_pinauth = self.applyTheme(pygame.image.load("res/ui/v2/changepinauth.png"))
        self.screen_pinentry = self.applyTheme(pygame.image.load("res/ui/v2/changepin.png"))
        self.screen_pinverif = self.applyTheme(pygame.image.load("res/ui/v2/verifypin.png"))
        self.screen_alert_battery = self.applyTheme(pygame.image.load("res/ui/v2/alert_battery-01.png"))
        self.screen_alert_tube_disc = self.applyTheme(pygame.image.load("res/ui/v2/alert_tube_disc-01.png"))
        self.screen_alert_cart_disc = self.applyTheme(pygame.image.load("res/ui/v2/alert_cart_disc-01.png"))
        self.screen_alert_cart_empty = self.applyTheme(pygame.image.load("res/ui/v2/alert_clog_empty-01.png"))

        batteryicon = (pygame.image.load("res/ui/v2/batteryicon-01.png"))
        scale = .1
        self.batteryicon = pygame.transform.scale(batteryicon, (int(batteryicon.get_width() * scale), int(batteryicon.get_height() * scale)))


    def checkboxCallback(self, checkboxIndex, state):
        print("Checkbox index is {}, expected value is {}".format(checkboxIndex, Checkboxes["removecartridge"]))
        if checkboxIndex == Checkboxes["childlock"]:
            pass
        elif checkboxIndex == Checkboxes["clog"]:
            pass
        elif checkboxIndex is Checkboxes["removecartridge"]:
            if not self.anim_cartridge:
                self.anim_cartridge = True
                self.anim_cart_direction = not self.anim_cart_direction
            else:
                self.anim_cart_direction = not self.anim_cart_direction
        elif checkboxIndex == Checkboxes["removeoutlet"]:
            if not self.anim_hose:
                self.anim_hose = True
                self.anim_hose_direction = not self.anim_hose_direction
            else:
                self.anim_hose_direction = not self.anim_hose_direction
        elif checkboxIndex == Checkboxes["feedempty"]:
            pass
        elif checkboxIndex == Checkboxes["other"]:
            pass

    def buttonCallback(self, buttonIndex, button):
        if self.state == MenuState.boot:
            pass
        elif self.state == MenuState.locked:
            if buttonIndex == 4:
                if self.UI.checkboxes[Checkboxes["childlock"]].state:
                    self.state = MenuState.unlock
                    self.passcode_entered = "1"
                else:
                    self.state = MenuState.menu_main
        elif self.state == MenuState.unlock:
            if buttonIndex == 2:
                currentpasscode = list(self.passcode_entered)
                if int(currentpasscode[-1]) == 9:
                    currentpasscode[-1] = '0'
                    self.passcode_entered = currentpasscode
                else:
                    currentpasscode[-1] = str(int(currentpasscode[-1]) + 1)
                    self.passcode_entered = currentpasscode


            if buttonIndex == 3:
                if len(self.passcode_entered) == 4:
                    if self.passcode_entered == self.passcode_stored:
                        self.state = MenuState.menu_main
                    else:
                        self.passcode_entered = "1"
                else:
                    self.passcode_entered += "1"
            if buttonIndex == 4:
                self.state = MenuState.locked
        elif self.state == MenuState.menu_main:
            if buttonIndex == 2:
                self.state = MenuState.feed
            if buttonIndex == 3:
                self.state = MenuState.settings
            if buttonIndex == 4:
                self.state = MenuState.locked
        elif self.state == MenuState.settings:
            if buttonIndex == 2:
                self.passcode_entered = "1"
                self.state = MenuState.change_pin_auth
            elif buttonIndex == 3:
                self.state = MenuState.colors
            elif buttonIndex == 4:
                self.state = MenuState.menu_main
        elif self.state == MenuState.change_pin_auth:
            if buttonIndex == 2:
                currentpasscode = list(self.passcode_entered)
                if int(currentpasscode[-1]) == 9:
                    currentpasscode[-1] = '0'
                    self.passcode_entered = currentpasscode
                else:
                    currentpasscode[-1] = str(int(currentpasscode[-1]) + 1)
                    self.passcode_entered = currentpasscode


            if buttonIndex == 3:
                if len(self.passcode_entered) == 4:
                    if self.passcode_entered == self.passcode_stored:
                        self.passcode_change = "1"
                        self.state = MenuState.change_pin_entry
                    else:
                        self.passcode_entered = "1"
                else:
                    self.passcode_entered += "1"
            if buttonIndex == 4:
                self.state = MenuState.settings
        elif self.state == MenuState.change_pin_entry:
            if buttonIndex == 2:
                currentpasscode = list(self.passcode_change)
                if int(currentpasscode[-1]) == 9:
                    currentpasscode[-1] = '0'
                    self.passcode_change = currentpasscode
                else:
                    currentpasscode[-1] = str(int(currentpasscode[-1]) + 1)
                    self.passcode_change = currentpasscode

            if buttonIndex == 3:
                if len(self.passcode_change) == 4:
                        self.passcode_entered = "1"
                        self.state = MenuState.change_pin_verify

                else:
                    self.passcode_change += "1"
            if buttonIndex == 4:
                self.state = MenuState.settings
        elif self.state == MenuState.change_pin_verify:
            if buttonIndex == 2:
                currentpasscode = list(self.passcode_entered)
                if int(currentpasscode[-1]) == 9:
                    currentpasscode[-1] = '0'
                    self.passcode_entered = currentpasscode
                else:
                    currentpasscode[-1] = str(int(currentpasscode[-1]) + 1)
                    self.passcode_entered = currentpasscode


            if buttonIndex == 3:
                if len(self.passcode_entered) == 4:
                    if self.passcode_entered == self.passcode_change:
                        self.passcode_stored = self.passcode_change
                        self.state = MenuState.menu_main
                    else:
                        self.passcode_entered = "1"
                else:
                    self.passcode_entered += "1"

            if buttonIndex == 4:
                self.state = MenuState.settings
        elif self.state == MenuState.colors:
            if buttonIndex == 2:
                self.swatch.randomize()
                self.theme_primary_user = self.swatch.theme_primary
                self.theme_secondary_user = self.swatch.theme_secondary
                self.theme_tertiary_user = self.swatch.theme_tertiary
                self.theme_bg_user = self.swatch.theme_bg

            if buttonIndex == 3:
                self.theme_primary_user = self.theme_primary
                self.theme_secondary_user = self.theme_secondary
                self.theme_tertiary_user = self.theme_tertiary
                self.swatch.replaceColor(self.swatch.theme_primary, self.theme_primary)
                self.swatch.replaceColor(self.swatch.theme_secondary, self.theme_secondary)
                self.swatch.replaceColor(self.swatch.theme_tertiary, self.theme_tertiary)
                self.swatch.replaceColor(self.swatch.theme_bg, self.theme_bg)
                self.swatch.theme_tertiary = self.theme_tertiary
                self.theme_bg_user = self.theme_bg
                self.screen_color = self.applyTheme(self.screen_color)

            if buttonIndex == 4:
                self.state = MenuState.color_confirm

        elif self.state == MenuState.color_confirm:
            if buttonIndex == 3:
                self.loadThemeAssets()
                self.state = MenuState.settings
            if buttonIndex == 4:
                self.theme_primary_user = self.theme_primary
                self.theme_secondary_user = self.theme_secondary
                self.theme_tertiary_user = self.theme_tertiary
                self.state = MenuState.settings
        elif self.state == MenuState.feed_in_progress:
            if buttonIndex == 4:
                self.state = MenuState.menu_main
        elif self.state == MenuState.feed:
            if buttonIndex == 1:
                if self.UI.checkboxes[Checkboxes["other"]].state:
                    self.state = MenuState.alert_battery
                self.state = MenuState.transfuse
            if buttonIndex == 2:
                self.state = MenuState.rate
            if buttonIndex == 3:
                self.state = MenuState.volume
            if buttonIndex == 4:
                self.state = MenuState.menu_main
        elif self.state == MenuState.rate:
            if buttonIndex == 1:
                self.state = MenuState.rate_low
            elif buttonIndex == 2:
                self.state = MenuState.rate_mid
            elif buttonIndex == 3:
                self.state = MenuState.rate_high
            elif buttonIndex == 4:
                self.state = MenuState.menu_main
        elif self.state == MenuState.rate_low:
            if buttonIndex == 1:
                self.rate = 60
                self.state = MenuState.feed
            elif buttonIndex == 2:
                self.rate = 70
                self.state = MenuState.feed
            elif buttonIndex == 3:
                self.rate = 80
                self.state = MenuState.feed
            elif buttonIndex == 4:
                self.state = MenuState.rate
        elif self.state == MenuState.rate_mid:
            if buttonIndex == 1:
                self.rate = 90
                self.state = MenuState.feed
            elif buttonIndex == 2:
                self.rate = 100
                self.state = MenuState.feed
            elif buttonIndex == 3:
                self.rate = 110
                self.state = MenuState.feed
            elif buttonIndex == 4:
                self.state = MenuState.rate
        elif self.state == MenuState.rate_high:
            if buttonIndex == 1:
                self.rate = 120
                self.state = MenuState.feed
            elif buttonIndex == 2:
                self.rate = 130
                self.state = MenuState.feed
            elif buttonIndex == 3:
                self.rate = 140
                self.state = MenuState.feed
            elif buttonIndex == 4:
                self.state = MenuState.rate
        elif self.state == MenuState.volume:
            if buttonIndex == 2:
                self.state = MenuState.volume_bottom
            elif buttonIndex == 3:
                self.state = MenuState.volume_top
            elif buttonIndex == 4:
                self.state = MenuState.feed
        elif self.state == MenuState.volume_bottom:
            if buttonIndex == 1:
                self.volume = 25
                self.state = MenuState.feed
            elif buttonIndex == 2:
                self.volume = 50
                self.state = MenuState.feed
            elif buttonIndex == 3:
                self.volume = 75
                self.state = MenuState.feed
            elif buttonIndex == 4:
                self.state = MenuState.volume
        elif self.state == MenuState.volume_top:
            if buttonIndex == 1:
                self.volume = 100
                self.state = MenuState.feed
            elif buttonIndex == 2:
                self.volume = 125
                self.state = MenuState.feed
            elif buttonIndex == 3:
                self.volume = 150
                self.state = MenuState.feed
            elif buttonIndex == 4:
                self.state = MenuState.volume
        elif self.state == MenuState.transfuse:
            if buttonIndex == 3:
                self.state = MenuState.transfuse_paused
            elif buttonIndex == 4:
                self.state = MenuState.menu_main
        elif self.state == MenuState.transfuse_paused:
            if buttonIndex == 3:
                self.state = MenuState.transfuse
            elif buttonIndex == 4:
                self.state = MenuState.menu_mai
        elif self.state == MenuState.alert_battery:
            if buttonIndex == 4:
                self.state = MenuState.menu_main
        elif self.state == MenuState.alert_tube_disconnect:
            if buttonIndex == 4:
                self.state = MenuState.menu_main
        elif self.state == MenuState.alert_cart_disconnect:
            if buttonIndex == 4:
                self.state = MenuState.menu_main
        elif self.state == MenuState.alert_clog_empty:
            if buttonIndex == 4:
                self.state = MenuState.menu_main


    def handleAnimations(self):
        if self.anim_cartridge:
            if self.anim_cart_direction:
                self.anim_cart_timer += self.anim_cartridge_delta
                if self.anim_cart_timer > max(self.anim_cartridge_interp):
                    self.anim_cartridge = False
            else:
                self.anim_cart_timer -= self.anim_cartridge_delta
                if self.anim_cart_timer < min(self.anim_cartridge_interp):
                    self.anim_cartridge = False

        if self.anim_hose:
            if self.anim_hose_direction:
                self.anim_hose_timer += self.anim_hose_delta
                if self.anim_hose_timer > max(self.anim_hose_interp):
                    self.anim_hose = False
            else:
                self.anim_hose_timer -= self.anim_hose_delta
                if self.anim_hose_timer < min(self.anim_hose_interp):
                    self.anim_hose = False

        if self.anim_transfusion:
            if self.anim_transfusion_state == 0:
                self.anim_transfusion_timer += self.anim_hose_delta
                if self.anim_transfusion_timer > max(self.anim_transfusion_timer_interp):
                    self.anim_transfusion_timer = 0
                    self.anim_transfusion_state = 1

            elif self.anim_transfusion_state == 1:
                self.anim_transfusion_timer += self.anim_hose_delta
                if self.anim_transfusion_timer > max(self.anim_transfusion_timer_interp):
                    self.anim_transfusion_timer = 0
                    self.anim_transfusion_state = 69 #lol
            else:
                self.anim_transfusion_timer += self.anim_hose_delta
                if self.anim_transfusion_timer > max(self.anim_transfusion_timer_interp):
                    self.anim_transfusion_timer = 0
                    self.anim_transfusion_state = 0

    def executeCurrentState(self):
        self.handleAnimations()
        self.Pump.Screen.draw(self.pygameScreen)
        self.Pump.drawCapThreadRelative(self.pygameScreen, self.anim_cart_timer, [0, 7200])
        self.Pump.drawHoseRelative(self.pygameScreen, self.anim_hose_timer, [0, 100])
        self.Pump.drawBody(self.pygameScreen)
        if self.state != MenuState.transfuse:
            self.UI.drawUIPanel(self.pygameScreen, False)
        else:
            self.UI.drawUIPanel(self.pygameScreen, True)
        pos = self.Pump.Screen.position
        offX = 0
        offY = 0
        self.pygameScreen.blit(self.batteryicon, (pos.x + offX, pos.y + offY ))
        if self.UI.checkboxes[Checkboxes["other"]].state:
            pygame.draw.rect(self.pygameScreen, self.theme_primary, pygame.Rect(pos.x + offX + 5, pos.y + offY + 5, 6, 7))

        else:
            pygame.draw.rect(self.pygameScreen, self.theme_secondary, pygame.Rect(pos.x + offX + 5, pos.y + offY + 5, 16, 7))
        if self.state == MenuState.boot:
            pass
        elif self.state == MenuState.locked:
            self.Pump.Screen.takeImageOBJ(self.screen_locked)
        elif self.state == MenuState.unlock:
            self.Pump.Screen.takeImageOBJ(self.screen_unlock)
            # Pin Entry Code:
            font = pygame.font.SysFont("Tahoma", 33)
            img = font.render("  ".join(self.passcode_entered), True, (255, 255, 255))
            pos = self.Pump.Screen.position
            scale = self.Pump.Screen.scale * self.Pump.scale
            offsetx = 105
            offsety = 160
            self.pygameScreen.blit(img, (pos.x + scale * offsetx, pos.y + scale * offsety))
        elif self.state == MenuState.menu_main:
            self.Pump.Screen.takeImageOBJ(self.screen_main_menu)
        elif self.state == MenuState.feed:
            self.Pump.Screen.takeImageOBJ(self.screen_feed)
            font = pygame.font.SysFont("Tahoma", 20)
            img = font.render(str(self.rate), True, (255, 255, 255))
            pos = self.Pump.Screen.position
            scale = self.Pump.Screen.scale * self.Pump.scale
            offsetx = 35
            offsety = 330
            self.pygameScreen.blit(img, (pos.x + scale * offsetx, pos.y + scale * offsety))

            font = pygame.font.SysFont("Tahoma", 20)
            img = font.render(str(self.volume), True, (255, 255, 255))
            pos = self.Pump.Screen.position
            scale = self.Pump.Screen.scale * self.Pump.scale
            offsetx = 35
            offsety = 435
            self.pygameScreen.blit(img, (pos.x + scale * offsetx, pos.y + scale * offsety))
        elif self.state == MenuState.settings:
            self.Pump.Screen.takeImageOBJ(self.screen_settings)

        elif self.state == MenuState.colors:
            self.Pump.Screen.takeImageOBJ(self.screen_color)
            self.swatch.draw(self.pygameScreen, self.Pump.Screen.position.x + 130, self.Pump.Screen.position.y+57)


        elif self.state == MenuState.feed_in_progress:
            self.Pump.Screen.takeImageOBJ(self.screen_palette)
        elif self.state == MenuState.change_pin:
            self.Pump.Screen.takeImageOBJ(self.screen_palette)
        elif self.state == MenuState.rate:
            self.Pump.Screen.takeImageOBJ(self.screen_rate)
        elif self.state == MenuState.rate_low:
            self.Pump.Screen.takeImageOBJ(self.screen_rate_low)
        elif self.state == MenuState.rate_mid:
            self.Pump.Screen.takeImageOBJ(self.screen_rate_mid)
        elif self.state == MenuState.rate_high:
            self.Pump.Screen.takeImageOBJ(self.screen_rate_high)
        elif self.state == MenuState.volume:
            self.Pump.Screen.takeImageOBJ(self.screen_volume)
        elif self.state == MenuState.volume_bottom:
            self.Pump.Screen.takeImageOBJ(self.screen_volume_bottom)
        elif self.state == MenuState.volume_top:
            self.Pump.Screen.takeImageOBJ(self.screen_volume_top)
        elif self.state == MenuState.transfuse:

            if self.UI.checkboxes[Checkboxes["other"]].state:
                self.state = MenuState.alert_battery

            if self.UI.checkboxes[Checkboxes["clog"]].state or self.UI.checkboxes[Checkboxes["feedempty"]].state:
                self.state = MenuState.alert_clog_empty

            if self.UI.checkboxes[Checkboxes["removeoutlet"]].state:
                self.state = MenuState.alert_tube_disconnect

            if self.UI.checkboxes[Checkboxes["removecartridge"]].state:
                self.state = MenuState.alert_cart_disconnect


            pos = self.Pump.Screen.position
            offX = 25
            offY = 100
            w = (255, 255, 255)
            if self.anim_transfusion_state == 0:
                pygame.draw.rect(self.pygameScreen, w, (offX + pos.x + 50, pos.y + offY , 18, 18))
                pygame.draw.rect(self.pygameScreen, w, (offX + pos.x + 75, pos.y + offY, 10, 10))
                pygame.draw.rect(self.pygameScreen, w, (offX + pos.x + 100, pos.y + offY, 10, 10))
            elif self.anim_transfusion_state == 1:
                pygame.draw.rect(self.pygameScreen, w, (offX + pos.x + 50, pos.y + offY, 10, 10))
                pygame.draw.rect(self.pygameScreen, w, (offX + pos.x + 75, pos.y + offY, 18, 18))
                pygame.draw.rect(self.pygameScreen, w, (offX + pos.x + 100, pos.y + offY, 10, 10))
            else:
                pygame.draw.rect(self.pygameScreen, w, (offX + pos.x + 50, pos.y + offY, 10, 10))
                pygame.draw.rect(self.pygameScreen, w, (offX + pos.x + 75, pos.y + offY, 10, 10))
                pygame.draw.rect(self.pygameScreen, w, (offX + pos.x + 100, pos.y + offY, 18, 18))
            self.Pump.Screen.takeImageOBJ(self.screen_transfuse)
        elif self.state == MenuState.transfuse_paused:

            if self.UI.checkboxes[Checkboxes["other"]].state:
                self.state = MenuState.alert_battery

            if self.UI.checkboxes[Checkboxes["clog"]].state or self.UI.checkboxes[Checkboxes["feedempty"]].state:
                self.state = MenuState.alert_clog_empty

            if self.UI.checkboxes[Checkboxes["removeoutlet"]].state:
                self.state = MenuState.alert_tube_disconnect

            if self.UI.checkboxes[Checkboxes["removecartridge"]].state:
                self.state = MenuState.alert_cart_disconnect

            pos = self.Pump.Screen.position
            offX = 25
            offY = 100
            w = (255, 255, 255)
            pygame.draw.rect(self.pygameScreen, w, (offX + pos.x + 50, pos.y + offY, 10, 10))
            pygame.draw.rect(self.pygameScreen, w, (offX + pos.x + 75, pos.y + offY, 10, 10))
            pygame.draw.rect(self.pygameScreen, w, (offX + pos.x + 100, pos.y + offY, 10, 10))
            self.Pump.Screen.takeImageOBJ(self.screen_transfuse_paused)
        elif self.state == MenuState.color_confirm:
            self.Pump.Screen.takeImageOBJ(self.screen_color_confirm)
        elif self.state == MenuState.change_pin_auth:
            self.Pump.Screen.takeImageOBJ(self.screen_pinauth)
            # Pin Entry Code:
            font = pygame.font.SysFont("Tahoma", 33)
            img = font.render("  ".join(self.passcode_entered), True, (255, 255, 255))
            pos = self.Pump.Screen.position
            scale = self.Pump.Screen.scale * self.Pump.scale
            offsetx = 105
            offsety = 160
            self.pygameScreen.blit(img, (pos.x + scale * offsetx, pos.y + scale * offsety))
        elif self.state == MenuState.change_pin_entry:
            self.Pump.Screen.takeImageOBJ(self.screen_pinentry)
            # Pin Entry Code:
            font = pygame.font.SysFont("Tahoma", 33)
            img = font.render("  ".join(self.passcode_change), True, (255, 255, 255))
            pos = self.Pump.Screen.position
            scale = self.Pump.Screen.scale * self.Pump.scale
            offsetx = 105
            offsety = 160
            self.pygameScreen.blit(img, (pos.x + scale * offsetx, pos.y + scale * offsety))
        elif self.state == MenuState.change_pin_verify:
            self.Pump.Screen.takeImageOBJ(self.screen_pinverif)
            # Pin Entry Code:
            font = pygame.font.SysFont("Tahoma", 33)
            img = font.render("  ".join(self.passcode_entered), True, (255, 255, 255))
            pos = self.Pump.Screen.position
            scale = self.Pump.Screen.scale * self.Pump.scale
            offsetx = 105
            offsety = 160
            self.pygameScreen.blit(img, (pos.x + scale * offsetx, pos.y + scale * offsety))
        elif self.state == MenuState.alert_battery:
            self.Pump.Screen.takeImageOBJ(self.screen_alert_battery)
        elif self.state == MenuState.alert_clog_empty:
            self.Pump.Screen.takeImageOBJ(self.screen_alert_cart_empty)
        elif self.state == MenuState.alert_cart_disconnect:
            self.Pump.Screen.takeImageOBJ(self.screen_alert_cart_disc)
            if self.UI.checkboxes[Checkboxes["removecartridge"]].state == False:
                self.state = MenuState.transfuse
        elif self.state == MenuState.alert_tube_disconnect:
            self.Pump.Screen.takeImageOBJ(self.screen_alert_tube_disc)
            if self.UI.checkboxes[Checkboxes["removeoutlet"]].state == False:
                self.state = MenuState.transfuse



