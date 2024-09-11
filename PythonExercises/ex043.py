'''
043. Desenvolver uma lógica que leia o peso e a altura de uma pessoa, calcular o sei IMC e mostrar o status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do Peso;
- Entre 18.5 e 25: Peso ideal;
- 25 até 30: Sobrepeso;
- 30 até 40: Obesidade;
- Acima de 40: Obesidade mórbida.
'''
# Leitura do peso e altura
peso = float(input('Peso (kg): '))
altura = float(input('Altura (cm): '))

# Conversão da altura de cm para metros
altura_m = altura / 100

# Cálculo do IMC
imc = peso / (altura_m ** 2)

# Determinação da categoria de IMC
if imc < 18.5:
    print(f'IMC de {imc:.2f}: Abaixo do peso.')
elif 18.5 <= imc < 25:
    print(f'IMC de {imc:.2f}: Peso ideal.')
elif 25 <= imc < 30:
    print(f'IMC de {imc:.2f}: Sobrepeso.')
elif 30 <= imc < 40:
    print(f'IMC de {imc:.2f}: Obesidade.')
else:
    print(f'IMC de {imc:.2f}: Obesidade mórbida.')

