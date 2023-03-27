import sys
from functions.dificulty import *
from classes.button import *


def pvp(main_menu):

    # local variables
    aux_pos = {}
    selected = None
    click = False
    n_play = 1
    player_turn = 1  # Player 1 go first
    black_pieces = []
    white_pieces = []
    p1wins = 0
    p2wins = 0
    moves = 0

    while True:

        #base
        SCREEN.blit(BG, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        BOARD = pygame.image.load("resources/images/Board.png")
        SCREEN.blit(BOARD, (340, 100))
        PLAY_TEXT = get_font(35).render("PLAYER VS PLAYER", True, "White")
        SCORE_TEXT = get_font(25).render("SCORE", True, "White")
        PLAYER1_TEXT = get_font(20).render("PLAYER 1: " + str(p1wins), True, "White")
        PLAYER2_TEXT = get_font(20).render("PLAYER 2: " + str(p2wins), True, "White")
        MOVES_TEXT = get_font(20).render("MOVES: " + str(moves), True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 50))
        SCORE_RECT = PLAY_TEXT.get_rect(center=(400, 150))
        PLAYER1_RECT = PLAY_TEXT.get_rect(center=(350, 200))
        PLAYER2_RECT = PLAY_TEXT.get_rect(center=(350, 250))
        MOVES_RECT = PLAY_TEXT.get_rect(center=(400, 550))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)
        SCREEN.blit(SCORE_TEXT, SCORE_RECT)
        SCREEN.blit(PLAYER1_TEXT, PLAYER1_RECT)
        SCREEN.blit(PLAYER2_TEXT, PLAYER2_RECT)
        SCREEN.blit(MOVES_TEXT,MOVES_RECT)
        start_bpositions = {0, 2, 7, 18, 19}
        start_wpositions = {8, 9, 11, 12, 13}

        # draw possible start positions
        if n_play < 5 and len(black_pieces) != 4:
            for i in start_bpositions:
                pygame.draw.circle(SCREEN, BLUE, (POSITIONS[i].get_position()), PIECE_RADIUS)

        if n_play >= 5 and len(white_pieces) != 4:
            for i in start_wpositions:
                pygame.draw.circle(SCREEN, BLUE, (POSITIONS[i].get_position()), PIECE_RADIUS)

        # draw the pieces on the board
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

        # button definition, hover changes and update
        PLAY_BACK = Button(image=None, pos=(175, 625), text_input="QUIT GAME", font=get_font(35), base_color="White", hovering_color="Red")
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            quit_game(event)

            # Players put all of their pieces in the board first
            if n_play < 9:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        main_menu()
                    else:
                        player_turn, n_play = put_pieces(start_bpositions, PLAY_MOUSE_POS, player_turn, n_play, white_pieces, black_pieces)
                        player_turn, n_play = put_pieces(start_wpositions, PLAY_MOUSE_POS, player_turn, n_play, white_pieces, black_pieces)

            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        main_menu()
                    else:
                        for i in range(20):
                            if distance(POSITIONS[i], PLAY_MOUSE_POS) < PIECE_RADIUS:
                                if click:

                                    # make_move
                                    if player_turn == 1:
                                        player_turn, black_pieces, selected, aux_pos = make_move(player_turn, POSITIONS[i], black_pieces, selected, aux_pos, BLACK)
                                        moves+=1
                                    elif player_turn == 2:
                                        player_turn, white_pieces, selected, aux_pos = make_move(player_turn, POSITIONS[i], white_pieces, selected, aux_pos, WHITE)
                                        moves+=1
                                    click = False

                                # change positions of selected and aux_pos
                                if player_turn == 1:
                                    selected, aux_pos, click = change_positions(POSITIONS[i], black_pieces, selected, aux_pos, click)
                                elif player_turn == 2:
                                    selected, aux_pos, click = change_positions(POSITIONS[i], white_pieces, selected, aux_pos, click)

            # game over
            p1wins, p2wins, white_pieces, black_pieces, n_play, player_turn, aux_pos, selected, click = game_over(player_turn, p1wins, p2wins, white_pieces, black_pieces, POSITIONS, n_play, aux_pos, selected, click)

        pygame.display.update()
