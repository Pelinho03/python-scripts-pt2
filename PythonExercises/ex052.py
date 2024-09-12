'''
052. Fazer um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''
# Lê um número inteiro do utilizador
num = int(input('Digite um número: '))

# Números menores ou iguais a 1 não são primos
if num <= 1:
    print(f'{num} não é um número primo!')
else:
    # Assume inicialmente que o número é primo
    primo = True
    # Verifica divisores de 2 até a raiz quadrada de num
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            primo = False
            break

    if primo:
        print(f'{num} é um número primo!')
    else:
        print(f'{num} não é um número primo!')
