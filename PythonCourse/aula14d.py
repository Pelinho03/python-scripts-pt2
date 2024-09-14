n = 1
par = impar = 0
while n != 0:
    n = int(input('Digita um valor: '))
    if n % 2 == 0:
        par += 1
    else:
        impar += 1
print(f'Inseriste {par} número pares e {impar} números ímpares!')
