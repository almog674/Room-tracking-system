import pygame
from main_scene import Main_scene
from global_vars import Global_vars

pygame.init()



# Set up the drawing window
main_scene = Main_scene(Global_vars.WINDOW)

# Run until the user asks to quit
running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            Global_vars.IS_KEYDOWN = True
            Global_vars.KEYDOWN_UNICODE = event.unicode

    main_scene.render()

    # Flip the display
    pygame.display.flip()

    Global_vars.CLOCK.tick(60)
    Global_vars.IS_KEYDOWN = False
    Global_vars.KEYDOWN_UNICODE = ''

# Done! Time to quit.
pygame.quit()