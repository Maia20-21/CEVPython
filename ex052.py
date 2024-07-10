x = int(input('Digite um número inteiro: '))

for i in range(1,10):
    if x % i == 0 and x != 1 and x != 2:
        print('Não é um número primo')
        break
    else:
        print('É um número primo')
        break