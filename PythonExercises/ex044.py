'''
044. Elabora um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de programação:
- À vista dinheiro/cheque: 10% de desconto;
- À vista no cartão: 5% de desconto;
- Em até 2x no cartão: preço normal;
- 3x ou mais no cartão: 20% de juros.
'''
# Leitura do preço do produto
preco = float(input('Preço do produto: '))
print('-=-' * 20)
print('1- À vista dinheiro/cheque - 10% de desconto'
      '\n2- À vista no cartão - 5% de desconto'
      '\n3- Em até 2x no cartão - preço normal'
      '\n4- 3x ou mais no cartão - 20% de juros')
print('-=-' * 20)

# Leitura da escolha do usuário
escolha = int(input('Escolha uma das opções de 1 a 4: '))

# Cálculo do valor a ser pago com base na escolha
if escolha == 1:
    # Desconto de 10% à vista dinheiro/cheque
    preco_final = preco * 0.9
    print(f'O produto custa {preco:.2f}€. Com 10% de desconto, fica por {preco_final:.2f}€.')
elif escolha == 2:
    # Desconto de 5% à vista no cartão
    preco_final = preco * 0.95
    print(f'O produto custa {preco:.2f}€. Com 5% de desconto, fica por {preco_final:.2f}€.')
elif escolha == 3:
    # Preço normal em até 2x no cartão
    print(f'O produto custa {preco:.2f}€. Em até 2x no cartão, o preço é o normal.')
elif escolha == 4:
    # Juros de 20% em 3x ou mais no cartão
    preco_final = preco * 1.2
    print(f'O produto custa {preco:.2f}€. Com 20% de juros, fica por {preco_final:.2f}€.')
else:
    print('Opção inválida! Escolha uma opção de 1 a 4.')