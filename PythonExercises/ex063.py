'''
063. Escrever um programa que leia um número N inteiro qualquer e mostre no ecrã os N primeiros elementos de uma Sequência de Fibonacci.
'''
# Lê o número de termos da sequência de Fibonacci que o utilizador quer ver
n = int(input('Quantos termos da sequência de Fibonacci queres ver? '))

# Inicializa os dois primeiros termos da sequência
t1 = 0
t2 = 1
cont = 3  # Começamos em 3 porque os dois primeiros termos já são conhecidos

# Exibe os dois primeiros termos
print(f'{t1} -> {t2}', end='')

# Loop para calcular e mostrar os próximos termos
while cont <= n:
    t3 = t1 + t2  # O próximo termo é a soma dos dois anteriores
    print(f' -> {t3}', end='')
    t1 = t2  # Atualiza t1 para o valor de t2
    t2 = t3  # Atualiza t2 para o valor de t3
    cont += 1

print(' -> FIM')
