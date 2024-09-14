'''
051.  Desenvolver um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
'''
# O utilizador insere o primeiro termo da PA
primeiro_termo = int(input('Primeiro termo: '))

# O utilizador insere a razão (a diferença constante entre os termos da PA)
razao = int(input('Razão: '))

# Cálculo do décimo termo da PA
# Fórmula do enésimo termo de uma PA: termo_n = primeiro_termo + (n - 1) * razao
# Como queremos o 10º termo, n = 10
decimo = primeiro_termo + (10 - 1) * razao

# O loop for vai de "primeiro_termo" até "decimo + razao", com passos iguais à razão
# A razão é usada como o intervalo de incremento entre os termos
for i in range(primeiro_termo, decimo + razao, razao):
    # Exibe o termo atual seguido de uma seta
    print(f'{i} ', end='-> ')

# Após imprimir todos os termos, exibe "FIM" para sinalizar o final da sequência
print('FIM')

