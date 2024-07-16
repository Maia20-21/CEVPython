print('PESADINHOS E LEVINHOS')

pessoas = []
dados = []

while True:
    nome = input('\nNome: ')
    dados.append(nome)
    peso = int(input('Peso: '))
    dados.append(peso)
    pessoas.append(dados[:])
    dados.clear()

    continuar = input('\nDeseja continuar [S/N]? ').upper()
    if continuar != 'S':
        break

pessoas.sort(key=lambda x: x[1])

print(f'''
RESULTADOS

quantidade de pessoas cadastradas: {len(pessoas)}''')

menor_peso = pessoas[0][1]
print(f'O menor peso foi de {menor_peso} Kg. Peso de ', end = '')
for pessoa in pessoas:
    if pessoa[1] == menor_peso:
        print(f'{pessoa[0]}', end = ' ')

print()

maior_peso = pessoas[-1][1]
print(f'O maior peso foi de {maior_peso} Kg. Peso de ', end = '')
for pessoa in pessoas:
    if pessoa[1] == maior_peso:
        print(f'{pessoa[0]}', end = ' ')
