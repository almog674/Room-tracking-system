import pygame
from global_vars import Global_vars
from Room_Controller import Room_Controller

class Main_scene():
    def __init__(self, screen):
        self.screen = screen

        self.title_section_height = 0.15
        self.title_section_width = 1

        self.font_size = 52
        self.room_controller = Room_Controller()

    def render(self):
        # Draw the top part
        self.draw_title_section()

        # Draw the rooms
        self.room_controller.draw()

    def draw_title_section(self):
        # 1) Draw the rect
        title_section_rect = pygame.Rect(0,0, Global_vars.WIDTH * self.title_section_width, Global_vars.HEIGHT * self.title_section_height)
        pygame.draw.rect(self.screen, (255,255, 255), title_section_rect)

        # 2) Draw the text
        font = pygame.font.SysFont('arial', self.font_size)
        title = font.render('Test Program',1, (0,0,0))
        title_rect = title.get_rect()
        title_rect.center = title_section_rect.center

        self.screen.blit(title, title_rect)
