'''
060. Fazer um programa que leia um número qualquer e mostre o seu fatorial.
'''
from math import factorial

n = int(input('Digita um n+umero para calcular o seu Fatorial: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}.')
