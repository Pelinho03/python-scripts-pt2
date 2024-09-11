import random

print('-=-' * 20)
print('1- Pedra'
      '\n2- Papel'
      '\n3- Tesoura')
print('-=-' * 20)
escolha = int(input('Escolhe uma das opções acima: '))

lista = ['Pedra', 'Papel', 'Tesoura']
pc = random.choice(lista)

if escolha == 1:
    print(f'Escolheste Pedra e o computador escolheu {pc}.')
    if pc == 'Pedra':
        print('EMPATE')
    elif pc == 'Papel':
        print('PERDESTE')
    else:
        print('VENCESTE')
elif escolha == 2:
    print(f'Escolheste Papel e o computador escolheu {pc}.')
    if pc == 'Pedra':
        print('VENCESTE')
    elif pc == 'Papel':
        print('EMPATE')
    else:
        print('PERDESTE')
elif escolha == 3:
    print(f'Escolheste Tesoura e o computador escolheu {pc}.')
    if pc == 'Pedra':
        print('PERDESTE')
    elif pc == 'Papel':
        print('VENCESTE')
    else:
        print('EMPATE')
