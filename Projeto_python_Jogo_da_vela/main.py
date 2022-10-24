from jogo_da_velha import c_board,check_movement,winner_check,make_movement,print_board,get_input_values
from  minimax import  moviment_IA

# JOGADOR 1
player = 0 
x = "X"
o = "O"
board = c_board()
winner = winner_check(board)

while(not winner):
    print_board(board)
    print(f"Vez do Jogar {x if player == 0 else o}")

    if(player == 0):
        li, col = moviment_IA(board, player)
    else:
        li = get_input_values("Digite a Linha:_ ")
        col = get_input_values("Digite a Coluna:_ ")

    if(check_movement(board, li, col)):
        make_movement(board, li, col, player)
        player = ((player +1)%2)

    else:
        print("A posição já esta aculpada!")
    
    winner = winner_check(board)
    
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
print_board(board)
print(f"GANHADOR :  {winner}")
print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
