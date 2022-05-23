import random

def main():
    print('Vamos Jogar JokenPô!\n',
    'Escolha uma das opções: papel, pedra, tesoura')
    player = input('Digite: ')
    computer = random.choice(['papel','pedra','tesoura'])

    if computer == player:
        return 'Empate!'
    
    win = winners(player,computer)

    if win:
        return "Vaocê ganhou!"
    
    return 'Você perdeu.'

def winners(player,computer):
    if (player == 'papel' and computer == 'pedra') \
        or (player == 'tesoura' and computer == 'papel') \
        or (player == 'pedra' and computer == 'tesoura'):
        return True
    
    return False




if __name__ == '__main__':
    print(main())