'''
048. Fazer um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
'''
s = 0  # Variável para acumular a soma
cont = 0  # Variável para contar quantos números foram somados

for i in range(3, 501, 3):  # Começa em 3 e vai até 500, saltando de 3 em 3 (apenas múltiplos de 3)
    s += i
    cont += 1
    print(f'{i}', end=' ')  # Imprimir os múltiplos na mesma linha

print(f'\nA soma de todos os {cont} múltiplos de 3 entre 1 e 500 é igual a {s}.')
