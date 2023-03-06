from common.classes.button import *
from common.functions import *


initial_positions = []
def draw_initial_positions():
    for i in range(20):
        button = Button(None, pos=POSITIONS[i], text_input="X", font=get_font(30), base_color="Black", hovering_color="Red")
        initial_positions.append(button)

    for i in range(20):
        initial_positions[i].changeColor(pygame.mouse.get_pos())
        initial_positions[i].update(SCREEN)
