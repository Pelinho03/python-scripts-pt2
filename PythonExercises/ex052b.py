'''
052. Fazer um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''
# Solicita ao utilizador um número inteiro
num = int(input('Digita um número: '))

# Variável para contar quantas vezes o número foi divisível
tot = 0

# Loop para verificar quantos divisores o número tem
for c in range(1, num + 1):
    # Verifica se o número é divisível pelo contador atual (c)
    if num % c == 0:
        print('\033[33m', end=' ')  # Se for divisível, muda a cor para amarelo
        tot += 1  # Incrementa o total de divisões bem-sucedidas
    else:
        print('\033[31m', end=' ')  # Se não for divisível, muda a cor para vermelho
    print(f'{c}', end='')  # Exibe o número do divisor

# Exibe o total de divisões bem-sucedidas
print(f'\n\033[mO número {num} foi divisível {tot} vezes.')

# Verifica se o número é primo (número primo é divisível apenas 2 vezes: por 1 e por ele mesmo)
if tot == 2:
    print('É PRIMO!')
else:
    print('NÃO É PRIMO!')

