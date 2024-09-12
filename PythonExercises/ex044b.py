print('{:=^40}'.format('LOJA DO PAULO'))
preco = float(input('Preço das tuas compras: '))

print('''MÉTODOS DE PAGAMENTO
[ 1 ] A dinheiro.
[ 2 ] A Cartão Débito.
[ 3 ] 2x no Cartão.
[ 4 ] 3x ou mais no Cartão.''')
opcao = int(input('Qual o método? '))

if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    vezes = total / 2
    print(f'A tua compra será dividida em 2x de {vezes:.2f}€ SEM JUROS.')
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    total_vezes = int(input('Quantas vezes? '))
    vezes = total / total_vezes
    print(f'A tua compra será dividida em {total_vezes}x de {vezes:.2f}€ COM JUROS.')
else:
    total = 0
    print('OPÇÃO INVÁLIDA!')

if total > 0:
    print(f'A tua compra de {preco:.2f}€ vai custar {total:.2f}€ no total.')
