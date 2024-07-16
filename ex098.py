print(f'{' CONTAGEM ':-^30}')
def contador(a, b, c):
    if a < b:
        for i in range(a, b+1, c):
            print(i, end = ' ')
    else:
        if c < 0:
            for i in range(a, b-1, c):
                print(i, end = ' ')
        else:
            for i in range(a, b-1, -c):
                print(i, end = ' ')

a = int(input('Início: '))
b = int(input('Fim: '))
c = int(input('Passo: '))
print()
contador(a, b, c)