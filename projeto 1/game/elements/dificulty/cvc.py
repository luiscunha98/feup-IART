import sys, math, random
from functions.auxiliar import *
from classes.button import *
from functions.minimax import *

def cvc(main_menu, dif):
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
                        if n_play < 5:
                            for i in start_bpositions:
                                if distance(POSITIONS[i], PLAY_MOUSE_POS) < 2000:
                                    # Check if the position is already occupied
                                    if not any(piece['position'] == POSITIONS[i].get_position() for piece in
                                               black_pieces + white_pieces):
                                        # Add the piece to the list
                                        while (player_turn == 1 and len(black_pieces) < 4):
                                            # place a white piece randomly
                                            index1 = random.randint(0, 19)
                                            if index1 in {0, 2, 7, 18, 19}:
                                                if not POSITIONS[index1].busy:
                                                    black_pieces.append(
                                                        {'position': POSITIONS[index1].get_position(), 'color': BLACK})
                                                    POSITIONS[index1].set_busy(True)
                                                    n_play += 1
                                        player_turn = 2

                        else:
                            for i in start_wpositions:
                                if distance(POSITIONS[i], PLAY_MOUSE_POS) < 2000:
                                    # Check if the position is already occupied
                                    if not any(piece['position'] == POSITIONS[i].get_position() for piece in
                                               black_pieces + white_pieces):
                                        # Add the piece to the list
                                        while (player_turn == 2 and len(white_pieces) < 4):
                                            # place a white piece randomly
                                            index2 = random.randint(8, 13)
                                            if index2 in {8, 9, 11, 12, 13}:
                                                if not POSITIONS[index2].busy:
                                                    white_pieces.append(
                                                        {'position': POSITIONS[index2].get_position(), 'color': WHITE})
                                                    POSITIONS[index2].set_busy(True)
                                                    n_play += 1
                                        player_turn = 1


        pygame.display.update()