'''
059. Criar um programa que leia dois valores e mostre um menu no ecrã:
- [ 1 ] somar
- [ 2 ] multiplicar
- [ 3 ] maior
- [ 4 ] novos números
- [ 5 ] sair do programa
    - O programa deverá realizar a operação solicitada em cada caso.
'''
from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('\n---- CALCULADORA ----'
          '\n[1] Somar'
          '\n[2] Multiplicar'
          '\n[3] Maior'
          '\n[4] Novos números'
          '\n[5] Sair do programa'
          '\n', '-' * 20)
    opcao = int(input('Qual a opção? '))
    if opcao == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é {soma}.')
    elif opcao == 2:
        produto = n1 * n2
        print(f'O resultado de {n1} x {n2} é {produto}.')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior é {maior}.')
    elif opcao == 4:
        print('Indica os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('A terminar...')
    else:
        print('Opção inválida. Tenta novamente!')
    print('=-=' * 10)
    sleep(2)
print('Fim do programa! Volte sempre!')
