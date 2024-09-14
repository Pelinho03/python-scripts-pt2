'''
053. Criar um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
'''
frase = str(input('Digita uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
#print(f'{junto}')
#print(f'{palavras}')
#print(f'{inverso}')
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print('TEMOS UM PALÍNDROMO!')
else:
    print('NÃO É UM PALÍNDROMO!')
