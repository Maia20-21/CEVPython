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