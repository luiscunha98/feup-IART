from common.functions import *
from common.classes.button import *
import sys

def instructions(main_menu):
    while True:
        SCREEN.blit(BG, (0, 0))
        INSTRUCTIONS_MOUSE_POS = pygame.mouse.get_pos()

        text = "Both players need four pieces to play. The older player\nplaces their four pieces on four of the five forks around\nthe outer ring. The younger player places their four pieces\non the central pentagon, each one on a fork opposite one of\nthe older player’s pieces. The older player takes the first\nturn. Thereafter players alternate. On your turn, move one of\nyour four pieces along a single edge to an empty adjacent\nfork. You must move a piece. A piece is bound if is\nsurrounded on all three sides, by any combination of\nplayers’ pieces. If, at any time, one of your opponent’s\npieces is bound, you have won the game."

        render_multi_line(text, 50, 100, 20)

        INSTRUCTIONS_BACK = Button(image=None, pos=(640, 650),
                                   text_input="BACK", font=get_font(30), base_color="White", hovering_color="Red")

        INSTRUCTIONS_BACK.changeColor(INSTRUCTIONS_MOUSE_POS)
        INSTRUCTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if INSTRUCTIONS_BACK.checkForInput(INSTRUCTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()