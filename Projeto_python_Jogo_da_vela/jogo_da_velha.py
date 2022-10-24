
vazio = " "

token_player = ["X","O"]

# CRIAR O BOARD 3x3 DO JOGO DA VELHA
def c_board():
    board = [
        [vazio, vazio, vazio],
        [vazio, vazio, vazio],
        [vazio, vazio, vazio],
    ]
    return board

# MOSTRAS O BOARD COM AS JOGADAS NA TELA
def print_board(board):
    for i in range(3):
        print("|".join(board[i]))
        if (i < 2):
            print("------")
    

# PEGA OS VALORES DE ENTRADA ESTÁ CERTA
def get_input_values(msn):
    try:
        number = int(input(msn))
        if ( number >= 1 and number <=3):
            return (number -1)
        else:
            print("Numero precisa estar entre 1 e 3 !")
            return get_input_values(msn)
    except :
        print("Numero Invalido!")
        return get_input_values(msn)

# VERIFICAR SE O MOVIMENTO RECEBIDO NO INPUT É VALIDO
def check_movement(board, li, col):
    if(board[li][col] == vazio):
        return True
    else:
        return False
    

# FAZ O MOVIMENTO
def make_movement(board, li, col, player):
    board[li][col] = token_player[player]

# VERIFICA O GANHADOR
def winner_check(board):
    
    # verificar linhas
    for li in range(3):
        if(board[li][0] == board[li][1] and board[li][1] == board[li][2] and board[li][0] != vazio):
            return board[li][0]
    # verificar colunas

    for col in range(3):
        if(board[0][col] == board[1][col] and board[1][col] == board[2][col] and board[0][col] != vazio):
            return board[0][col]
    # diagonal \
    if(board[0][0] != vazio and board[0][0] == board[1][1] and board[1][1] == board[2][2]):
        return board[0][0]
    # diagonal /
    elif(board[0][2] != vazio and board[0][2] == board[1][1]and board[1][1] == board[2][0]):
        return board[0][2]

    for li in range(3):
        for col in range(3):
            if (board[li][col] == vazio):
                return False
    
    return "EMPATE"
