'''
070. Cria um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o utilizador quer continuar ou não. No final, mostra:
- A) Qual é o total gasto na compra.
- B) Quantos produtos custam mais de 1000€.
- C) Qual é o nome do produto mais barato.
'''
from time import sleep

total_compras = 0
maior_1000 = 0
barato = None
nome_prod_barato = ''

while True:
    # Ler o nome e o preço do produto
    nome = str(input('Digita o nome do artigo: '))
    preco = float(input('Digita o preço do artigo: '))

    # Adicionar o preço ao total
    total_compras += preco

    # Verificar se o produto custa mais de 1000€
    if preco > 1000:
        maior_1000 += 1

    # Identificar o produto mais barato
    if barato is None or preco < barato:
        barato = preco
        nome_prod_barato = nome

    # Perguntar se o utilizador quer continuar
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Pretendes continuar? [S/N]: ')).strip().upper()[0]

    if escolha == 'N':
        break
print('{:-^40}'.format('Programa finalizado.'))
print('\nA calcular resultados...')
sleep(1)
print('3')
sleep(1)
print('2')
sleep(1)
print('1')
sleep(2)
# Exibir os resultados finais
print(f'\nO total gasto é de {total_compras:.2f}€')
print(f'Acima de 1000€ temos {maior_1000} artigos')
print(f'O produto mais barato foi {nome_prod_barato} que custa {barato:.2f}€')
