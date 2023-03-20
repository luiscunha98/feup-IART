import sys
import random

from common.classes.button import *
from common.functions import *

global start_bpositions
global start_wpositions
global player_turn


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
    p1wins = 0
    p2wins = 0
    while True:
        SCREEN.blit(BG, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        BOARD = pygame.image.load("resources/images/Board.png")
        SCREEN.blit(BOARD, (340, 100))
        PLAY_TEXT = get_font(35).render("PLAYER VS PLAYER", True, "White")
        SCORE_TEXT = get_font(25).render("SCORE", True, "White")
        PLAYER1_TEXT = get_font(20).render("PLAYER 1: " + str(p1wins), True, "White")
        PLAYER2_TEXT = get_font(20).render("PLAYER 2: " + str(p2wins), True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 50))
        SCORE_RECT = PLAY_TEXT.get_rect(center=(400, 150))
        PLAYER1_RECT = PLAY_TEXT.get_rect(center=(350, 200))
        PLAYER2_RECT = PLAY_TEXT.get_rect(center=(350, 250))

        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        SCREEN.blit(SCORE_TEXT, SCORE_RECT)
        SCREEN.blit(PLAYER1_TEXT, PLAYER1_RECT)
        SCREEN.blit(PLAYER2_TEXT, PLAYER2_RECT)
        start_bpositions = {0, 2, 7, 18, 19}
        start_wpositions = {8, 9, 11, 12, 13}
        if (len(black_pieces) != 4):
            for i in start_bpositions:
                pygame.draw.circle(SCREEN, BLUE, (POSITIONS[i].get_position()), PIECE_RADIUS)

        if player_turn == 2 and len(white_pieces) != 4:
            for i in start_wpositions:
                pygame.draw.circle(SCREEN, BLUE, (POSITIONS[i].get_position()), PIECE_RADIUS)

        # Draw the pieces on the board
        for piece in black_pieces + white_pieces:
            pygame.draw.circle(SCREEN, piece['color'], piece['position'], PIECE_RADIUS)

        if selected is not None:
            pygame.draw.circle(SCREEN, "Red", selected.get_position(), PIECE_RADIUS)
            if selected.poss1.busy is False:
                pygame.draw.circle(SCREEN, BLUE, selected.poss1.get_position(), PIECE_RADIUS)
            if selected.poss2.busy is False:
                pygame.draw.circle(SCREEN, BLUE, selected.poss2.get_position(), PIECE_RADIUS)
            if selected.poss3.busy is False:
                pygame.draw.circle(SCREEN, BLUE, selected.poss3.get_position(), PIECE_RADIUS)

        PLAY_BACK = Button(image=None, pos=(175, 625),
                           text_input="QUIT GAME", font=get_font(35), base_color="White", hovering_color="Red")

        RETURN = Button(image=None, pos=(175, 570),
                        text_input="BACK", font=get_font(35), base_color="White", hovering_color="Red")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)
        RETURN.changeColor(PLAY_MOUSE_POS)
        RETURN.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if n_play < 9:  # Players put all of their pieces in the board first
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        main_menu()
                    elif RETURN.checkForInput(PLAY_MOUSE_POS):
                        return False
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
                                        black_pieces.append(
                                            {'position': POSITIONS[i].get_position(), 'color': color})
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
                                        white_pieces.append(
                                            {'position': POSITIONS[i].get_position(), 'color': color})
                                        POSITIONS[i].set_busy(True)
                                        if len(white_pieces) == 4:
                                            player_turn = 1
                                        n_play += 1

            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        main_menu()
                    elif RETURN.checkForInput(PLAY_MOUSE_POS):
                        return False
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
                                            black_pieces.remove(
                                                {'position': aux_pos.get_position(), 'color': color})
                                            aux_pos.set_busy(False)
                                            black_pieces.append(
                                                {'position': POSITIONS[i].get_position(), 'color': color})
                                            POSITIONS[i].set_busy(True)
                                            player_turn = 2
                                        selected = None
                                    elif player_turn == 2:
                                        color = WHITE
                                        if (selected == POSITIONS[i].poss1 and POSITIONS[i].busy == False) or (
                                                selected == POSITIONS[i].poss2 and POSITIONS[i].busy == False) or (
                                                selected == POSITIONS[i].poss3 and POSITIONS[i].busy == False):
                                            white_pieces.remove(
                                                {'position': aux_pos.get_position(), 'color': color})
                                            aux_pos.set_busy(False)
                                            white_pieces.append(
                                                {'position': POSITIONS[i].get_position(), 'color': color})
                                            POSITIONS[i].set_busy(True)
                                            player_turn = 1
                                        selected = None
                                    click = False
                                if player_turn == 1:
                                    if any(piece['position'] == POSITIONS[i].get_position() for piece in
                                           black_pieces):
                                        selected = POSITIONS[i]
                                        aux_pos = POSITIONS[i]
                                        click = True
                                elif player_turn == 2:
                                    if any(piece['position'] == POSITIONS[i].get_position() for piece in
                                           white_pieces):
                                        selected = POSITIONS[i]
                                        aux_pos = POSITIONS[i]
                                        click = True
        for position in POSITIONS:
            if verify(position) == 1:
                #game_over(player_turn)
                aux = {'position': position.get_position(), 'color': BLACK}
                aux2 = {'position': position.get_position(), 'color': WHITE}
                if player_turn == 1 and aux2 in white_pieces:
                    p1wins += 1
                elif player_turn == 1 and aux in black_pieces:
                    p2wins += 1
                elif player_turn == 2 and aux2 in white_pieces:
                    p1wins += 1
                elif player_turn == 2 and aux in black_pieces:
                    p2wins += 1
                n_play = 1
                player_turn = 1  # Player 1 goes first
                black_pieces = []
                white_pieces = []
                aux_pos = {}
                selected = None
                click = False
                for pos in POSITIONS:
                    pos.set_busy(False)
        pygame.display.update()


