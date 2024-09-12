'''
042. Reforça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: todos os lados iguais;
- Isósceles: dois lados iguais;
- Escaleno: todos os lados diferentes.
'''
# Leitura dos comprimentos das três retas
r1 = float(input('Indica o comprimento da primeira reta: '))
r2 = float(input('Indica o comprimento da segunda reta: '))
r3 = float(input('Indica o comprimento da terceira reta: '))

# Verificar se as três retas podem formar um triângulo
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As três retas podem formar um triângulo ', end='')

    # Determinar o tipo de triângulo
    if r1 == r2 == r3:
        print('EQUILÁTERO.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('ISÓSCELES.')
    else:
        print('ESCALENO.')
else:
    print('As três retas NÃO podem formar um triângulo.')
