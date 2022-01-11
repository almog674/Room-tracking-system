import pygame


class Global_vars:
    WIDTH  = 1000
    HEIGHT = 800
    WINDOW = pygame.display.set_mode([WIDTH, HEIGHT])

    CLOCK = pygame.time.Clock()

    IS_KEYDOWN = False
    KEYDOWN_UNICODE = ''

    MIXER = pygame.mixer
    MIXER.init()
    RING_SOUND = MIXER.Sound("bell_ring.wav")