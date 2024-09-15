'''
058. Melhorar o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''
from random import randint

computador = randint(0, 10)
print('Sou o computador... e pensei num número entre 0 e 10.'
      '\nConsegues adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o teu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tenta mais uma vez.')
        elif jogador > computador:
            print('Menos... Tenta mais uma vez.')
print(f'CORRETO, com {palpites} tentativas!'
      f'\nParabéns!')
