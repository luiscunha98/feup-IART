import sys
from common.classes.piece import *
from elements.game.modes.pvp.movements import *

pieces = piece()


def difficulty(main_menu, play, mode):
    while True:
        SCREEN.blit(BG, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        PLAY_TEXT = get_font(45).render("Difficulty:", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(300, 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        EASY = Button(image=None, pos=(300, 250),
                      text_input="EASY", font=get_font(35), base_color="White", hovering_color="Red")
        EASY.changeColor(PLAY_MOUSE_POS)
        EASY.update(SCREEN)

        MEDIUM = Button(image=None, pos=(335, 350),
                        text_input="MEDIUM", font=get_font(35), base_color="White", hovering_color="Red")
        MEDIUM.changeColor(PLAY_MOUSE_POS)
        MEDIUM.update(SCREEN)

        HARD = Button(image=None, pos=(300, 450),
                      text_input="HARD", font=get_font(35), base_color="White", hovering_color="Red")
        HARD.changeColor(PLAY_MOUSE_POS)
        HARD.update(SCREEN)

        PLAY_BACK = Button(image=None, pos=(640, 600),
                           text_input="BACK", font=get_font(50), base_color="White", hovering_color="Red")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
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
                    play()

        pygame.display.update()


def pvp(main_menu):
    while True:
        SCREEN.blit(BG, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        BOARD = pygame.image.load("resources/images/Board.png")
        SCREEN.blit(BOARD, (340, 100))
        draw_initial_positions()
        PLAY_TEXT = get_font(35).render("PLAYER VS PLAYER", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 50))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(175, 625),
                           text_input="QUIT GAME", font=get_font(35), base_color="White", hovering_color="Red")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            movements(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def pvc(main_menu, dif):
    while True:
        SCREEN.blit(BG, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        BOARD = pygame.image.load("resources/images/Board.png")
        SCREEN.blit(BOARD, (340, 100))
        PLAY_TEXT = get_font(45).render("PLAYER VS CPU", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 50))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(175, 625),
                           text_input="QUIT GAME", font=get_font(35), base_color="White", hovering_color="Red")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def cvc(main_menu, dif):
    while True:
        SCREEN.blit(BG, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        BOARD = pygame.image.load("resources/images/Board.png")
        SCREEN.blit(BOARD, (340, 100))
        PLAY_TEXT = get_font(45).render("CPU VS CPU", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 50))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(175, 625),
                           text_input="QUIT GAME", font=get_font(35), base_color="White", hovering_color="Red")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()
