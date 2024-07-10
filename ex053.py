frase = input('Digite uma frase: ')
frase2 = frase.upper().strip().split()
frase3 = ''.join(frase2)

contrario = ''

for i in range(len(frase3) - 1, -1, -1):
    contrario += frase3[i]

print(f'O contrário de {frase3} é {contrario}')

if frase3 == contrario:
    print('A frase é um palíndromo!')
else:
    print('A frase não é um palíndromo.')