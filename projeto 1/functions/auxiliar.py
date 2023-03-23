from variables.interface import *
from variables.constants import *
from variables.positions import *

def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("resources/assets/font.ttf", size)


def render_multi_line(text, x, y, fsize):
    lines = text.splitlines()
    for i, l in enumerate(lines):
        SCREEN.blit(get_font(20).render(l, 0, "White"), (x, y + fsize * 2 * i))


def distance(point1, point2):
    x1, y1 = point1.x, point1.y
    x2, y2 = point2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5