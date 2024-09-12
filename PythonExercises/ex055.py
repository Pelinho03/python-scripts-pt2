'''
055. Fazer um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
'''
# Inicializa as variáveis para armazenar o maior e o menor peso
maior = float('-inf')  # Inicializa com o menor valor possível
menor = float('inf')  # Inicializa com o maior valor possível

# Loop para ler o peso de 5 pessoas
for i in range(5):
    peso = float(input(f'Adiciona o peso da {i + 1}ª pessoa (em kg): '))

    # Atualiza o maior peso, se necessário
    if peso > maior:
        maior = peso

    # Atualiza o menor peso, se necessário
    if peso < menor:
        menor = peso

# Exibe o maior e o menor peso registrado
print(f'O maior peso foi {maior:.2f} kg e o menor peso foi {menor:.2f} kg.')
