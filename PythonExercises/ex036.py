'''
036. Escrever um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
- Calcular o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
'''
# Dados de entrada
valor_casa = float(input('Qual é o valor da casa? € '))
salario = float(input('Qual é o teu salário mensal? € '))
anos = int(input('Em quantos anos vais pagar a casa? '))

# Cálculo da prestação mensal
meses = anos * 12
prestacao_mensal = valor_casa / meses

# Verificação se a prestação excede 30% do salário
limite = salario * 0.30

print(f'A prestação mensal será de: €{prestacao_mensal:.2f}')

if prestacao_mensal > limite:
    print('Empréstimo NEGADO. A prestação excede 30% do teu salário.')
else:
    print('Empréstimo APROVADO.')
