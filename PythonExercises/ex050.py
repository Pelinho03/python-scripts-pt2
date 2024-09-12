'''
050. Desenvolver um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
'''
# Inicializa a soma dos pares
soma_pares = 0

# Laço 'for' para receber 6 números
for i in range(1, 7):
    # Lê um número inteiro do utilizador
    num = int(input(f'Digita o {i}º número: '))

    # Verifica se o número é par e soma
    if num % 2 == 0:
        soma_pares += num

# Imprime o resultado final apenas uma vez
print(f'A soma dos números pares é {soma_pares}.')


