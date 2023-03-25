from functions.auxiliar import *
import sys, random, math


def verify(position):
    if position.busy is True and position.poss1.busy is True and position.poss2.busy is True and position.poss3.busy is True:
        return True  # winner
    else:
        return False  # no winner


def possible_moves(pieces, color):
    possible_moves = []
    for p in pieces:
        for position in POSITIONS:
            if p == {'position': position.get_position(), 'color': color}:
                if not position.poss1.busy:
                    possible_moves.append((position, position.poss1))
                if not position.poss2.busy:
                    possible_moves.append((position, position.poss2))
                if not position.poss3.busy:
                    possible_moves.append((position, position.poss3))

    return possible_moves


def put_pieces(positions, PLAY_MOUSE_POS, player_turn, n_play, white_pieces, black_pieces):
    for i in positions:
        if distance(POSITIONS[i], PLAY_MOUSE_POS) < PIECE_RADIUS:
            if not any(piece['position'] == POSITIONS[i].get_position() for piece in black_pieces + white_pieces):

                if player_turn == 1 and len(black_pieces) < 4:
                    color = BLACK
                    black_pieces.append({'position': POSITIONS[i].get_position(), 'color': color})
                    POSITIONS[i].set_busy(True)
                    if len(black_pieces) == 4:
                        player_turn = 2
                    n_play += 1

                elif player_turn == 2 and len(white_pieces) < 4:
                    color = WHITE
                    white_pieces.append({'position': POSITIONS[i].get_position(), 'color': color})
                    POSITIONS[i].set_busy(True)
                    if len(white_pieces) == 4:
                        player_turn = 1
                    n_play += 1

    return player_turn, n_play


def make_move(player_turn, position, pieces, selected, aux_pos, color):
    if (selected == position.poss1 and position.busy == False) or (
            selected == position.poss2 and position.busy == False) or (
            selected == position.poss3 and position.busy == False):

        pieces.remove({'position': aux_pos.get_position(), 'color': color})
        aux_pos.set_busy(False)
        pieces.append({'position': position.get_position(), 'color': color})
        position.set_busy(True)

        if player_turn == 1:
            player_turn = 2
        elif player_turn == 2:
            player_turn = 1
    selected = None

    return player_turn, pieces, selected, aux_pos


def change_positions(position, pieces, selected, aux_pos, click):
    if any(piece['position'] == position.get_position() for piece in pieces):
        selected = position
        aux_pos = position
        click = True

    return selected, aux_pos, click


def game_over(player_turn, p1wins, p2wins, white_pieces, black_pieces, POSITIONS, n_play, aux_pos, selected, click):
    for position in POSITIONS:
        if verify(position) == 1:
            aux = {'position': position.get_position(), 'color': BLACK}
            aux2 = {'position': position.get_position(), 'color': WHITE}

            # verify winner
            if player_turn == 1 and aux2 in white_pieces:
                p1wins += 1
            elif player_turn == 1 and aux in black_pieces:
                p2wins += 1
            elif player_turn == 2 and aux2 in white_pieces:
                p1wins += 1
            elif player_turn == 2 and aux in black_pieces:
                p2wins += 1

            # reset of the board
            n_play = 1
            player_turn = 1
            black_pieces = []
            white_pieces = []
            aux_pos = {}
            selected = None
            click = False
            for pos in POSITIONS:
                pos.set_busy(False)

    return p1wins, p2wins, white_pieces, black_pieces, n_play, player_turn, aux_pos, selected, click


