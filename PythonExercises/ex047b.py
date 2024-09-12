'''
047. Criar um programa que mostre no ecrã todos os números pares que estão no intervalo entre 1 e 50.
'''
for i in range(1, 51, 1):
    if i % 2 == 0:
        print(f'{i} ', end='')
print('\nTodos os números pares entre 1 e 50 foram listados!')
