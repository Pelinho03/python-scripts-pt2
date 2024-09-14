'''
046. Fazer um programa que mostre no ecrã uma contagem regressiva para o estouro de fogos de artifício, de 10 até 0, com uma pausa de 1 segundo entre eles.
'''
from time import sleep

# Contagem regressiva de 10 até 0
for i in range(10, -1, -1):
    print(i)
    sleep(0.5)

# Mensagem de fim
print('BUM! BUM! PÁ! 🎆🎇🎆')
