'''
058. Melhorar o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''
import random

# O computador escolhe um número aleatório entre 0 e 10
pc_escolha = random.randint(0, 10)

# Inicializa a variável para armazenar o número de tentativas
tot_tentativas = 1

# Solicita ao usuário que escolha um número
user_escolha = int(input('Escolhe um número de 0 a 10: '))

# Loop que continua até o usuário acertar o número escolhido pelo computador
while pc_escolha != user_escolha:
    # Incrementa o contador de tentativas
    tot_tentativas += 1

    # Solicita ao usuário que escolha um novo número
    user_escolha = int(input('Valor incorreto! Tenta novamente entre 0 e 10. '))

# Exibe uma mensagem quando o usuário acerta o número
print(f'CORRETO!'
      f'\nO computador escolheu {pc_escolha} e tu escolheste {user_escolha}. Parabéns!'
      f'\nNúmero de tentativas: {tot_tentativas}')
