from pumpbody import Pump as Body
from menuFSM import MenuFSM
from button import *
from ui import UI as ui

pygame.init()
Pump = Body(600, 200, .35)
UI = ui(150, 900, scale=.25)


# Set up the drawing window
#screen = pygame.display.set_mode([800, 600])
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


MenuHandler = MenuFSM(Pump, UI, screen)


# Run until the user asks to quit
running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_q]:
                running = False


        if event.type == pygame.MOUSEBUTTONDOWN:
            for index, btn in enumerate(Pump.Buttons):
                if btn.isClicked():
                    print("Button Pressed")
                    MenuHandler.buttonCallback(index)


            for index, ckbox in enumerate(UI.checkboxes):
                if ckbox.isClicked():
                    print("Checkbox was clicked")
                    ckbox.state = not ckbox.state
                    MenuHandler.checkboxCallback(index, ckbox.state)







    # Fill the background with white
    # A6EBF7
    graybg = (0xA6, 0xEB, 0xF7)
    screen.fill(graybg)

    MenuHandler.executeCurrentState()



    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()


