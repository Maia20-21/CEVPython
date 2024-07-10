lista = []

for i in range(1,4):
    x = int(input(f' {i}º valor: '))
    lista.append(x)
lista.sort()

print(f'Maior valor: {lista[2]}')
print(f'Menor valor: {lista[0]}')

