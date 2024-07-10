print('''
----- CADASTRO DE PESSOAS -----''')

maioridade = []
homens = []
mulheres_menos_20 = []

while True:
    while True:
        try:
            idade = int(input('\nIdade: '))
            if idade < 0:
                print("A idade não pode ser negativa. Tente novamente.")
            else:
                break
        except ValueError:
            print("Por favor, insira um número válido.")

    if idade >= 18:
        maioridade.append(idade)

    sexo = ' '
    while sexo not in 'FM':
        sexo = input('Sexo [F/M]: ').upper().strip()
        if sexo == 'M':
            homens.append(sexo)
        elif sexo == 'F' and idade < 20:
            mulheres_menos_20.append(sexo)

    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Deseja continuar? [S/N] ').upper().strip()
    if continuar == 'N':
        break
print('\n------ FIM DOS CADASTROS ------')

print(f'''
QUANTIDADE
Pessoas com mais de 18 anos: {len(maioridade)}
Homens: {len(homens)}
Mulheres com menos de 20 anos: {len(mulheres_menos_20)}''')

