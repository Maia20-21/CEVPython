print('''
----- LOJA BARATINHA -----''')

total_gasto = []
mais_de_1000 = []
preco_minimo = float('inf')
produto_mais_barato = ' '


while True:
    produto = input('\nProduto: ').strip()

    while True:
        try:
            preco = float(input('Preço: R$ '))
            if preco < 0:
                print('O preço não pode ser negativo!')
            else:
                total_gasto.append(preco)

                if preco < preco_minimo:
                    preco_minimo = preco
                    produto_mais_barato = produto

                if preco > 1000:
                    mais_de_1000.append(preco)

                break
        except ValueError:
            print('Por favor, insira um número válido!')

    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Deseja continuar [S/N]: ').upper().strip()
    if continuar == 'N':
        break

print('\n------ FIM DAS COMPRAS ------')

print(f'''
PRODUTOS
Total gasto: R${sum(total_gasto):.2f}
Quantidade de produtos +R$ 1000.00: {len(mais_de_1000)}
Produto mais barato: {produto_mais_barato}
''')

