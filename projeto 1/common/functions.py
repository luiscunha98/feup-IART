from common.variables import *

def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("resources/assets/font.ttf", size)

def render_multi_line(text, x, y, fsize):
    lines = text.splitlines()
    for i, l in enumerate(lines):
        SCREEN.blit(get_font(20).render(l, 0, "White"), (x, y + fsize * 2 * i))