nome = input('Digite seu nome completo: ').strip()

print('Analisando seu nome...')
print(f'Maiúsculas: {nome.upper()}')
print(f'Minúsuclas: {nome.lower()}')
print(f'Letras: {len(nome) - nome.count(' ')} letras')

separa = nome.split()
print(f'{separa[0]}: {len(separa[0])} letras')
