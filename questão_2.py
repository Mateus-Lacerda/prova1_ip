## Aqui eu fiz as importações, NumPy para utilização de matrizes e a função time.sleep(), para melhorar a fluidez do jogo.
import numpy as np
from time import sleep


## Criação da função principal, a ideia é ter um ponto de recursividade, caso haja algum problema durante a execução do código.
def main():
    print("Olá, bem vindo ao Jogo da Velha NumPY! ")
    sleep(1)
    player_1 = input("Qual o nome do primeiro jogador? Ele jogará com o \"X\". ")
    sleep(1)
    player_2 = input("Qual o nome do segundo jogador? Ele jogará com o \"O\". ")
    sleep(1)
    print("Instruções:\nA cada jogada, você deverá escolher a linha e a coluna da posição em que deseja realizar a jogada, " 
          "as entradas deverão ser números de 1 a 3.\nVamos começar!")
    

    ## Criação de uma matriz modelo, onde serão adicionadas as jogadas de cada jogador e ocorrerá o jogo. 
    model = np.full((3,3),' ')


    ## Essa função mostra os créditos finais e reinicia o jogo. 
    def ending():
        print("Muito obrigado por jogar Jogo da Velha NumPy!\nA game by: Mateus Lacerda.\nReiniciando o jogo...")
        sleep(2)
        main()


    ## Essa função mostra o modelo quando chamada
    def display_model():
        print(f"{model[0][0]}|{model[0][1]}|{model[0][2]}")
        print("_____")
        print(f"{model[1][0]}|{model[1][1]}|{model[1][2]}")
        print("_____")
        print(f"{model[2][0]}|{model[2][1]}|{model[2][2]}")
        

    ## Essa função irá adicionar a jogada feita à matriz modelo, ela adiciona a jogada apenas se o espaço estiver desocupado, usando if-else.
    ## Ela recebe o nome do jogador e o símbolo que ele está usando.
    def move(player, symbol):
        print(f"Vez de {player}.\n")
        i,j = int(input("Escolha a linha da jogada: ")), int(input("Escolha a coluna da jogada: "))

        if model[i-1][j-1] == ' ':
            model[i-1][j-1] = symbol

        else:
            print("Esse espaço já está ocupado! ")
            if player == player_1:
                player_1_game()
            elif player == player_2:
                player_2_game()


    ## Essa funçao irá checar se há algum jogador vitorioso, comparando os elementos com if-statements.
    def check_for_win(model, player):
        ## Aqui é usado um laço for para diminuir o tamanho do código, e comparar eficientemente os elementos de cada linha ou coluna.
        for i in range(3):
            if model[i][0] == model[i][1] == model[i][2] != ' ':
                print(f"{player} ganhou!")
                ending()
            
            elif model[0][i] == model[1][i] == model[2][i] != ' ':
                print(f"{player} ganhou!")
                ending()

        if model[0][0] == model[1][1] == model[2][2] != ' ' or model[0][2] == model[1][1] == model[2][0] != ' ':
            print(f"{player} ganhou!")
            ending()

        ## Aqui o código, após checar se há vitórias, indica que o jogo "deu velha", caso o modelo esteja cheio.
        counter = 0
        for i in range(3):
            if (' ' in model[i]) == False:
                counter += 1

        if counter == 3:
            print("Deu velha!")
            ending()


    ## Cada uma dessas funções representa um dos jogadores jogando, usando as outras funções criadas.
    def player_1_game():
            sleep(1)
            move(player_1, 'X')
            check_for_win(model,player_1)


    def player_2_game():
            sleep(1)
            move(player_2, 'O')
            check_for_win(model,player_2)

    ## Esse laço while roda infinitamente, até que um jogador ganhe e o jogo seja reiniciado.    
    while True:
        display_model()
        player_1_game()
        display_model()
        player_2_game()

if __name__ == '__main__': ## Condição para rodar o programa
    main()
