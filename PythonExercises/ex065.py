'''
065. Criar um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao utilizador se ele quer ou não continuar a digitar valores.
'''
resposta = 'N'
media = 0
soma = 0
maior = None
menor = None
total_numeros = 0

while resposta != 'S':
    cont = int(input('Quantos números queres ler? '))

    for i in range(cont):
        num = int(input('Digita um número: '))
        soma += num
        total_numeros += 1

        if maior is None or num > maior:
            maior = num
        if menor is None or num < menor:
            menor = num

    # Calcular a média
    if total_numeros > 0:
        media = soma / total_numeros

    resposta = input('Pretendes terminar? [S/N] ').strip().upper()

print(f'A média dos valores foi {media:.2f}.')
print(f'O maior valor foi {maior}.')
print(f'O menor valor foi {menor}.')

