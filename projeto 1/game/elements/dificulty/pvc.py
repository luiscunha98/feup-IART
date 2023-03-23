import sys, math
from functions.auxiliar import *
from classes.button import *
from functions.minimax import *


def pvc(main_menu, dif):
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
                        player_turn, n_play = put_pieces(start_bpositions, PLAY_MOUSE_POS, player_turn, n_play,
                                                         white_pieces, black_pieces)
                        n_play, player_turn, white_pieces = cpu_positions(n_play, player_turn, start_wpositions,
                                                                          black_pieces, white_pieces, PLAY_MOUSE_POS,
                                                                          POSITIONS)
            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        main_menu()
                    else:
                        # Check if the click is within one of the positions
                        for i in range(20):
                            if distance(POSITIONS[i], PLAY_MOUSE_POS) < PIECE_RADIUS:
                                if player_turn == 1:
                                    if click:
                                        player_turn, black_pieces, selected, aux_pos = make_move(player_turn,
                                                                                                 POSITIONS[i],
                                                                                                 black_pieces, selected,
                                                                                                 aux_pos, BLACK)
                                        click = False
                                elif player_turn == 2:
                                    maxv = minimax(dif, True, black_pieces, white_pieces, possible_moves(white_pieces),
                                                   -math.inf, math.inf)
                                    print(maxv)

                                    for move in possible_moves(white_pieces):
                                        for position in POSITIONS:
                                            if move == {'position': position.get_position(), 'color': WHITE}:
                                                if move.value == maxv:
                                                    white_pieces.append(
                                                        {'position': move.get_position(), 'color': WHITE})
                                                    white_pieces[0].poss1.set_busy(True)
                                                    white_pieces[0].set_busy(False)
                                                    white_pieces.remove(
                                                        {'position': white_pieces[0].get_position(), 'color': WHITE})

                                    """for i in range(4):
                                        if maxv < minimax(dif, True, black_pieces, white_pieces, possible_moves(white_pieces[i].poss1), -math.inf, math.inf) and white_pieces[i].poss1 == False:
                                            maxv = minimax(dif, True, black_pieces, white_pieces, possible_moves(white_pieces[i].poss1), -math.inf, math.inf)
                                            aux = str(i) + "1"
                                        elif maxv < minimax(dif, True, black_pieces, white_pieces, possible_moves(white_pieces[i].poss2), -math.inf, math.inf) and white_pieces[i].poss2 == False:
                                            maxv = minimax(dif, True, black_pieces, white_pieces, possible_moves(white_pieces[i].poss2), -math.inf, math.inf)
                                            aux = str(i) + "2"
                                        elif maxv < minimax(dif, True, black_pieces, white_pieces, possible_moves(white_pieces[i].poss3), -math.inf, math.inf) and white_pieces[i].poss3 == False:
                                            maxv = minimax(dif, True, black_pieces, white_pieces, possible_moves(white_pieces[i].poss3), -math.inf, math.inf)
                                            aux = str(i) + "3"
                                    if aux == "01":
                                        white_pieces.append(
                                            {'position': white_pieces[0].poss1, 'color': WHITE})
                                        white_pieces[0].poss1.set_busy(True)
                                        white_pieces[0].set_busy(False)
                                        white_pieces.remove({'position': white_pieces[0].get_position(), 'color': WHITE})
                                    elif aux == "02":
                                        white_pieces.append(
                                            {'position': white_pieces[0].poss2, 'color': WHITE})
                                        white_pieces[0].poss2.set_busy(True)
                                        white_pieces[0].set_busy(False)
                                        white_pieces.remove({'position': white_pieces[0].get_position(), 'color': WHITE})
                                    elif aux == "03":
                                        white_pieces.append(
                                            {'position': white_pieces[0].poss3, 'color': WHITE})
                                        white_pieces[0].poss3.set_busy(True)
                                        white_pieces[0].set_busy(False)
                                        white_pieces.remove({'position': white_pieces[0].get_position(), 'color': WHITE})
                                    elif aux == "11":
                                        white_pieces.append(
                                            {'position': white_pieces[1].poss1, 'color': WHITE})
                                        white_pieces[1].poss1.set_busy(True)
                                        white_pieces[1].set_busy(False)
                                        white_pieces.remove({'position': white_pieces[1].get_position(), 'color': WHITE})
                                    elif aux == "12":
                                        white_pieces.append(
                                            {'position': white_pieces[1].poss2, 'color': WHITE})
                                        white_pieces[1].poss2.set_busy(True)
                                        white_pieces[1].set_busy(False)
                                        white_pieces.remove({'position': white_pieces[1].get_position(), 'color': WHITE})
                                    elif aux == "13":
                                        white_pieces.append(
                                            {'position': white_pieces[1].poss3, 'color': WHITE})
                                        white_pieces[1].poss3.set_busy(True)
                                        white_pieces[1].set_busy(False)
                                        white_pieces.remove({'position': white_pieces[1].get_position(), 'color': WHITE})
                                    elif aux == "21":
                                        white_pieces.append(
                                            {'position': white_pieces[2].poss1, 'color': WHITE})
                                        white_pieces[2].poss1.set_busy(True)
                                        white_pieces[2].set_busy(False)
                                        white_pieces.remove({'position': white_pieces[2].get_position(), 'color': WHITE})
                                    elif aux == "22":
                                        white_pieces.append(
                                            {'position': white_pieces[2].poss2, 'color': WHITE})
                                        white_pieces[2].poss2.set_busy(True)
                                        white_pieces[2].set_busy(False)
                                        white_pieces.remove({'position': white_pieces[2].get_position(), 'color': WHITE})
                                    elif aux == "23":
                                        white_pieces.append(
                                            {'position': white_pieces[2].poss3, 'color': WHITE})
                                        white_pieces[2].poss3.set_busy(True)
                                        white_pieces[2].set_busy(False)
                                        white_pieces.remove({'position': white_pieces[2].get_position(), 'color': WHITE})
                                    elif aux == "31":
                                        white_pieces.append(
                                            {'position': white_pieces[3].poss1, 'color': WHITE})
                                        white_pieces[3].poss1.set_busy(True)
                                        white_pieces[3].set_busy(False)
                                        white_pieces.remove({'position': white_pieces[3].get_position(), 'color': WHITE})
                                    elif aux == "32":
                                        white_pieces.append(
                                            {'position': white_pieces[3].poss2, 'color': WHITE})
                                        white_pieces[3].poss2.set_busy(True)
                                        white_pieces[3].set_busy(False)
                                        white_pieces.remove({'position': white_pieces[3].get_position(), 'color': WHITE})
                                    elif aux == "33":
                                        white_pieces.append(
                                            {'position': white_pieces[3].poss3, 'color': WHITE})
                                        white_pieces[3].poss3.set_busy(True)
                                        white_pieces[3].set_busy(False)
                                        white_pieces.remove({'position': white_pieces[3].get_position(), 'color': WHITE})
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
                                    selected = None"""
                                if player_turn == 1:
                                    if any(piece['position'] == POSITIONS[i].get_position() for piece in
                                           black_pieces):
                                        selected = POSITIONS[i]
                                        aux_pos = POSITIONS[i]
                                        click = True
                                """elif player_turn == 2:
                                    if any(piece['position'] == POSITIONS[i].get_position() for piece in
                                           white_pieces):
                                        selected = POSITIONS[i]
                                        aux_pos = POSITIONS[i]
                                        click = True"""
        for position in POSITIONS:
            if verify(position) == 1:
                # game_over(player_turn)
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
                player_turn = 1
                black_pieces = []
                white_pieces = []
                aux_pos = {}
                selected = None
                click = False
                for pos in POSITIONS:
                    pos.set_busy(False)
        pygame.display.update()
