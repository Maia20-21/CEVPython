pesos = []

for i in range(1, 6):
    peso = float(input(f'Peso da {i}º pessoa: '))
    pesos.append(peso)

ordenado = pesos.sort()

print(f'''
Mais pesado: {pesos[-1]} Kg
Menos pesado: {pesos[0]} Kg
''')