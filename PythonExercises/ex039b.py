from datetime import date

# Obter a data atual (ano, mês, dia)

ano_atual = date.today().year
mes_atual = date.today().month
dia_atual = date.today().day

# Recolher dados de nascimento
nasc = int(input('Ano de nascimento: '))
mes_nasc = int(input('Mês de nascimento (número): '))
dia_nasc = int(input('Dia de nascimento: '))

# Cálculo inicial da idade
idade = ano_atual - nasc

# Ajustar a idade se ainda não fez anos no ano atual
if mes_nasc > mes_atual or (mes_nasc == mes_atual and dia_nasc > dia_atual):
    idade -= 1

print(f'Quem nasceu em {nasc} tem {idade} anos em {ano_atual}.')

# Condições de alistamento
if idade == 18:
    print('\nTens que te alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print(f'\nAinda faltam {saldo} anos para te alistares!')
    ano_alistamento = ano_atual + saldo
    print(f'O teu alistamento será em {ano_alistamento}.')
else:
    saldo = idade - 18
    print(f'\nJá te devias ter alistado há {saldo} anos.')
    ano_alistamento = ano_atual - saldo
    print(f'O teu alistamento foi em {ano_alistamento}.')
