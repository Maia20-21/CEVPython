print('LISTAS COM PARES E ÍMPARES\n')

lista = [[], []]


for i in range(7):
    x = int(input(f'Digite o {i+1}ºvalor: '))
    if x % 2 == 0:
        lista[0].append(x)
    else:
        lista[1].append(x)

print(f'''
Números pares: {lista[0]}
Números ímpares: {lista[1]}
''')
