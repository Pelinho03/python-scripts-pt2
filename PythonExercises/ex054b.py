from datetime import date

def contar_maioridade(anos_nascimento):
    ano_atual = date.today().year
    menores = 0
    maiores = 0
    for ano in anos_nascimento:
        idade = ano_atual - ano
        if idade < 18:
            menores += 1
        else:
            maiores += 1
    return menores, maiores

# Leitura dos anos de nascimento
anos_nascimento = [int(input(f'Insira o ano de nascimento da {i + 1}ª pessoa: ')) for i in range(7)]

# Contagem de maioridade
menores, maiores = contar_maioridade(anos_nascimento)

# Exibição do resultado
print('-=-' * 10)
print(f'Número de menores de idade: {menores}')
print(f'Número de maiores de idade: {maiores}')
print('-=-' * 10)
