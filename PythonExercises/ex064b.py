'''
064. Criar um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o utilizador digitar o valor 999, que é a condição de paragem. No final, mostra quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
'''
num = cont = soma = 0
num = int(input('Digita um número [999 para parar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digita um número [999 para parar]: '))
print(f'Digitaste {cont} números e a soma entre eles foi de {soma}.')
