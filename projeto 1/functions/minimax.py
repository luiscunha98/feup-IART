import math
from functions.dificulty import *


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

    if(black + white) == 0:
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

            value = max(value, minimax_white(depth - 1, False, aux_black, aux_white, possible_moves(aux_black, BLACK), alpha, beta))
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

            value = min(value, minimax_white(depth - 1, True, aux_black, aux_white, possible_moves(aux_white, WHITE), alpha, beta))
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

            value = max(value, minimax_black(depth - 1, False, aux_black, aux_white, possible_moves(aux_white, WHITE), alpha, beta))
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

            value = min(value, minimax_black(depth - 1, True, aux_black, aux_white, possible_moves(aux_black, BLACK), alpha, beta))
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