def pvc(main_menu, dif):
    if dif == 1:
        aux_pos = {}
        selected = None
        click = False
        n_play = 1
        player_turn = 1  # Player 1 goes first
        black_pieces = []
        white_pieces = []
        p1wins = 0
        p2wins = 0
        while True:
            SCREEN.blit(BG, (0, 0))
            PLAY_MOUSE_POS = pygame.mouse.get_pos()
            BOARD = pygame.image.load("resources/images/Board.png")
            SCREEN.blit(BOARD, (340, 100))
            PLAY_TEXT = get_font(35).render("PLAYER VS PLAYER", True, "White")
            SCORE_TEXT = get_font(25).render("SCORE", True, "White")
            PLAYER1_TEXT = get_font(20).render("PLAYER 1: " + str(p1wins), True, "White")
            PLAYER2_TEXT = get_font(20).render("PLAYER 2: " + str(p2wins), True, "White")
            PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 50))
            SCORE_RECT = PLAY_TEXT.get_rect(center=(400, 150))
            PLAYER1_RECT = PLAY_TEXT.get_rect(center=(350, 200))
            PLAYER2_RECT = PLAY_TEXT.get_rect(center=(350, 250))

            SCREEN.blit(PLAY_TEXT, PLAY_RECT)
            SCREEN.blit(SCORE_TEXT, SCORE_RECT)
            SCREEN.blit(PLAYER1_TEXT, PLAYER1_RECT)
            SCREEN.blit(PLAYER2_TEXT, PLAYER2_RECT)
            start_bpositions = {0, 2, 7, 18, 19}
            start_wpositions = {8, 9, 11, 12, 13}
            if (len(black_pieces) != 4):
                for i in start_bpositions:
                    pygame.draw.circle(SCREEN, BLUE, (POSITIONS[i].get_position()), PIECE_RADIUS)

            # Draw the pieces on the board
            for piece in black_pieces + white_pieces:
                pygame.draw.circle(SCREEN, piece['color'], piece['position'], PIECE_RADIUS)

            if selected is not None:
                pygame.draw.circle(SCREEN, "Red", selected.get_position(), PIECE_RADIUS)
                if selected.poss1.busy is False:
                    pygame.draw.circle(SCREEN, BLUE, selected.poss1.get_position(), PIECE_RADIUS)
                if selected.poss2.busy is False:
                    pygame.draw.circle(SCREEN, BLUE, selected.poss2.get_position(), PIECE_RADIUS)
                if selected.poss3.busy is False:
                    pygame.draw.circle(SCREEN, BLUE, selected.poss3.get_position(), PIECE_RADIUS)

            PLAY_BACK = Button(image=None, pos=(175, 625),
                            text_input="QUIT GAME", font=get_font(35), base_color="White", hovering_color="Red")

            RETURN = Button(image=None, pos=(175, 570),
                            text_input="BACK", font=get_font(35), base_color="White", hovering_color="Red")

            PLAY_BACK.changeColor(PLAY_MOUSE_POS)
            PLAY_BACK.update(SCREEN)
            RETURN.changeColor(PLAY_MOUSE_POS)
            RETURN.update(SCREEN)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if n_play < 9:  # Players put all of their pieces in the board first
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                            main_menu()
                        elif RETURN.checkForInput(PLAY_MOUSE_POS):
                            return False
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
                                            black_pieces.append(
                                                {'position': POSITIONS[i].get_position(), 'color': color})
                                            POSITIONS[i].set_busy(True)
                                            if len(black_pieces) == 4:
                                                player_turn = 2
                                            n_play += 1
                            if n_play >= 5:
                                for i in start_wpositions:
                                    if distance(POSITIONS[i], PLAY_MOUSE_POS) < 2000:
                                        # Check if the position is already occupied
                                        if not any(piece['position'] == POSITIONS[i].get_position() for piece in
                                                black_pieces + white_pieces):
                                            # Add the piece to the list
                                            while (player_turn == 2 and len(white_pieces) < 4):
                                                # place a white piece randomly
                                                index = random.randint(8,13)
                                                if index in {8,9,11,12,13}:
                                                    if not POSITIONS[index].busy:
                                                        white_pieces.append({'position': POSITIONS[index].get_position(), 'color': WHITE})
                                                        POSITIONS[index].set_busy(True)
                                            player_turn = 1
                                            n_play += 4

                else:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                            main_menu()
                        elif RETURN.checkForInput(PLAY_MOUSE_POS):
                            return False
                        else:
                            # Check if the click is within one of the positions
                            for i in range(20):
                                if distance(POSITIONS[i], PLAY_MOUSE_POS) < PIECE_RADIUS:
                                    if player_turn==1 and click:
                                        color = BLACK
                                        if (selected == POSITIONS[i].poss1 and POSITIONS[i].busy == False) or (
                                                selected == POSITIONS[i].poss2 and POSITIONS[i].busy == False) or (
                                                selected == POSITIONS[i].poss3 and POSITIONS[i].busy == False):
                                            black_pieces.remove(
                                                {'position': aux_pos.get_position(), 'color': color})
                                            aux_pos.set_busy(False)
                                            black_pieces.append(
                                                {'position': POSITIONS[i].get_position(), 'color': color})
                                            POSITIONS[i].set_busy(True)
                                            player_turn = 2
                                        selected = None
                                    elif player_turn == 2:
                                        # Randomly select a piece for player 2
                                        selected_piece = random.choice(white_pieces)
                                        white_pieces.remove(selected_piece)
                                        for i in range(len(POSITIONS)):
                                            if POSITIONS[i].get_position() == selected_piece['position']:
                                                if distance(POSITIONS[i], PLAY_MOUSE_POS) < PIECE_RADIUS:
                                                    if not POSITIONS[i].busy:
                                                        color = WHITE
                                                        selected_piece['position'] = POSITIONS[i].get_position()
                                                        white_pieces.append(selected_piece)
                                                        POSITIONS[i].set_busy(True)
                                        for piece in white_pieces:
                                            pygame.draw.circle(SCREEN, piece['color'], piece['position'], PIECE_RADIUS)
                                        player_turn = 1
                                    if player_turn == 1:
                                        if any(piece['position'] == POSITIONS[i].get_position() for piece in
                                            black_pieces):
                                            selected = POSITIONS[i]
                                            aux_pos = POSITIONS[i]
                                            click = True
                                    elif player_turn == 2:
                                        if any(piece['position'] == POSITIONS[i].get_position() for piece in
                                            white_pieces):
                                            selected = POSITIONS[i]
                                            aux_pos = POSITIONS[i]
                                            click = True
            for position in POSITIONS:
                if verify(position) == 1:
                    #game_over(player_turn)
                    aux = {'position': position.get_position(), 'color': BLACK}
                    aux2 = {'position': position.get_position(), 'color': WHITE}
                    if player_turn == 1 and aux2 in white_pieces:
                        p1wins += 1
                    elif player_turn == 1 and aux in black_pieces:
                        p2wins += 1
                    elif player_turn == 2 and aux2 in white_pieces:
                        p1wins += 1
                    elif player_turn == 2 and aux in black_pieces:
                        p2wins += 1
                    n_play = 1
                    player_turn = 1  # Player 1 goes first
                    black_pieces = []
                    white_pieces = []
                    aux_pos = {}
                    selected = None
                    click = False
                    for pos in POSITIONS:
                        pos.set_busy(False)
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

