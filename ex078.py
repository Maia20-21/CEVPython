lista = []

for i in range(0, 5):
    x = int(input(f'Digite um valor para a posição {i}: '))
    lista.append(x)
lista_ordenada = sorted(lista)

print(f'''Maior valor: {lista_ordenada[-1]}
Menor valor: {lista_ordenada[0]}''')