'''
049. Refazer o DESAFIO 009, mostrando a tabuada de um número que o utilizador escolher, só que agora utilizando um laço for.
'''
# Solicita ao utilizador que introduza um número para gerar a tabuada
num = int(input('Escolhe um número: '))

# Laço 'for' para percorrer os números de 1 a 10
for i in range(1, 11):  # O passo 1 é implícito, então não é necessário especificá-lo
    # Exibe o resultado da multiplicação, com o valor de 'i' formatado para ocupar 2 espaços (para melhor alinhamento)
    print(f'{num} x {i:2} = {num * i}')
