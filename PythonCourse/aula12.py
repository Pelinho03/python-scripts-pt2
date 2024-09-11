nome = str(input('Qual é o teu nome? '))
if nome == 'Paulo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Rita' or nome == 'João':
    print('O teu nome é popular em Portugal!')
elif nome in 'Ana Joana Maria':
    print('Belo nome!')
else:
    print('Um nome normal.')
print(f'Tem um bom dia, {nome}.')
