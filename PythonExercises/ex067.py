'''
067. Fazer um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo utilizador.
O programa será interrompido quando o número solicitado for negativo.
'''
while True:
    # Lê o número do utilizador
    num = int(input('Digita um número para ver a tabuada (valor negativo para sair): '))

    # Verifica se o número é negativo, e se for, interrompe o loop
    if num < 0:
        break

    # Exibe a tabuada do número positivo
    print(f'\n-- Tabuada do {num} --')

    # Loop para calcular e exibir a tabuada do número
    for i in range(1, 11):
        tabuada = num * i
        print(f'{num} x {i:2} = {tabuada}')

    # Linha de separação entre tabuadas
    print('-=-' * 5)

# Mensagem de encerramento do programa
print('Programa encerrado. FIM')
