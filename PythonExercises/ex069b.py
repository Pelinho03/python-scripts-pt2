'''
069. Criar um programa que leia a idade e o sexo de várias pessoas. A cada pessoa registada, o programa deverá perguntar se o utilizador quer ou não continuar. No final, mostre:
- A) quantas pessoas tem mais de 18 anos.
- B) quantos homens foram registados
- C) quantas mulheres tem menos de 20 anos.
'''
from time import sleep

# Inicializa os contadores
tot18 = toth = totm = 0

# Loop principal para coletar informações
while True:
    # Solicita a idade da pessoa
    print('-=-'*12)
    idade = int(input('Digite a idade: '))

    # Solicita o sexo da pessoa e garante que a entrada seja válida
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
        print('-=-' * 12)

    # Atualiza o contador baseado na idade e no sexo
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade < 20:
        totm += 1

    # Pergunta se o usuário deseja continuar
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]

    # Se a resposta for 'N', encerra o loop
    if resp == 'N':
        break

# Exibe a mensagem de finalização com um delay para efeito visual
print('\nPrograma Finalizado com sucesso!')
print('A calcular resultados em...')
sleep(1)
print('3')
sleep(1)
print('2')
sleep(1)
print('1')
sleep(1)

# Exibe os resultados finais com formatação
print('\n' + '-' * 40)
print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Total de homens registrados: {toth}')
print(f'Total de mulheres com menos de 20 anos: {totm}')
print('-' * 40)
