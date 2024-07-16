print(f'{' CADASTRO E ANÁLISE DE DADOS DE PESSOAS ':-^60}')

pessoas = []
temp = {}

while True:
    print()
    nome = input('Nome: ')
    temp['nome'] = nome

    while True:
        sexo = input('Sexo [F/M]: ').upper()
        if sexo in 'FM':
            temp['sexo'] = sexo
            break
        print('\nResposta inválida! Digite F ou M.\n')

    while True:
        try:
            idade = int(input('Idade: '))
            temp['idade'] = idade
            break
        except ValueError:
            print('\nResposta inválida! Digite um NÚMERO INTEIRO.\n')

    pessoas.append(temp.copy())
    temp.clear()

    while True:
        print()
        continuar = input('Deseja continuar [S/N]: ').upper()
        if continuar not in 'SN':
            print('\nResposta inválida. Digite "S" ou "N".\n')
        else:
            break
    if continuar == 'N':
        break
print()

print(f'{' RESULTADO ':-^40}')

print(f'• Total de pessoas cadastradas: {len(pessoas)}')

media_idade = sum(pessoa['idade'] for pessoa in pessoas) / len(pessoas)
print(f'• Média das idades: {media_idade:.2f} anos')

print('• Mulheres cadastradas: ', end = '')
for pessoa in pessoas:
    if pessoa['sexo'] == 'F':
        print(pessoa['nome'], end = ' ')

print('\n• Pessoas com idade acima da média: ', end = '')
for pessoa in pessoas:
    if pessoa['idade'] > media_idade:
        print(pessoa['nome'], end = ' ')
print()







