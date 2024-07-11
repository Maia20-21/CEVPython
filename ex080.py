print('LISTA ORDENADA SEM REPETIÇÕES\n')
# sem o uso da função sort()

lista = []

for i in range(5):
    x = int(input('Digite um valor: '))
    if i == 0 or x > lista[-1]:
        lista.append(x)
        print(f'Adicionando o valor {x} no final da lista\n')
    else:
        pos = 0
        while pos < len(lista):
            if x <= lista[pos]:
                lista.insert(pos, x)
                print(f'Adicionando o valor {x} na posição {pos}\n')
                break
            pos += 1

print(f'Lista ordenada: {lista}')
