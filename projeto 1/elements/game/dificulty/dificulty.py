from common.functions import *
from common.classes.button import *
import sys

from elements.game.game_over.game_over import game_over

global start_bpositions
global start_wpositions
global player_turn
global gameover


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
    aux_pos = {}
    selected = None
    click = False
    n_play = 1
    player_turn = 1  # Player 1 goes first
    black_pieces = []
    white_pieces = []
    while True:
        SCREEN.blit(BG, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        BOARD = pygame.image.load("resources/images/Board.png")
        SCREEN.blit(BOARD, (340, 100))
        PLAY_TEXT = get_font(35).render("PLAYER VS PLAYER", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 50))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        start_bpositions = {0, 2, 7, 18, 19}
        start_wpositions = {8, 9, 11, 12, 13}

        if (len(black_pieces) != 4):
            for i in start_bpositions:
                pygame.draw.circle(SCREEN, BLUE, (POSITIONS[i].get_position()), PIECE_RADIUS)

        if (player_turn == 2 and len(white_pieces) != 4):
            for i in start_wpositions:
                pygame.draw.circle(SCREEN, BLUE, (POSITIONS[i].get_position()), PIECE_RADIUS)

        # Draw the pieces on the board
        for piece in black_pieces + white_pieces:
            pygame.draw.circle(SCREEN, piece['color'], piece['position'], PIECE_RADIUS)

        if selected != None:
            pygame.draw.circle(SCREEN, "Red", selected.get_position(), PIECE_RADIUS)
            if (selected.poss1.busy == False):
                pygame.draw.circle(SCREEN, BLUE, selected.poss1.get_position(), PIECE_RADIUS)
            if (selected.poss2.busy == False):
                pygame.draw.circle(SCREEN, BLUE, selected.poss2.get_position(), PIECE_RADIUS)
            if (selected.poss3.busy == False):
                pygame.draw.circle(SCREEN, BLUE, selected.poss3.get_position(), PIECE_RADIUS)

        PLAY_BACK = Button(image=None, pos=(175, 625),
                           text_input="QUIT GAME", font=get_font(35), base_color="White", hovering_color="Red")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if n_play < 9:  # Players put all of their pieces in the board first
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        main_menu()
                    else:
                        # Check if the click is within one of the positions
                        for i in start_bpositions:
                            if distance(POSITIONS[i], PLAY_MOUSE_POS) < PIECE_RADIUS:
                                # Check if the position is already occupied
                                if not any(piece['position'] == POSITIONS[i].get_position() for piece in
                                           black_pieces + white_pieces):
                                    # Add the piece to the list
                                    if player_turn == 1 and len(black_pieces) < 4:
                                        color = BLACK
                                        black_pieces.append({'position': POSITIONS[i].get_position(), 'color': color})
                                        POSITIONS[i].set_busy(True)
                                        if len(black_pieces) == 4:
                                            player_turn = 2
                                        n_play += 1
                        for i in start_wpositions:
                            if distance(POSITIONS[i], PLAY_MOUSE_POS) < PIECE_RADIUS:
                                # Check if the position is already occupied
                                if not any(piece['position'] == POSITIONS[i].get_position() for piece in
                                           black_pieces + white_pieces):
                                    # Add the piece to the list
                                    if player_turn == 2 and len(white_pieces) < 4:
                                        color = WHITE
                                        white_pieces.append({'position': POSITIONS[i].get_position(), 'color': color})
                                        POSITIONS[i].set_busy(True)
                                        if len(white_pieces) == 4:
                                            player_turn = 1
                                        n_play += 1

            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        main_menu()
                    else:
                        # Check if the click is within one of the positions
                        for i in range(20):
                            if distance(POSITIONS[i], PLAY_MOUSE_POS) < PIECE_RADIUS:
                                if click:
                                    if player_turn == 1:
                                        color = BLACK
                                        if (selected == POSITIONS[i].poss1 and POSITIONS[i].busy == False) or (
                                                selected == POSITIONS[i].poss2 and POSITIONS[i].busy == False) or (
                                                selected == POSITIONS[i].poss3 and POSITIONS[i].busy == False):
                                            black_pieces.remove({'position': aux_pos.get_position(), 'color': color})
                                            aux_pos.set_busy(False)
                                            black_pieces.append(
                                                {'position': POSITIONS[i].get_position(), 'color': color})
                                            POSITIONS[i].set_busy(True)
                                            player_turn = 2
                                        selected = None
                                    else:
                                        color = WHITE
                                        if (selected == POSITIONS[i].poss1 and POSITIONS[i].busy == False) or (
                                                selected == POSITIONS[i].poss2 and POSITIONS[i].busy == False) or (
                                                selected == POSITIONS[i].poss3 and POSITIONS[i].busy == False):
                                            white_pieces.remove({'position': aux_pos.get_position(), 'color': color})
                                            aux_pos.set_busy(False)
                                            white_pieces.append(
                                                {'position': POSITIONS[i].get_position(), 'color': color})
                                            POSITIONS[i].set_busy(True)
                                            player_turn = 1
                                        selected = None
                                    click = False
                                if player_turn == 1:
                                    if any(piece['position'] == POSITIONS[i].get_position() for piece in black_pieces):
                                        selected = POSITIONS[i]
                                        aux_pos = POSITIONS[i]
                                        click = True
                                else:
                                    if any(piece['position'] == POSITIONS[i].get_position() for piece in white_pieces):
                                        selected = POSITIONS[i]
                                        aux_pos = POSITIONS[i]
                                        click = True
        for position in POSITIONS:
            if verify(position) == 1:
                game_over(player_turn)
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