def quit_game(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()


def cpu_positions(n_play, player_turn, positions, black_pieces, white_pieces, PLAY_MOUSE_POS, POSITIONS):
    if n_play < 5:
        for i in positions:
            if distance(POSITIONS[i], PLAY_MOUSE_POS) < 2000:
                if not any(piece['position'] == POSITIONS[i].get_position() for piece in black_pieces + white_pieces):
                    while player_turn == 1 and len(black_pieces) < 4:
                        index = random.randint(0, 19)
                        if index in {0, 2, 7, 18, 19}:
                            if not POSITIONS[index].busy:
                                black_pieces.append({'position': POSITIONS[index].get_position(), 'color': BLACK})
                                POSITIONS[index].set_busy(True)
                    player_turn = 2
        return n_play + 4, player_turn, black_pieces
    if n_play >= 5:
        for i in positions:
            if distance(POSITIONS[i], PLAY_MOUSE_POS) < 2000:
                if not any(piece['position'] == POSITIONS[i].get_position() for piece in black_pieces + white_pieces):
                    while player_turn == 2 and len(white_pieces) < 4:
                        index = random.randint(8, 13)
                        if index in {8, 9, 11, 12, 13}:
                            if not POSITIONS[index].busy:
                                white_pieces.append(
                                    {'position': POSITIONS[index].get_position(), 'color': WHITE})
                                POSITIONS[index].set_busy(True)
                    player_turn = 1
        return n_play + 4, player_turn, white_pieces


def cpu_movements(player_turn, dif, black_pieces, white_pieces):
    if player_turn == 1:
        maxv = minimax_black(dif, True, black_pieces, white_pieces, possible_moves(black_pieces, BLACK),
                             -math.inf, math.inf)

        moves = possible_moves(black_pieces, BLACK)
        for move in moves:
            if move[1].value == maxv:
                black_pieces.append({'position': move[1].get_position(), 'color': BLACK})
                move[1].set_busy(True)
                position_to_remove = move[0].get_position()
                black_pieces.remove({'position': position_to_remove, 'color': BLACK})
                move[0].set_busy(False)
                player_turn = 2
                break
        return player_turn, black_pieces

    elif player_turn == 2:
        maxv = minimax_white(dif, True, black_pieces, white_pieces, possible_moves(white_pieces, WHITE), -math.inf,
                             math.inf)

        moves = possible_moves(white_pieces, WHITE)
        for move in moves:
            if move[1].value == maxv:
                white_pieces.append({'position': move[1].get_position(), 'color': WHITE})
                move[1].set_busy(True)
                position_to_remove = move[0].get_position()
                white_pieces.remove({'position': position_to_remove, 'color': WHITE})
                move[0].set_busy(False)
                player_turn = 1
                break
        return player_turn, white_pieces


def utility(white_pieces, black_pieces):
    white = 0
    black = 0

    for b in black_pieces:
        for position in POSITIONS:
            if b == {'position': position.get_position(), 'color': BLACK}:
                if position.poss1.busy:
                    black += 1
                if position.poss2.busy:
                    black += 1
                if position.poss3.busy:
                    black += 1

    for w in white_pieces:
        for position in POSITIONS:
            if w == {'position': position.get_position(), 'color': WHITE}:
                if position.poss1.busy:
                    white += 1
                if position.poss2.busy:
                    white += 1
                if position.poss3.busy:
                    white += 1

    if (black + white) == 0:
        return 1
    else:
        return (black - white) / (black + white)


def minimax_white(depth, is_maximizing, black_pieces, white_pieces, moves, alpha, beta):
    aux_white = white_pieces
    aux_black = black_pieces

    # Check if game over or maximum depth reached
    for i in range(20):
        if verify(POSITIONS[i]) or depth == 0:
            return utility(white_pieces, black_pieces)
        # else:
        #   return 1  # parte do game over

    # If it's the maximizing player's turn
    if is_maximizing:
        value = -math.inf
        for move in moves:
            # simulate move
            aux_white.append({'position': move[1].get_position(), 'color': WHITE})
            move[1].set_busy(True)
            position_to_remove = move[0].get_position()
            aux_white.remove({'position': position_to_remove, 'color': WHITE})
            move[0].set_busy(False)

            value = max(value,
                        minimax_white(depth - 1, False, aux_black, aux_white, possible_moves(aux_black, BLACK), alpha,
                                      beta))
            move[1].value = value

            # undo move
            aux_white.remove({'position': move[1].get_position(), 'color': WHITE})
            move[1].set_busy(False)
            position_to_append = move[0].get_position()
            white_pieces.append({'position': position_to_append, 'color': WHITE})
            move[0].set_busy(True)

            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return value

    # If it's the minimizing player's turn
    else:
        value = math.inf
        for move in moves:
            # simula
            aux_black.append({'position': move[1].get_position(), 'color': BLACK})
            move[1].set_busy(True)
            position_to_remove = move[0].get_position()
            aux_black.remove({'position': position_to_remove, 'color': BLACK})
            move[0].set_busy(False)

            value = min(value,
                        minimax_white(depth - 1, True, aux_black, aux_white, possible_moves(aux_white, WHITE), alpha,
                                      beta))
            move[1].value = value

            aux_black.remove({'position': move[1].get_position(), 'color': BLACK})
            move[1].set_busy(False)
            position_to_append = move[0].get_position()
            aux_black.append({'position': position_to_append, 'color': BLACK})
            move[0].set_busy(True)

            beta = min(beta, value)
            if beta <= alpha:
                break
        return value


def minimax_black(depth, is_maximizing, black_pieces, white_pieces, moves, alpha, beta):
    aux_white = white_pieces
    aux_black = black_pieces

    # Check if game over or maximum depth reached
    for i in range(20):
        if verify(POSITIONS[i]) or depth == 0:
            return utility(white_pieces, black_pieces)
        # else:
        #   return 1  # parte do game over

    # If it's the maximizing player's turn
    if is_maximizing:
        value = -math.inf
        for move in moves:
            # simulate move
            aux_black.append({'position': move[1].get_position(), 'color': BLACK})
            move[1].set_busy(True)
            position_to_remove = move[0].get_position()
            aux_black.remove({'position': position_to_remove, 'color': BLACK})
            move[0].set_busy(False)

            value = max(value,
                        minimax_black(depth - 1, False, aux_black, aux_white, possible_moves(aux_white, WHITE), alpha,
                                      beta))
            move[1].value = value

            # undo move
            aux_black.remove({'position': move[1].get_position(), 'color': BLACK})
            move[1].set_busy(False)
            position_to_append = move[0].get_position()
            black_pieces.append({'position': position_to_append, 'color': BLACK})
            move[0].set_busy(True)

            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return value

    # If it's the minimizing player's turn
    else:
        value = math.inf
        for move in moves:
            # simula
            aux_white.append({'position': move[1].get_position(), 'color': WHITE})
            move[1].set_busy(True)
            position_to_remove = move[0].get_position()
            aux_white.remove({'position': position_to_remove, 'color': WHITE})
            move[0].set_busy(False)

            value = min(value,
                        minimax_black(depth - 1, True, aux_black, aux_white, possible_moves(aux_black, BLACK), alpha,
                                      beta))
            move[1].value = value

            aux_white.remove({'position': move[1].get_position(), 'color': WHITE})
            move[1].set_busy(False)
            position_to_append = move[0].get_position()
            aux_white.append({'position': position_to_append, 'color': WHITE})
            move[0].set_busy(True)

            beta = min(beta, value)
            if beta <= alpha:
                break
        return value
