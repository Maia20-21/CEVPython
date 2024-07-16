print('ANÁLISE DE DADOS - MATRIZ\n')

matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for linha in range(3):
    for coluna in range(3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print()
for linha in range(3):
    for coluna in range(3):
        print(f'[{matriz[linha][coluna]:^5}]', end = ' ')
    print()

print(f'''
RESULTADOS
A soma da primeira linha é {sum(matriz[0])}
A soma da segunda linha é {sum(matriz[1])}
A soma da terceira linha é {sum(matriz[2])}
''')