'''
039. Escrever um programa que leia o ano de nascimento de um jovem e informa, de acordo com a sua idade:
- Se ele ainda vai se alistar no serviço militar;
- Se é a hora de se alistar;
- Se já passou do tempo do alistamento.
    - O programa também deverá mostrar o tempo que faltou ou que passou do prazo.
'''
# Leitura do ano de nascimento
ano = int(input('Em que ano nasceste? '))

# Cálculo da idade com base no ano atual (2024)
idade = 2024 - ano
print(f'Tens {idade} anos.')

# Verificação das condições de alistamento
if idade == 18:
    print('É hora de te alistares!')
elif idade < 18:
    anos_faltam = 18 - idade
    print(f'Ainda te vais alistar. Faltam {anos_faltam} anos para o alistamento.')
else:
    anos_passados = idade - 18
    print('Já passaste da idade de alistamento.')
    print(f'Passaram-se {anos_passados} anos desde o período de alistamento.')

