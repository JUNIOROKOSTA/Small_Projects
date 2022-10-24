from jogo_da_velha import vazio, token_player, winner_check

def moviment_IA(board, player):
    possibilities = get_positions(board)
    best_move = None
    best_value = None
    for possibilitie in possibilities:
        board[possibilitie[0]][possibilitie[1]] = token_player[player]
        valuer = minimax(board, player)
        board[possibilitie[0]][possibilitie[1]] = vazio

        if(best_value is None):
            best_value = valuer
            best_move = possibilitie
        elif(player == 0 ):
            if(valuer > best_value):
                best_value = valuer
                best_move = possibilitie
        elif(player == 0 ):
            if(valuer < best_value):
                best_value = valuer
                best_move = possibilitie

    return best_move[0], best_move[1]

    

def get_positions(board):
    position=[]
    for li in range(3):
        for col in range(3):
            if (board[li][col] == vazio):
                position.append([li,col])
    return position

score = {
    "EMPATE": 0,
    "X": 1,
    "O": -1
}

def minimax(board,player):
    winner_player = winner_check(board)
    if(winner_player):
        return score[winner_player]

    player = ((player+1)%2)

    possibilities = get_positions(board)
    best_value = None
    for possibilitie in possibilities:
        board[possibilitie[0]][possibilitie[1]] = token_player[player]
        valuer = minimax(board, player)
        board[possibilitie[0]][possibilitie[1]] = vazio

        if(best_value is None):
            best_value = valuer
        elif(player == 0 ):
            if(valuer > best_value):
                best_value = valuer

        elif(player == 0 ):
            if(valuer < best_value):
                best_value = valuer
 
    return best_value