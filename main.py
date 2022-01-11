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

    main_scene.render()
    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()