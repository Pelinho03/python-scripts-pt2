'''
065. Criar um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao utilizador se ele quer ou não continuar a digitar valores.
'''
resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digita um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Queres continuar? [S/N] ')).strip().upper()
media = soma / quant
print(f'Acabaste de digitar {quant} números e a média foi {media}.')
print(f'O maior número {maior} e o menor foi {menor}.')
