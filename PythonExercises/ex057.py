'''
057. Fazer um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''
sexo = input('Digita o sexo da pessoa [M/F]: ').strip().upper()  # Lê o sexo, remove espaços e converte para maiúsculas
while sexo != 'M' and sexo != 'F':  # Enquanto não for 'M' nem 'F', continua a pedir
    sexo = input('Valor inválido. Digita o sexo da pessoa [M/F]: ').strip().upper()  # Repete a leitura
print(f'Sexo {sexo} registado com sucesso!')  # Mensagem de confirmação
