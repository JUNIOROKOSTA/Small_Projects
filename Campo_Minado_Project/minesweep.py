vazio = "0"
bomba = "*"
board = [
        [vazio, bomba, vazio, vazio, vazio, vazio, bomba, vazio, vazio, vazio],
        [vazio, vazio, vazio, vazio, vazio, vazio, bomba, vazio, vazio, vazio],
        [vazio, vazio, bomba, vazio, vazio, vazio, bomba, vazio, vazio, bomba],
        [vazio, vazio, bomba, vazio, vazio, vazio, bomba, vazio, vazio, bomba],
        [vazio, bomba, vazio, vazio, bomba, vazio, vazio, bomba, vazio, vazio],
        [vazio, bomba, vazio, vazio, vazio, vazio, bomba, vazio, vazio, vazio],
        [vazio, vazio, vazio, vazio, vazio, vazio, bomba, vazio, vazio, vazio],
        [vazio, vazio, bomba, vazio, vazio, vazio, bomba, vazio, vazio, bomba],
        [vazio, vazio, bomba, vazio, vazio, vazio, bomba, vazio, vazio, bomba],
        [vazio, bomba, vazio, vazio, bomba, vazio, vazio, bomba, vazio, vazio]
        ]


# PRINT BOARD
def print_board(board):
    for i in range(10):
        print("|".join(board[i]))
        if (i < 9):
            print("-------------------")
    print("<________________________>")
    

# CRIAR O BOARD 5x5 DO JOGO DA VELHA


def winner_check(board):
    t=10
    num =0
    for linha in range(t): # linha == Linhas do Campo
        #print(f'For1_linha: {linha}')
        for coluna in range(t): # coluna == Colunas do Campo
            #print(f'For2_coluna: {coluna}')
            if (board[linha][coluna] == vazio): # Verifica Posição (linha,coluna), se é Vazio 
                #print(f'If1_Board_linha_coluna é vazio: {board[linha][coluna]}')
                for a in range((linha-1),(linha+2)): # Laço percorre linha-1 a linha+2 // Exemplo: Se linha for == 0 : linha-1 ==-1 e linha+2 == 2. Laço vai de -1 a 2.
                    #print(f'For3_a_no_range_linha-1_linha+2: {a} _ {linha-1} e {linha+2}')
                    for b in range((coluna-1),(coluna+2)): # Laço percorre coluna-1 a coluna+2 // Exemplo: Se coluna for == 1 : coluna-1 == 0 e coluna+2 == 3. laço vai de de 0 a 3.
                        #print(f'For4_b_range_coluna-1_coluna+2: {b} _ {coluna-1} e {coluna+2}')
                        if ((a>=0 and b>=0) and (a<t and b<t)): # Se a e b >= 0 e Se a e b < t, retorna True.
                            #print(f'If2_a>=0_b>=0__e__a<t_b<t: {a} _>=0_ {b} _/_t_ {t}')
                            if (board[a][b] == bomba): # Se na Posição a e b do Campo for igual a Bomba.
                                #print(f'If3_board[a][b]_=_Bomba: {board[a][b]}')
                                num+=1 # Variavel num recebe mais 1.
                                #print(f'num_: {num}')
                board[linha][coluna] = str(num)
                #print(f'board[linha][coluna]: {board[linha][coluna]}')
                num=0
                
    print_board(board)


print_board(board)

winner_check(board)
