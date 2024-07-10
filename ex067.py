print('TABUADA DE X')

while True:
    num = int(input('\nDeseja ver a tabuada de qual valor? '))
    if num < 0:
        break
    print(f'\nTABUADA DO {num}')
    for i in range(0,11):
        print(f'{num} x {i} = {num * i}')
print('FIM')