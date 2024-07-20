print(f'{'FATORIAL':-^40}')

def fatorial(num):
    fat = 1
    for i in range(num, 0, -1):
        fat *= i
        if i == 1:
            print(i, end = ' = ')
        else:
            print(i, end=' x ')
    return fat

n = int(input('Digite um número: '))
print(fatorial(n))