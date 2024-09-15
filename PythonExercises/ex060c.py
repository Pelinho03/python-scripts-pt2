'''
060. Fazer um programa que leia um número qualquer e mostre o seu fatorial.
'''
n = int(input('Digita um número para calcular o seu Fatorial: '))
c = n
f = 1
print(f'Calcular {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f*=c
    c -= 1
print(f'{f}')
