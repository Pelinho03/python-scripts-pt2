'''
066. Criar um programa que leia números inteiros pelo teclado.
O programa só vai parar quando o utilizador digitar o valor 999,
que é a condição de paragem. No final, mostra quantos números foram
digitados e qual foi a soma entre eles (desconsiderando o flag).
'''

# Inicializa o contador e a soma
cont = 0
soma = 0

# Inicia o loop infinito, que será interrompido apenas com o 'break'
while True:
    num = int(input('Digita um número (999 para parar): '))

    # Se o número for diferente de 999, incrementa o contador e soma
    if num != 999:
        cont += 1
        soma += num
    else:
        # Se o número for 999, interrompe o loop
        break

# Exibe o total de números digitados e a soma (sem contar o 999)
print(f'Digitaste um total de {cont} números e a soma foi igual a {soma}')
