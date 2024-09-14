'''
048. Fazer um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
'''
s = 0
c = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        c += 1
        s += i
        print(f'{i} ', end='')
print(f'\nO total da doma de {c} números é igual a {s}')
