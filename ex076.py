produtos = ('Lápis', 1.50,
            'Borracha', 2.50,
            'Caderno', 50.00,
            'Mochila', 80.00,
            'Tablet', 2500.00)

print(f'{"PRODUTOS E PREÇOS":^40}')

for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end = '')
    else:
        print(f'R${produtos[pos]:>7.2f}')