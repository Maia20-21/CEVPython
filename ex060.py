num = int(input('Digite um número para calcular seu fatorial: '))
resultado = 1
valor_inicial = num

while num > 0:
    print(f'{num}', end=' ')
    resultado *= num
    num -= 1
    if num > 0:
        print('x', end=' ')
    else:
        print('=', end=' ')

print(f' {resultado}')
