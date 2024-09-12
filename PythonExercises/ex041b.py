'''
041.  A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre a sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM;
- Até 14 anos: INFANTIL;
- Até 19 anos: JÚNIOR;
- Até 25 anos: SÉNIOR;
- Acima: MASTER.
'''
from datetime import date

ano_nasc = int(input('Ano de nascimento: '))
mes_nasc = int(input('Mês de nascimento: '))
dia_nasc = int(input('Dia de nascimento: '))

# Obter a data atual
ano_atual = date.today().year
mes_atual = date.today().month
dia_atual = date.today().day

# Calcular a idade
idade = ano_atual - ano_nasc

# Ajustar idade se ainda não fez anos no ano atual
if mes_nasc > mes_atual or (mes_nasc == mes_atual and dia_nasc > dia_atual):
    idade -= 1

# Classificar o atleta de acordo com a idade
if idade <= 9:
    print(f'Com {idade} anos és MIRIM.')
elif idade <= 14:
    print(f'Com {idade} anos és INFANTIL.')
elif idade <= 19:
    print(f'Com {idade} anos és JÚNIOR.')
elif idade <= 25:
    print(f'Com {idade} anos és SÉNIOR.')
else:
    print(f'Com {idade} anos és MASTER.')
