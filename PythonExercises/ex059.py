'''
059. Criar um programa que leia dois valores e mostre um menu no ecrã:
- [ 1 ] somar
- [ 2 ] multiplicar
- [ 3 ] maior
- [ 4 ] novos números
- [ 5 ] sair do programa
    - O programa deverá realizar a operação solicitada em cada caso.
'''
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

# Lê os valores iniciais
num1 = int(input(f'Digite o {cores["roxo"]}1º valor: {cores["limpa"]}'))
num2 = int(input(f'Digite o {cores["roxo"]}2º valor: {cores["limpa"]}'))

while True:
    # Mostra o menu
    print('\n---- CALCULADORA ----'
          '\n[1] Somar'
          '\n[2] Multiplicar'
          '\n[3] Maior'
          '\n[4] Novos números'
          '\n[5] Sair do programa'
          '\n', '-' * 20)

    # Lê a escolha do utilizador
    escolha = int(input('Escolha uma das opções: '))

    # Executa a operação com base na escolha
    if escolha == 1:
        soma = num1 + num2
        print(f'A soma dos valores {num1} e {num2} é igual a {cores["verde"]}{soma}{cores["limpa"]}.')
    elif escolha == 2:
        multi = num1 * num2
        print(f'O produto dos valores {num1} e {num2} é igual a {cores["verde"]}{multi}{cores["limpa"]}.')
    elif escolha == 3:
        maior = max(num1, num2)
        print(f'O maior valor entre {num1} e {num2} é {cores["verde"]}{maior}{cores["limpa"]}.')
    elif escolha == 4:
        # Lê novos valores
        num1 = int(input(f'Digite o {cores["roxo"]}1º valor: {cores["limpa"]}'))
        num2 = int(input(f'Digite o {cores["roxo"]}2º valor: {cores["limpa"]}'))
    elif escolha == 5:
        sleep(0.5)
        print('A sair do programa...')
        sleep(0.5)
        print('3')
        sleep(1)
        print('2')
        sleep(1)
        print('1')
        sleep(1)
        print('Obrigado!')
        break  # Sai do loop e encerra o programa
    else:
        print('Opção inválida. Tente novamente.')
