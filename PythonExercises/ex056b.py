'''
056.  Desenvolver um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
'''
# Inicializa as variáveis para calcular a soma das idades, a média de idade,
# o nome e a idade do homem mais velho e o número de mulheres com menos de 20 anos
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

# Loop para processar as informações de 4 pessoas
for p in range(1, 5):
    print(f'----- {p}ª PESSOA -----')

    # Leitura do nome, idade e sexo da pessoa
    nome = str(input('Nome: ')).strip()  # .strip() remove espaços extras no início e fim
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()  # Valida o sexo como 'M' ou 'F'
    print('-=-' * 5)

    # Soma das idades para posterior cálculo da média
    somaidade += idade

    # Verifica se a pessoa é o homem mais velho
    if p == 1 and sexo in 'Mm':  # Se for o primeiro homem, inicializa com ele
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:  # Atualiza se encontrar um homem mais velho
        maioridadehomem = idade
        nomevelho = nome

    # Contabiliza as mulheres com menos de 20 anos
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

# Calcula a média de idade do grupo
mediaidade = somaidade / 4

# Exibe os resultados finais
print(f'\nA média de idade do grupo é de {mediaidade:.1f} anos.')
print(f'O homem mais velho tem {maioridadehomem} anos e chama-se {nomevelho}.')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos.')

