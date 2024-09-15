'''
071. Cria um programa que simule o funcionamento de uma caixa multibanco. No início, pergunta ao utilizador qual o valor a ser levantado (número inteiro), e o programa deverá informar quantas notas de cada valor serão entregues.
'''
# Definir os valores das notas disponíveis
notas = [500, 200, 100, 50, 20, 10, 5, 1]

# Ler o valor a ser levantado
valor = int(input('Digite o valor a ser levantado (inteiro): '))

# Verificar se o valor é positivo
if valor <= 0:
    print('O valor deve ser um número inteiro positivo.')
else:
    print('Notas entregues:')

    for nota in notas:
        if valor >= nota:
            # Calcular o número de notas de cada valor
            quantidade = valor // nota
            valor %= nota
            # Exibir a quantidade de notas
            print(f'{quantidade} nota(s) de {nota}€')
