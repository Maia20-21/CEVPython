soma = 0

for i in range(1, 7):
    x = int(input(f'{i}º número: '))
    if x % 2 == 0:
        soma += i
print(f'A soma dos números pares é {soma}')