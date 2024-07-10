from time import sleep

num1 = float(input('1º número: '))
num2 = float(input('2º número: '))

print('''
OPÇÕES
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
''')

opcao = int(input('Qual é a sua opção: '))

while opcao != 5:
    if opcao == 1:
        print(f'A soma entre {num1} e {num2} = {num1 + num2}')
    elif opcao == 2:
        print(f'A multiplicação entre {num1} e {num2} = {num1 * num2}')
    elif opcao == 3:
        if num1 > num2:
            print(f'{num1} é maior que {num2}')
        else:
            print(f'{num2} é maior que {num1}')
    elif opcao == 4:
        num1 = float(input('1º número: '))
        num2 = float(input('2º número: '))
    sleep(1)

    print('''
    OPÇÕES
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa
    ''')

    opcao = int(input('Qual é a sua opção: '))

sleep(0.5)
print('\nSaindo do programa...')