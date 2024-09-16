'''
068. Fazer um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''
from random import randint

# Inicializa o contador de vitórias consecutivas
v = 0

# Loop principal do jogo
while True:
    # Recebe um valor do jogador
    jogador = int(input('Diz um valor: '))

    # O computador escolhe um número aleatório entre 0 e 11
    computador = randint(0, 11)

    # Calcula o total dos valores jogados
    total = jogador + computador

    # Solicita ao jogador se quer jogar par ou ímpar
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]

    # Exibe o resultado do jogo
    print(f'Jogaste {jogador} e o computador {computador}. Total de {total}', end='')
    print(f'DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')

    # Verifica se o jogador ganhou ou perdeu
    if tipo == 'P':
        if total % 2 == 0:
            print('Venceste!')
            v += 1  # Incrementa o contador de vitórias
        else:
            print('Perdeste!')
            break  # Encerra o jogo se o jogador perdeu
    elif tipo == 'I':
        if total % 2 == 1:
            print('Venceste!')
            v += 1  # Incrementa o contador de vitórias
        else:
            print('Perdeste!')
            break  # Encerra o jogo se o jogador perdeu

    print('Vamos jogar novamente...')

# Exibe o número total de vitórias consecutivas quando o jogo termina
print(f'GAME OVER! Venceste {v} vezes.')
