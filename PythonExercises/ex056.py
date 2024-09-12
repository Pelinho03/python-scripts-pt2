'''
056.  Desenvolver um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
'''
# Inicializa as variáveis
soma_idades = 0
idade_mais_velho = 0
nome_mais_velho = ''
cont_mulheres_menor_20 = 0

# Loop para ler as informações de 4 pessoas
for i in range(4):
    print(f'\nPessoa {i + 1}:')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo (M/F): ').strip().upper()
    print('-=-' * 10)

    # Atualiza a soma das idades
    soma_idades += idade

    # Verifica se a pessoa é um homem e se ele é o mais velho
    if sexo == 'M':
        if idade > idade_mais_velho:
            idade_mais_velho = idade
            nome_mais_velho = nome

    # Conta quantas mulheres têm menos de 20 anos
    if sexo == 'F' and idade < 20:
        cont_mulheres_menor_20 += 1

# Calcula a média de idade
media_idade = soma_idades / 4

# Exibe os resultados
print(f'\nMédia de idade do grupo: {media_idade:.2f}')
print(f'Homem mais velho: {nome_mais_velho} com {idade_mais_velho} anos.')
print(f'Número de mulheres com menos de 20 anos: {cont_mulheres_menor_20}')

