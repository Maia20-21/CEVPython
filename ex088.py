from time import sleep
from random import randint

print(f'{' MEGA SENA ':-^50}')

lista = []
temp = []

x = int(input('Quantos jogos você quer que eu sorteie? '))


for i in range(x):
    for c in range(6):
        num = randint(1, 60)
        if num not in lista:
            temp.append(num)
        else:
            num += 1
            temp.append(num)
    lista.append(temp[:])
    temp.clear()

print("\nPALPITES:")
for i, jogo in enumerate(lista):
    print(f'{i+1}º jogo: {jogo}')
    sleep(1)