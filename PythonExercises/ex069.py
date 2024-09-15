'''
069. Criar um programa que leia a idade e o sexo de várias pessoas. A cada pessoa registada, o programa deverá perguntar se o utilizador quer ou não continuar. No final, mostre:
- A) quantas pessoas tem mais de 18 anos.
- B) quantos homens foram registados
- C) quantas mulheres tem menos de 20 anos.
'''
from time import sleep

escolha = ''
quant_18 = quant_homem = quant_mulher_20 = 0
while escolha in 'Ss':
    idade = int(input('Digita a idade: '))
    sexo = str(input('Digita o sexo [M/F]: ')).strip().upper()[0]
    if escolha in 'Ss':
        if idade > 18:
            quant_18 += 1
        if sexo in 'Mm':
            quant_homem += 1
        if sexo in 'Ff' and idade < 20:
            quant_mulher_20 += 1
        print('-=-' * 20)
        escolha = str(input('Pretendes continuar? [S/N] ')).strip().upper()[0]
        print('-=-' * 20)
    else:
        break
print(f'Programa Finalizado com sucesso'
      f'\nA calcular resultados em...')
sleep(1)
print('3')
sleep(1)
print('2')
sleep(1)
print('1')
sleep(1)
print(f'Pessoas maior de 18 = {quant_18}'
      f'\nHomens registados = {quant_homem}'
      f'\nMulheres menos de 20 = {quant_mulher_20}')
