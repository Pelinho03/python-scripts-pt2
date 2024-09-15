'''
068. Fazer um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''
import random

# Inicializa o contador de vitórias consecutivas
vitorias = 0

while True:
    # Jogador escolhe um número
    jogador_num = int(input('Escolhe um número: '))

    # Computador escolhe um número aleatório
    computador_num = random.randint(0, 10)

    # Jogador escolhe se quer Par ou Ímpar
    escolha = ''
    while escolha not in 'PI':  # Valida a entrada
        escolha = input('Par ou Ímpar? [P/I]: ').strip().upper()[0]

    # Soma dos números
    total = jogador_num + computador_num

    # Verifica se o total é par ou ímpar
    if total % 2 == 0:
        resultado = 'P'
    else:
        resultado = 'I'

    # Exibe os números e a soma
    print(f'\nTu escolheste {jogador_num} e o computador {computador_num}. Total = {total}.')

    # Verifica se o jogador acertou
    if resultado == escolha:
        print(f'Acertaste! O total é {"Par" if resultado == "P" else "Ímpar"}.')
        vitorias += 1  # Incrementa as vitórias consecutivas
    else:
        print(f'Perdeste! O total é {"Par" if resultado == "P" else "Ímpar"}.')
        break  # O jogo termina quando o jogador perde

    print('-=-' * 10)  # Separador visual

# Exibe o total de vitórias consecutivas ao final do jogo
print(f'\nJogo encerrado. Conseguistes {vitorias} vitórias consecutivas.')
