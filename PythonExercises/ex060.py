'''
060. Fazer um programa que leia um número qualquer e mostre o seu fatorial.
'''
# Lê um número do utilizador
num = int(input('Digita um número: '))

# Inicializa as variáveis: 'resultado' começa em 1, e 'count' é o contador
resultado = 1
count = num

# Exibe o título do cálculo do fatorial
print(f'\n{num}! = ', end='')

# Loop para calcular o fatorial e mostrar o processo
while count > 0:
    print(f'{count}', end='')  # Mostra o número atual
    resultado *= count  # Atualiza o resultado
    count -= 1  # Decrementa o contador
    if count > 0:
        print(f' x ', end='')  # Mostra o 'x' se ainda houver multiplicações a fazer
    else:
        print(f' = {resultado}')  # Mostra o resultado final quando terminar

# Exibe o fatorial do número
print(f'\nO fatorial de {num} é {resultado}.')
