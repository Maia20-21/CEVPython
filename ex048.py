c = 0

for i in range(1, 501, 2):
    if i % 3 == 0:
        c += i

print(f'A soma de todos os números múltiplos de 3 no intervalo de 1 a 500 é igual a {c}')