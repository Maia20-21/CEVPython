from random import randint

print(f'{'SORTEANDO E SOMANDO OS PARES':-^50}')

def sorteia(lista):
    for i in range(5):
        x = randint(1, 10)
        lista.append(x)
    return lista

def somaPar(*valores):
    soma = 0
    print('A soma dos valores pares ', end='')
    for valor in valores:
        if valor % 2 == 0:
            print(valor, end=' ')
            soma += valor
    print(f'é {soma}')

lista = []
print(sorteia(lista))
somaPar(*lista)