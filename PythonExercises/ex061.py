'''
061. Refazer o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
'''
# Lê o primeiro termo e a razão da PA
primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

# Inicializa o contador e o termo atual
cont = 1
termo_atual = primeiro_termo

# Exibe os 10 primeiros termos usando while
print('Os 10 primeiros termos da PA são:')
while cont <= 10:
    print(f'{termo_atual}', end=' -> ')
    termo_atual += razao  # Atualiza o termo com a razão
    cont += 1  # Incrementa o contador

print('FIM')
