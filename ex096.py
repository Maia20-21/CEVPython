print(f'{' ÁREA DE UM TERRENO ':-^50}')

def area(largura, comprimento):
    return largura*comprimento

largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))

print(f'A área de um terreno {largura} x {comprimento} é de {area(largura, comprimento)} m²')