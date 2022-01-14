import winsound
import pygame

from gpiozero import Button

from global_vars import Global_vars


class Room:
    def __init__(self, width, height, pos, number, key, screen):
        self.width = width
        self.height = height
        self.pos = pos
        self.number = number
        self.key = key
        self.screen = screen

        self.color = (0, 255, 0)
        self.state = 0

        self.calling = False
        self.font_size = 32

    def draw(self):
        # Draw the container
        container = pygame.Rect((self.pos), (self.width, self.height))
        pygame.draw.rect(self.screen, self.color, container)
        pygame.draw.rect(self.screen, (0, 0, 0), container, 2)

        # Draw the room number
        font = pygame.font.SysFont('arial', self.font_size)
        label = font.render(f'Room Number: {self.number}', 1, (0,0,0))
        x = self.pos[0] + (self.width / 2 - label.get_width() / 2)
        self.screen.blit(label, (x, self.pos[1] + 20))

        # If active change color to red
        if self.state == 1:
            self.color = (255, 0, 0)
        elif self.state == 2:
            self.color = (255, 255, 0)
        else:
            self.color = (0, 255, 0)

        # Check for click
        self.check_for_click()

    def check_for_click(self):
        if Global_vars.IS_KEYDOWN:
            if Global_vars.KEYDOWN_UNICODE == self.key:
                if self.state == 0:
                    Global_vars.RING_SOUND.play()
                    self.state += 1
                elif self.state == 1:
                    Global_vars.RING_SOUND.play()
                    self.state = 2
                else:
                    self.state = 0
            if Global_vars.KEYDOWN_UNICODE.isnumeric():
                if int(Global_vars.KEYDOWN_UNICODE) == self.number:
                    self.state = 0
                    print('clicked')
                