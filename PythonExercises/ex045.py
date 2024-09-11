'''
045. Criar um programa que faça o computador jogar Pedra, Papel, Tesoura connosco.
'''
import random

# Exibição das opções
print('-=-' * 20)
print('1- Pedra'
      '\n2- Papel'
      '\n3- Tesoura')
print('-=-' * 20)

# Leitura da escolha do utilizador
escolha = int(input('Escolhe uma das opções acima: '))

# Lista com as opções
opcoes = ['Pedra', 'Papel', 'Tesoura']

# Escolha do computador
pc = random.choice(opcoes)

# Mapeamento da escolha do utilizador
if escolha == 1:
    escolha_utilizador = 'Pedra'
elif escolha == 2:
    escolha_utilizador = 'Papel'
elif escolha == 3:
    escolha_utilizador = 'Tesoura'
else:
    print('Opção inválida! Escolhe 1, 2 ou 3.')
    exit()

# Exibição das escolhas
print(f'Escolheste {escolha_utilizador} e o computador escolheu {pc}.')

# Determinação do resultado
if escolha_utilizador == pc:
    resultado = 'EMPATE'
elif (escolha_utilizador == 'Pedra' and pc == 'Tesoura') or \
     (escolha_utilizador == 'Papel' and pc == 'Pedra') or \
     (escolha_utilizador == 'Tesoura' and pc == 'Papel'):
    resultado = 'VENCESTE'
else:
    resultado = 'PERDESTE'

print(resultado)
