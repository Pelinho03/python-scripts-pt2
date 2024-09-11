'''
038. Escrever um programa que leia dois números inteiros e compare-os, mostrando no ecrã uma mensagem:
- O primeiro valor é maior;
- O segundo valor é maior;
- Não existe valor maior, os dois são iguais.
'''
# Leitura dos dois números inteiros fornecidos pelo utilizador
num1 = int(input('1º número: '))
num2 = int(input('2º número: '))

# Verificação se o primeiro número é maior que o segundo
if num1 > num2:
    print(f'O 1º número {num1} é maior que o 2º número {num2}.')
# Verificação se o segundo número é maior que o primeiro
elif num2 > num1:
    print(f'O 2º número {num2} é maior que o 1º número {num1}.')
# Caso contrário, significa que ambos os números são iguais
else:
    print(f'Nenhum dos dois é maior, 1º={num1} é igual ao 2º={num2}.')

