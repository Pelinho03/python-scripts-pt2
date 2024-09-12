from random import randint
from time import sleep

# Cores ANSI
cores = {
    'limpa': '\033[m',
    'vermelho': '\033[31m',
    'verde': '\033[32m',
    'amarelo': '\033[33m',
    'azul': '\033[34m',
    'roxo': '\033[35m',
    'ciano': '\033[36m'
}

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print(f"""{cores['ciano']}OPÇÕES:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA{cores['limpa']}""")
jogador = int(input('Qual é a tua jogada? '))

if jogador not in [0, 1, 2]:
    print(f"{cores['vermelho']}JOGADA INVÁLIDA!{cores['limpa']}")
else:
    print(f"{cores['azul']}PEDRA{cores['limpa']}")
    sleep(1)
    print(f"{cores['amarelo']}PAPEL{cores['limpa']}")
    sleep(1)
    print(f"{cores['roxo']}TESOURA!!!!{cores['limpa']}")
    sleep(1)

    print(f"{cores['verde']}{'-=-' * 11}{cores['limpa']}")
    print(f"Computador jogou {cores['vermelho']}{itens[computador]}{cores['limpa']}")
    print(f"Jogador jogou {cores['azul']}{itens[jogador]}{cores['limpa']}")
    print(f"{cores['verde']}{'-=-' * 11}{cores['limpa']}")

    if computador == 0:  # Computador jogou PEDRA
        if jogador == 0:
            print(f"{cores['amarelo']}EMPATE{cores['limpa']}")
        elif jogador == 1:
            print(f"{cores['azul']}Vencedor: JOGADOR{cores['limpa']}")
        elif jogador == 2:
            print(f"{cores['vermelho']}Vencedor: COMPUTADOR{cores['limpa']}")
    elif computador == 1:  # Computador jogou PAPEL
        if jogador == 0:
            print(f"{cores['vermelho']}Vencedor: COMPUTADOR{cores['limpa']}")
        elif jogador == 1:
            print(f"{cores['amarelo']}EMPATE{cores['limpa']}")
        elif jogador == 2:
            print(f"{cores['azul']}Vencedor: JOGADOR{cores['limpa']}")
    elif computador == 2:  # Computador jogou TESOURA
        if jogador == 0:
            print(f"{cores['azul']}Vencedor: JOGADOR{cores['limpa']}")
        elif jogador == 1:
            print(f"{cores['vermelho']}Vencedor: COMPUTADOR{cores['limpa']}")
        elif jogador == 2:
            print(f"{cores['amarelo']}EMPATE{cores['limpa']}")
