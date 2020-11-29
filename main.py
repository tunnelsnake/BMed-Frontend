from pumpbody import Pump as Body
from button import *
from ui import UI as ui

pygame.init()
Pump = Body(600, 200, .35)
UI = ui(150, 900, scale=.25)



# Set up the drawing window
#screen = pygame.display.set_mode([800, 600])
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


# Set up state handler
state = [False, False, False, False, False, False]

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
            for btn in Pump.Buttons:
                if btn.isClicked():
                    print("Button Pressed")

            for ckbox in UI.checkboxes:
                if ckbox.isClicked():
                    print("Checkbox was clicked")
                    ckbox.state = not ckbox.state

                    # TODO Handlers for each checkbox
                        # TODO Remove Cartridge with state change
                        # ---> Start an animation counter
                        # TODO Remove Tube Connect with state change
                        # ---> Start another anim counter
                        # TODO state change for Food Empty
                        # ---> Register a ui event
                        # TODO state change for Child Lock
                        # ---> Register a ui event
                        # TODO state change for Clog
                        # ---> Register a ui event



    # Fill the background with white
    # A6EBF7
    graybg = (0xA6, 0xEB, 0xF7)
    screen.fill(graybg)

    Pump.Screen.draw(screen)
    Pump.drawCapThreadRelative(screen, 0)
    Pump.drawBody(screen)

    UI.drawUIPanel(screen)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()


