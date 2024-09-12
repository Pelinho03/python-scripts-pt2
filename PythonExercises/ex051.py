'''
051.  Desenvolver um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
'''
# Lê o primeiro termo e a razão da PA
primeiro_termo = int(input('Primeiro termo da PA: '))
razao = int(input('Razão da PA: '))

# Exibe os 10 primeiros termos da PA usando um laço 'for'
for i in range(10):
    termo_atual = primeiro_termo + i * razao
    print(termo_atual, end=' -> ')

print('FIM')
