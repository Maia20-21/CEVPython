idades = 0
menorMulher = 0
maisVelho = 0
nomeMaisVelho = ''

for i in range(1, 5):
    print(f'\n{i}º PESSOA')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo (F ou M): ').strip().upper()

    idades += idade

    if sexo == 'F' and idade < 20:
        menorMulher += 1

    if sexo == 'M':
        if idade > maisVelho:
            maisVelho = idade
            nomeMaisVelho = nome

print(f'''
Média de idade do grupo : {idades / 4} anos
Nome do homem mais velho: {nomeMaisVelho}
Quantidade de mulheres com menos de 20 anos: {menorMulher}
''')