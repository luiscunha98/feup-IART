from game.elements.dificulty.pvp import *
from game.elements.dificulty.pvc import *
from game.elements.dificulty.cvc import *


def difficulty(main_menu, play, mode):

    # select mode
    while True:

        #case PVP
        if mode == PVP:
            pvp(main_menu)

        else:

            #base
            SCREEN.blit(BG, (0, 0))
            PLAY_MOUSE_POS = pygame.mouse.get_pos()
            PLAY_TEXT = get_font(45).render("Difficulty:", True, "White")
            PLAY_RECT = PLAY_TEXT.get_rect(center=(300, 100))
            SCREEN.blit(PLAY_TEXT, PLAY_RECT)


            #button definition
            EASY = Button(image=None, pos=(300, 250), text_input="EASY", font=get_font(35), base_color="White", hovering_color="Red")
            MEDIUM = Button(image=None, pos=(335, 350), text_input="MEDIUM", font=get_font(35), base_color="White", hovering_color="Red")
            HARD = Button(image=None, pos=(300, 450), text_input="HARD", font=get_font(35), base_color="White", hovering_color="Red")
            PLAY_BACK = Button(image=None, pos=(640, 600), text_input="BACK", font=get_font(50), base_color="White", hovering_color="Red")

            #button hover changes and update
            for button in [EASY, MEDIUM, HARD, PLAY_BACK]:
                button.changeColor(PLAY_MOUSE_POS)
                button.update(SCREEN)

            for event in pygame.event.get():
                quit_game(event)

                # case PVC or CVC choose difficulty
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if EASY.checkForInput(PLAY_MOUSE_POS):
                        pvc(main_menu, E)
                    if MEDIUM.checkForInput(PLAY_MOUSE_POS):
                        pvc(main_menu, M)
                    if HARD.checkForInput(PLAY_MOUSE_POS):
                        pvc(main_menu, H)
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        play(main_menu)

            pygame.display.update()


def difficulty1(main_menu, play):
    while True:
        SCREEN.blit(BG, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_TEXT = get_font(45).render("CPU-1 Difficulty:", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(400, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)


        #button definition
        EASY = Button(image=None, pos=(300, 250), text_input="EASY", font=get_font(35), base_color="White", hovering_color="Red")
        MEDIUM = Button(image=None, pos=(335, 350), text_input="MEDIUM", font=get_font(35), base_color="White", hovering_color="Red")
        HARD = Button(image=None, pos=(300, 450), text_input="HARD", font=get_font(35), base_color="White", hovering_color="Red")
        PLAY_BACK = Button(image=None, pos=(640, 600), text_input="BACK", font=get_font(50), base_color="White", hovering_color="Red")

        #button hover changes and update
        for button in [EASY, MEDIUM, HARD, PLAY_BACK]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            quit_game(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if EASY.checkForInput(PLAY_MOUSE_POS):
                    return E
                if MEDIUM.checkForInput(PLAY_MOUSE_POS):
                    return M
                if HARD.checkForInput(PLAY_MOUSE_POS):
                    return H
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    play(main_menu)

        pygame.display.update()

def difficulty2(main_menu, play, dif1):
    while True:
        SCREEN.blit(BG, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_TEXT = get_font(45).render("CPU-2 Difficulty:", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(400, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)


        #button definition
        EASY = Button(image=None, pos=(300, 250), text_input="EASY", font=get_font(35), base_color="White", hovering_color="Red")
        MEDIUM = Button(image=None, pos=(335, 350), text_input="MEDIUM", font=get_font(35), base_color="White", hovering_color="Red")
        HARD = Button(image=None, pos=(300, 450), text_input="HARD", font=get_font(35), base_color="White", hovering_color="Red")
        PLAY_BACK = Button(image=None, pos=(640, 600), text_input="BACK", font=get_font(50), base_color="White", hovering_color="Red")

        #button hover changes and update
        for button in [EASY, MEDIUM, HARD, PLAY_BACK]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            quit_game(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if EASY.checkForInput(PLAY_MOUSE_POS):
                    cvc(main_menu, dif1, E)
                if MEDIUM.checkForInput(PLAY_MOUSE_POS):
                    cvc(main_menu, dif1, M)
                if HARD.checkForInput(PLAY_MOUSE_POS):
                    cvc(main_menu, dif1, H)
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    play(main_menu)

        pygame.display.update()