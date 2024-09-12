'''
053. Criar um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
'''
# Lê uma frase do utilizador
frase = input('Digite uma frase: ').replace(' ', '').lower()  # Remove espaços e transforma em minúsculas

# Verifica se a frase é um palíndromo
if frase == frase[::-1]:  # Compara a frase com a sua reversa
    print('A frase é um palíndromo!')
else:
    print('A frase não é um palíndromo!')
