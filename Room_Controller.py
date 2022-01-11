from Room import Room
import math
from global_vars import Global_vars

class Room_Controller:
    def __init__(self):
        keys = [5, 6, 13, 16, 19, 26]
        self.height_percentage = 0.85
        self.height = Global_vars.HEIGHT * self.height_percentage
        self.start_y = (1 - self.height_percentage) * Global_vars.HEIGHT
        self.rooms = []
        self.cols = 3
        self.rows = 2
        self.get_rooms(keys)

    def get_rooms(self, keys):
        for i, key in enumerate(keys):
            room_width = Global_vars.WIDTH / self.cols
            room_height = self.height / self.rows
            x = (i % self.cols) * room_width
            y = self.start_y + math.floor(i / self.cols) * room_height
            room = Room(room_width, room_height, (x, y),  i + 1, key, Global_vars.WINDOW)
            self.rooms.append(room)

    def draw(self):
        for room in self.rooms:
            room.draw()