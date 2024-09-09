import random

tabuleiro = [
    ['   ', '   ', '   '],
    ['   ', '   ', '   '],
    ['   ', '   ', '   ']
]

def exibe_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print('|'.join(linha))
        print('-' * 11)

def verifica_vitoria(tabuleiro, jogador):
    for linha in tabuleiro:
        if all([celula == jogador for celula in linha]):
            return True
    for coluna in range(3):
        if all([tabuleiro[linha][coluna] == jogador for linha in range(3)]):
            return True
    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
        return True
    return False

def verifica_empate(tabuleiro):
    for linha in tabuleiro:
        if '   ' in linha:
            return False
    return True

def movimento_humano(tabuleiro):
    while True:
        try:
            linha = int(input("Escolha a linha (0, 1 ou 2): "))
            coluna = int(input("Escolha a coluna (0, 1 ou 2): "))
            if tabuleiro[linha][coluna] == '   ':
                return linha, coluna
            else:
                print("Esta casa está ocupada, tente outra")
        except (ValueError, IndexError):
            print("Entrada inválida! Utilize números entre 0 e 2.")

def movimento_bot_medio(tabuleiro, bot, jogador_humano):
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == '   ':
                tabuleiro[linha][coluna] = jogador_humano
                if verifica_vitoria(tabuleiro, jogador_humano):
                    tabuleiro[linha][coluna] = '   '
                    return linha, coluna
                tabuleiro[linha][coluna] = '   '

    movimentos_disponiveis = [(linha, coluna) for linha in range(3) for coluna in range(3) if tabuleiro[linha][coluna] == '   ']
    return random.choice(movimentos_disponiveis)

def jogo_da_velha():
    tabuleiro = [['   ' for _ in range(3)] for _ in range(3)]
    player = ' x '

    while True:
        exibe_tabuleiro(tabuleiro)
        if player == ' x ':
            print(f'Turno do jogador {player}')
            x, y = movimento_humano(tabuleiro)
        else:
            print(f'Turno do bot {player}')
            x, y = movimento_bot_medio(tabuleiro, ' O ', ' x ')

        tabuleiro[x][y] = player

        if verifica_vitoria(tabuleiro, player):
            exibe_tabuleiro(tabuleiro)
            print(f'{player} venceu!')
            break

        if verifica_empate(tabuleiro):
            exibe_tabuleiro(tabuleiro)
            print("Empate!")
            break

        player = ' O ' if player == ' x ' else ' x '

jogo_da_velha()
