x = int(input('Digite um número para ver sua tabuada: '))

print(f'\nTABUADA DO {x}\n')

for i in range(0, 11):
    print(f'{x} x {i} = {x*i}')