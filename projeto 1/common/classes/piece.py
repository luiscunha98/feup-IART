from common.variables import *

class piece():
    def draw_piece(position, color):
            pygame.draw.circle(SCREEN, color, position, 20)

    def move_piece(self, x, y):
        self.x = x
        self.y = y