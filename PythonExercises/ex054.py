'''
054. Criar um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''
from datetime import date

# Obtém o ano atual
ano_atual = date.today().year

# Contadores para menores e maiores de idade
menores = 0
maiores = 0

# Loop para ler o ano de nascimento de 7 pessoas
for i in range(7):
    ano_nascimento = int(input(f'Insira o ano de nascimento da {i + 1}ª pessoa: '))
    idade = ano_atual - ano_nascimento

    # Verifica se a pessoa é menor ou maior de idade
    if idade < 18:
        menores += 1
    else:
        maiores += 1

# Exibe o resultado
print('-=-' * 10)
print(f'Número de menores de idade: {menores}')
print(f'Número de maiores de idade: {maiores}')
print('-=-' * 10)
