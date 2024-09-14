'''
055. Fazer um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
'''
# Inicializa as variáveis para armazenar o maior e menor peso
maior = 0
menor = 0

# Loop para pedir o peso de 5 pessoas
for p in range(1, 6):
    # Solicita o peso da pessoa e converte para float
    peso = float(input(f'Digita o peso da {p}ª pessoa: '))

    # Para a primeira pessoa, define o maior e menor peso como o peso da primeira entrada
    if p == 1:
        maior = peso
        menor = peso
    else:
        # Verifica se o peso atual é maior que o maior peso registado
        if peso > maior:
            maior = peso
        # Verifica se o peso atual é menor que o menor peso registado
        if peso < menor:
            menor = peso

# Exibe uma linha decorativa
print('\n', '-=-' * 20)

# Exibe o maior e o menor peso registado
print(f'O maior peso foi de {maior}Kg.')
print(f'O menor peso foi de {menor}Kg.')

# Exibe outra linha decorativa
print('-=-' * 20)
