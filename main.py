from pumpbody import Pump as Body
from button import *
from ui import UI as ui

pygame.init()
Pump = Body(375, 125, .27)
UI = ui()

ANIM_CTR = 1
ROT_CTR = 0
INCREASE = True

# Set up the drawing window
#screen = pygame.display.set_mode([800, 600])
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

# Run until the user asks to quit
running = True
while running:

    if ROT_CTR == 3600:
        ROT_CTR = 0
    else:
        ROT_CTR += 1


    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_q]:
                running = False


        if event.type == pygame.MOUSEBUTTONDOWN:
            for btn in Pump.Buttons:
                if isButtonPressed(btn):
                    print("Button Pressed")

    # Fill the background with white
    # A6EBF7
    graybg = (0xA6, 0xEB, 0xF7)
    screen.fill(graybg)

    Pump.Screen.draw(screen)
    Pump.drawCapThreadRelative(screen, 0)
    Pump.drawBody(screen)

    UI.drawRotateAssembly(screen, 1000, 400, .1, ROT_CTR)
    UI.drawUIPanel(screen, 85, 540, .23)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()


