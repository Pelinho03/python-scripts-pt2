'''
040. Criar um programa que leia duas notas de um aluno e calcule a média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO;
- Média entre 5.0 e 6.0: RECUPERAÇÃO;
- Média 7.0 ou superior: APROVADO.
'''
# Leitura das duas notas
nota1 = float(input('1ª nota: '))
nota2 = float(input('2ª nota: '))

# Cálculo da média
media = (nota1 + nota2) / 2

# Verificação da média e condição do aluno
if media < 5.0:
    print(f'Com as notas {nota1} e {nota2} tens média de {media:.1f}! REPROVADO!')
elif 5.0 <= media < 7.0:
    print(f'Com as notas {nota1} e {nota2} tens média de {media:.1f}! RECUPERAÇÃO!')
else:
    print(f'Com as notas {nota1} e {nota2} tens média de {media:.1f}! APROVADO!')

