'''
064. Criar um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o utilizador digitar o valor 999, que é a condição de paragem. No final, mostra quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
'''
cont = 0  # Inicializamos a contagem a 0
soma = 0  # Variável que vai armazenar a soma dos números
num = 0   # Inicializamos num a 0 (o valor não tem impacto inicial)

# Loop que vai correr até o utilizador digitar 999
while num != 999:
    num = int(input('Digita um número (999 para parar): '))
    if num != 999:  # Só somamos e contamos se o número não for o flag 999
        soma += num
        cont += 1  # Contamos mais um número válido

print(f'FIM'
      f'\nForam contabilizados {cont} números e a soma entre eles foi {soma}.')

