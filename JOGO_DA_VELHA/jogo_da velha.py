def jogo_da_velha():
    print("---|-----")
    print("---|-----")
    print("---|-----")
    print("---|-----")
    print("---|-----")


tabuleiro = [1, 2, 3, 4, 5, 6, 7, 8, 9]
quadrado_magico = [4, 9, 2, 3, 5, 7, 8, 1, 6]
acabou = False
def ImprimirTabuleiro():
    print()
    print('', tabuleiro[0], "|", tabuleiro[1], "|", tabuleiro[2])
    print("---|---|---")
    print('', tabuleiro[3], "|", tabuleiro[4], "|", tabuleiro[5])
    print("---|---|---")
    print('', tabuleiro[6], "|", tabuleiro[7], "|", tabuleiro[8])
    print()

  


def pegar_numero():  # Função que recebe dados do Usuário
    while True:
        numero = input()
        try:
            numero = int(numero)
            if numero in range(1, 10):
                return numero
            else:
                print("\nNúmero não está no tabuleiro.")
        except ValueError:
            print("\nIsso não é um número. Tente novamente.")
        continue


def Turno(jogador):  # Função que verifica se o espaço já foi preenchido
    espaco_colocado = pegar_numero() - 1
    if tabuleiro[espaco_colocado] == "X" or tabuleiro[espaco_colocado] == "O":
        print("\nEspaço já ocupado. Tente colocar em outro.")
        Turno(jogador)
    else:
        tabuleiro[espaco_colocado] = jogador


def ChecaVitoria(jogador):  # Função que verifica qual jogador venceu o jogo
    jogadas = 0

    for x in range(9):
        for y in range(9):
            for z in range(9):
                if x != y and y != z and z != x:
                    if tabuleiro[x] == jogador and tabuleiro[y] == jogador and tabuleiro[z] == jogador:
                        if quadrado_magico[x] + quadrado_magico[y] + quadrado_magico[z] == 15:
                            print("Jogador", jogador, "ganhou!\n")
                            return True

    for a in range(9):
        if tabuleiro[a] == "X" or tabuleiro[a] == "O":
            jogadas += 1
        if jogadas == 9:
            print("O jogo acabou em um empate\n")
            return True

# verifica se o jogo acabou
while not acabou:
    ImprimirTabuleiro()
    acabou = ChecaVitoria("O")
    if acabou == True:
        break
    print("Jogador X, escolha um espaço.")
    Turno("X")
    
    
# Função que imprime o tabuleiro na tela
    ImprimirTabuleiro()
    acabou = ChecaVitoria("X")
    if acabou == True:
        break
    print("Jogador O, escolha um espaço.")
    Turno("O")

jogo_da_velha() # chamada da função
