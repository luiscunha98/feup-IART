from elements.game.modes.pvp.initial_positions import *
import sys
from common.classes.piece import *

def movements(event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(20):
                if initial_positions[i].checkForInput(pygame.mouse.get_pos()):
                    piece.draw_piece(POSITIONS[i], "White")