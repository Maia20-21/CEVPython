valores = []
pares = []

for i in range(4):
    while True:
        try:
            numero = int(input(f'Digite o {i+1}º valor: '))
            valores.append(numero)
            if numero % 2 == 0:
                pares.append(numero)
            break
        except ValueError:
            print("Por favor, insira um número válido.")

valores = tuple(valores)

print(f'O valor 9 apareceu {valores.count(9)} vezes')
print(f'O valor 3 aparece pela primeira vez na posição {valores.index(3) + 1}')
print(f'Números pares: {pares}')
