'''
037. Escrever um programa que leia um número qualquer e peça para o utilizador escolher qual será a base de conversão:
- 1 para binário;
- 2 para octal;
- 3 para hexadecimal.
'''
print('-=-' * 20)
num = int(input('Um número qualquer: '))
print('-=-' * 20)

# Menu de opções
print('Escolhe a base de conversão:')
print('1 - Binário')
print('2 - Octal')
print('3 - Hexadecimal')

# Escolha da conversão
escolha = int(input('Escolhe uma das opções de 1 a 3: '))

# Verificar a escolha do utilizador
if escolha == 1:
    print(f'O número {num} em binário é {bin(num)[2:]}')
elif escolha == 2:
    print(f'O número {num} em octal é {oct(num)[2:]}')
elif escolha == 3:
    print(f'O número {num} em hexadecimal é {hex(num)[2:]}')
else:
    print('Opção inválida!')

