from elements.game.main_menu.options.instructions import *
from elements.game.main_menu.options.play import *


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(125).render("BOUND GAME", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(None, pos=(640, 375),
                             text_input="PLAY", font=get_font(100), base_color="White", hovering_color="Red")
        INSTRUCTIONS_BUTTON = Button(None, pos=(640, 500),
                                     text_input="INSTRUCTIONS", font=get_font(30), base_color="White",
                                     hovering_color="Red")
        QUIT_BUTTON = Button(None, pos=(640, 600),
                             text_input="QUIT GAME", font=get_font(30), base_color="White", hovering_color="Red")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, INSTRUCTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play(main_menu)
                if INSTRUCTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    instructions(main_menu)
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
