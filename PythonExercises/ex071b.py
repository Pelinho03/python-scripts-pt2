'''
071. Cria um programa que simule o funcionamento de uma caixa multibanco. No início, pergunta ao utilizador qual o valor a ser levantado (número inteiro), e o programa deverá informar quantas notas de cada valor serão entregues.
'''
# Exibe a interface inicial do "Banco Nota"
print('=' * 30)
print('{:^30}'.format('BANCO NOTA'))  # Centraliza o título "BANCO NOTA" com 30 caracteres
print('=' * 30)

# Solicita o valor a ser levantado
valor = int(input('Quanto queres levantar? '))

# Inicializa variáveis para controle das notas e do total a ser processado
total = valor  # Valor total a ser levantado
nota = 50  # Começa pelas notas de 50€
totnotas = 0  # Contador de notas de cada valor

# Loop principal para calcular a quantidade de notas
while True:
    if total >= nota:
        # Se o valor restante for maior ou igual ao valor da nota, subtrai o valor da nota
        total -= nota
        totnotas += 1  # Conta uma nota do valor atual
    else:
        if totnotas > 0:
            # Mostra o total de notas de um determinado valor, se houver
            print(f'Total de {totnotas} notas de {nota}€')

        # Altera o valor da nota para o próximo disponível (50 -> 20 -> 10 -> 1)
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1

        # Reinicia o contador de notas para o novo valor de nota
        totnotas = 0

        # Se o total chegou a 0, encerra o loop
        if total == 0:
            break

# Exibe a mensagem final
print('=' * 30)
print('Volte sempre ao BANCO NOTA!'
      '\nTem um bom dia!')
