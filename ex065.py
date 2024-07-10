print('MÉDIA, MAIOR E MENOR VALOR')

lista = []

while True:
    num = int(input('\nDigite um número inteiro: '))
    lista.append(num)

    continuar = input('\nDeseja continuar [S/N]? ').upper()
    while continuar not in 'SN':
        continuar = input('\nResposta inválida. Deseja continuar [S/N]? ').upper()

    if continuar == 'N':
        break

lista.sort()

print(f'''
Média: {sum(lista) / len(lista)}
Maior: {lista[-1]}
Menor: {lista[0]}
''')
