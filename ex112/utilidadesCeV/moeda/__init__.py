def aumentar(preco = 0, format = False):
    resultado = preco + preco * 0.1
    if format is False:
        return resultado
    else:
        return moeda(resultado)

def diminuir(preco = 0, format = False):
    resultado = preco - preco * 0.1
    if format is False:
        return resultado
    else:
        return moeda(resultado)

def dobro(preco = 0, format = False):
    resultado = preco * 2
    if format is False:
        return resultado
    else:
        return moeda(resultado)

def metade(preco = 0, format = False):
    resultado = preco / 2
    if format is False:
        return resultado
    else:
        return moeda(resultado)

def moeda(preco=0, moeda='R$ '):
    return f'{moeda}{preco:.2f}'.replace('.', ',')

def resumo(preco):
    print('-' * 40)
    print(f'{'RESUMO DO VALOR': ^40}')
    print('-' * 40)
    print(f'Preço analisado: \t\t{moeda(preco)}')
    print(f'Metade do preço: \t\t{metade(preco, True)}')
    print(f'Dobro do preço: \t\t{dobro(preco, True)}')
    print(f'Com 10% de aumento: \t{aumentar(preco, True)}')
    print(f'Com 10% de desconto: \t{diminuir(preco, True)}')
