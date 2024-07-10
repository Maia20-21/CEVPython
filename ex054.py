from datetime import date

atual = date.today().year

maior = 0
menor = 0

for i in range (1, 8):
    nascimento = int(input(f'Ano de nascimento da {i}º pessoa: '))
    idade = atual - nascimento
    if idade >= 18:
        maior += 1
    else:
        menor += 1

print(f'''
QUANTIDADE DE PESSOAS
Maiores de idade: {maior}
Menores de idade: {menor}
''')