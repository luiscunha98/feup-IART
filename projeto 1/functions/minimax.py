import math
from functions.dificulty import *

def utility(white_pieces, black_pieces):
    white = 0
    black = 0
    for b in black_pieces:
        for position in POSITIONS:
            if b == {'position': position.get_position(), 'color': WHITE}:
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

    return (black - white)/(black+white)

def minimax(depth, is_maximizing, black_pieces, white_pieces, possible_moves, alpha, beta):
    # Check if game over or maximum depth reached
    for i in range(20):
        if verify(POSITIONS[i]) or depth == 0:
            return utility(white_pieces, black_pieces)
        #else:
        #   return 1  # parte do game over

    # If it's the maximizing player's turn
    if is_maximizing:
        value = -math.inf
        for move in possible_moves:
            value = max(value, minimax(depth - 1, False, black_pieces, white_pieces, possible_moves, alpha, beta))
            move[1].value = value
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return value

    # If it's the minimizing player's turn
    else:
        value = math.inf
        for move in possible_moves:
            value = min(value, minimax(depth - 1, True, black_pieces, white_pieces, possible_moves, alpha, beta))
            move[1].value = value
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value


"""
def make_best_move():
    bestScore = -math.inf
    bestMove = None
    for move in ticTacBoard.get_possible_moves():
        ticTacBoard.make_move(move)
        score = minimax(False, aiPlayer, ticTacBoard)
        ticTacBoard.undo()
        if (score > bestScore):
            bestScore = score
            bestMove = move
    ticTacBoard.make_move(bestMove)

def minimax(isMaxTurn, maximizerMark, board):
    state = board.get_state()
    if (state is State.DRAW):
        return 0
    elif (state is State.OVER):
        return 1 if board.get_winner() is maximizerMark else -1

    scores = []
    for move in board.get_possible_moves():
        board.make_move(move)
        scores.append(minimax(not isMaxTurn, maximizerMark, board))
        board.undo()

    return max(scores) if isMaxTurn else min(scores)"""

# def minimax()