def pc_move(piece, possmoveindex, white_pieces):
    aux = []
    for white in white_pieces:
        for pos in POSITIONS:
            if white == {'position': pos.get_position(), 'color': WHITE}:
                aux.append(pos)

    if possmoveindex == 1 and aux[piece].poss1.busy == False:
        white_pieces.append({'position': aux[piece].poss1.get_position(), 'color': WHITE})
        aux[piece].poss1.set_busy(True)
        for white in white_pieces:
            if white == {'position': aux[piece].get_position(), 'color': WHITE}:
                white_pieces.remove({'position': aux[piece].get_position(), 'color': WHITE})
                for pos in POSITIONS:
                    if pos.get_position() == aux[piece]:
                        pos.set_busy(False)

    if possmoveindex == 2 and aux[piece].poss2.busy == False:
        white_pieces.append({'position': aux[piece].poss2.get_position(), 'color': WHITE})
        aux[piece].poss2.set_busy(True)
        for white in white_pieces:
            if white == {'position': aux[piece].get_position(), 'color': WHITE}:
                white_pieces.remove({'position': aux[piece].get_position(), 'color': WHITE})
                for pos in POSITIONS:
                    if pos.get_position() == aux[piece]:
                        pos.set_busy(False)


    if possmoveindex == 3 and aux[piece].poss3.busy == False:
        white_pieces.append({'position': aux[piece].poss3.get_position(), 'color': WHITE})
        aux[piece].poss3.set_busy(True)
        for white in white_pieces:
            if white == {'position': aux[piece].get_position(), 'color': WHITE}:
                white_pieces.remove({'position': aux[piece].get_position(), 'color': WHITE})
                for pos in POSITIONS:
                    if pos.get_position() == aux[piece]:
                        pos.set_busy(False)


