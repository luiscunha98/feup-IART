from game.elements.dificulty.pvp import *
from game.elements.dificulty.pvc import *
from game.elements.dificulty.cvc import *


def difficulty(main_menu, play, mode):
    while True:
        if mode == PVP:
            pvp(main_menu)
        else:
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

            #button hover changes
            EASY.changeColor(PLAY_MOUSE_POS)
            MEDIUM.changeColor(PLAY_MOUSE_POS)
            HARD.changeColor(PLAY_MOUSE_POS)
            PLAY_BACK.changeColor(PLAY_MOUSE_POS)

            #button update
            EASY.update(SCREEN)
            MEDIUM.update(SCREEN)
            HARD.update(SCREEN)
            PLAY_BACK.update(SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if EASY.checkForInput(PLAY_MOUSE_POS):
                        if mode == PVC:
                            pvc(main_menu, E)
                        else:
                            cvc(main_menu, E)
                    if MEDIUM.checkForInput(PLAY_MOUSE_POS):
                        if mode == PVC:
                            pvc(main_menu, M)
                        else:
                            cvc(main_menu, M)
                    if HARD.checkForInput(PLAY_MOUSE_POS):
                        if mode == PVC:
                            pvc(main_menu, H)
                        else:
                            cvc(main_menu, H)
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        play(main_menu)
            pygame.display.update()