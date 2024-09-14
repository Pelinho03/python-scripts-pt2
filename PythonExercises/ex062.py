'''
062. Melhorar o DESAFIO 061, perguntando para o utilizador se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
'''
# Lê o primeiro termo e a razão da PA
primeiro_termo = int(input('Digita o primeiro termo da PA: '))
razao = int(input('Digita a razão: '))

# Inicializa as variáveis
cont = 1
termo_atual = primeiro_termo
total_termos = 10  # Exibe inicialmente 10 termos
mais_termos = total_termos  # Começa por mostrar 10 termos

# Loop principal para mostrar os termos da PA
while mais_termos != 0:
    while cont <= total_termos:
        print(f'{termo_atual}', end=' -> ')
        termo_atual += razao
        cont += 1
    print('PAUSA')

    # Pergunta ao utilizador quantos termos quer ver a mais
    mais_termos = int(input('Quantos termos a mais queres ver? (0 para sair): '))
    total_termos += mais_termos  # Atualiza o total de termos a serem mostrados

print('FIM da progressão.')
