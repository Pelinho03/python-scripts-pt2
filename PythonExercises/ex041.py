'''
041.  A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre a sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM;
- Até 14 anos: INFANTIL;
- Até 19 anos: JUNIOR;
- Até 20 anos: SÉNIOR;
- Acima: MASTER.
'''
# Leitura do ano de nascimento
ano = int(input('Em que ano nasceste? '))

# Cálculo da idade com base no ano atual (2024)
idade = 2024 - ano

# Verificação da categoria de acordo com a idade do atleta
if idade <= 9:
    print(f'Com {idade} anos és MIRIM.')
elif idade <= 14:
    print(f'Com {idade} anos és INFANTIL.')
elif idade <= 19:
    print(f'Com {idade} anos és JUNIOR.')
elif idade <= 20:
    print(f'Com {idade} anos és SÉNIOR.')
else:
    print(f'Com {idade} anos és MASTER.')
